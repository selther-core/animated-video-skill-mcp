#!/usr/bin/env python3
"""Render an authored seekable HTML scene to MP4; optionally mux an existing mix.

Requires Python Playwright, its Chromium browser and FFmpeg with libx264 on PATH.
The HTML must define window.DURATION (seconds) and window.seek(t). No media,
voice or motion is created by this script: the HTML must implement animation.
Only use trusted local HTML; it executes JavaScript in a local browser.
"""
from __future__ import annotations

import argparse
import math
import shutil
import subprocess
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--html", required=True, help="Trusted authored local HTML with window.seek(t) and window.DURATION")
    parser.add_argument("--output", required=True, help="New .mp4 file; existing files are never overwritten")
    parser.add_argument("--audio", help="Optional existing final audio mix; it must already be timed to this output")
    parser.add_argument("--fps", type=int, default=30)
    parser.add_argument("--width", type=int, default=1280)
    parser.add_argument("--height", type=int, default=720)
    parser.add_argument("--start", type=float, default=0, help="First scene time, in seconds")
    parser.add_argument("--duration", type=float, help="Clip duration in seconds (default: remainder of scene)")
    args = parser.parse_args()
    if not 1 <= args.fps <= 60 or min(args.width, args.height) < 2 or args.width % 2 or args.height % 2:
        parser.error("fps must be 1–60 and dimensions must be positive even numbers")
    if not math.isfinite(args.start) or args.start < 0 or (args.duration is not None and (not math.isfinite(args.duration) or args.duration <= 0)):
        parser.error("start must be finite and nonnegative; duration must be finite and positive")
    html = Path(args.html).expanduser().resolve()
    dest = Path(args.output).expanduser().absolute()
    audio = Path(args.audio).expanduser().resolve() if args.audio else None
    if not html.is_file() or html.suffix.lower() not in (".html", ".htm"):
        parser.error("html must be an existing local .html or .htm file")
    if dest.suffix.lower() != ".mp4" or dest.exists() or dest.is_symlink() or not dest.parent.is_dir():
        parser.error("output must be a new .mp4 in an existing directory")
    if audio and not audio.is_file():
        parser.error("audio must be an existing file")
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        print("FFmpeg is required on PATH; no file was rendered.", file=sys.stderr)
        return 2
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Python Playwright and its Chromium browser are required.", file=sys.stderr)
        return 2

    process = None
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            page = browser.new_page(viewport={"width": args.width, "height": args.height}, device_scale_factor=1)
            errors: list[str] = []
            page.on("pageerror", lambda error: errors.append(str(error)))
            # The template is intentionally self-contained. Do not leak data to network URLs.
            page.route("**/*", lambda route: route.continue_() if route.request.url.startswith(("file:", "data:", "blob:")) else route.abort())
            page.goto(html.as_uri() + "?t=0", wait_until="load")
            page.evaluate("document.fonts.ready")
            has_seek = page.evaluate("typeof window.seek === 'function'")
            scene_duration = page.evaluate("window.DURATION")
            if not has_seek or isinstance(scene_duration, bool) or not isinstance(scene_duration, (int, float)) or not math.isfinite(scene_duration) or not 0 < scene_duration <= 3600:
                raise ValueError("HTML must expose a seek function and a finite window.DURATION between 0 and 3600 seconds")
            if args.start >= scene_duration:
                raise ValueError("start must be before the end of the scene")
            duration = args.duration if args.duration is not None else scene_duration - args.start
            if args.start + duration > scene_duration + 1e-8:
                raise ValueError("requested clip extends beyond the scene duration")
            frames = math.ceil(duration * args.fps - 1e-9)
            actual = frames / args.fps
            cmd = [ffmpeg, "-hide_banner", "-loglevel", "error", "-n", "-f", "image2pipe", "-framerate", str(args.fps), "-vcodec", "png", "-i", "pipe:0"]
            if audio:
                cmd += ["-i", str(audio), "-map", "0:v:0", "-map", "1:a:0", "-af", "apad", "-t", str(actual), "-c:a", "aac", "-b:a", "192k"]
            else:
                cmd += ["-an"]
            cmd += ["-frames:v", str(frames), "-c:v", "libx264", "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(dest)]
            process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
            assert process.stdin is not None and process.stderr is not None
            for frame in range(frames):
                page.evaluate("t => window.seek(t)", args.start + frame / args.fps)
                if errors:
                    raise RuntimeError("HTML page error: " + errors[0])
                process.stdin.write(page.screenshot(type="png", animations="disabled"))
            process.stdin.close()
            message = process.stderr.read().decode("utf-8", errors="replace")
            if process.wait() != 0:
                raise RuntimeError("ffmpeg failed: " + message.strip())
            browser.close()
        print(f"Rendered {dest}: {actual:.3f}s, {args.fps} fps, {frames} frames, {'existing audio mix' if audio else 'silent'}. Inspect the actual output; this is not a quality check.")
        return 0
    except Exception as exc:
        if process is not None and process.poll() is None:
            if process.stdin and not process.stdin.closed:
                process.stdin.close()
            process.kill()
            process.wait()
        print(f"Render failed: {exc}. A partial output may exist at {dest}.", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
