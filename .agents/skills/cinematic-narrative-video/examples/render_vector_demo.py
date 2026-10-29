#!/usr/bin/env python3
"""Render the included SVG animation to a silent MP4 (optional dependencies)."""
from __future__ import annotations
import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, help="New .mp4 file; never overwrites")
    parser.add_argument("--fps", type=int, default=30, help="Frames per second (1–60; default 30)")
    parser.add_argument("--width", type=int, default=1280, help="Even output width (default 1280)")
    parser.add_argument("--height", type=int, default=720, help="Even output height (default 720)")
    args = parser.parse_args()
    if not 1 <= args.fps <= 60 or min(args.width, args.height) < 2 or args.width % 2 or args.height % 2:
        parser.error("fps must be 1–60; width and height must be positive even numbers")
    dest = Path(args.output).expanduser().absolute()
    if dest.suffix.lower() != ".mp4":
        parser.error("output must end with .mp4")
    if dest.exists() or dest.is_symlink():
        parser.error("output already exists; refusing to overwrite")
    if not dest.parent.is_dir():
        parser.error("output parent directory must already exist")
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        print("ffmpeg is required on PATH; no output was rendered.", file=sys.stderr)
        return 2
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Python Playwright and a supported Chromium installation are required.", file=sys.stderr)
        return 2
    html = Path(__file__).with_name("backyard-vector-demo.html").resolve()
    cmd = [ffmpeg, "-hide_banner", "-loglevel", "error", "-n", "-f", "image2pipe", "-framerate", str(args.fps),
           "-vcodec", "png", "-i", "pipe:0", "-an", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(dest)]
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            page = browser.new_page(viewport={"width": args.width, "height": args.height}, device_scale_factor=1)
            page.goto(html.as_uri() + "?t=0", wait_until="load")
            page.evaluate("document.fonts.ready")
            duration = page.evaluate("window.DURATION")
            if not isinstance(duration, (int, float)) or not 0 < duration <= 600:
                raise ValueError("Invalid demo duration")
            process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
            try:
                for frame in range(round(duration * args.fps)):
                    page.evaluate("t => window.seek(t)", frame / args.fps)
                    process.stdin.write(page.screenshot(type="png"))
                process.stdin.close()
                error = process.stderr.read().decode("utf-8", errors="replace")
                result = process.wait()
                if result:
                    raise RuntimeError(f"ffmpeg exited {result}: {error.strip()}")
            except BaseException:
                if process.stdin and not process.stdin.closed:
                    process.stdin.close()
                process.kill()
                process.wait()
                raise
            finally:
                browser.close()
    except Exception as exc:
        print(f"Render failed: {exc}. A partial file may exist at {dest}.", file=sys.stderr)
        return 1
    print(f"Rendered {dest}: {duration:g}s, {args.fps} fps, silent visual study (no narration or audio).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
