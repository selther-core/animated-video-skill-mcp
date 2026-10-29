#!/usr/bin/env python3
"""End-to-end smoke tests for the server's stdio JSON-RPC interface."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent.parent
SERVER = ROOT / "mcp" / "server.py"
SKILL_ROOT = ROOT / ".agents" / "skills" / "cinematic-narrative-video"

def req(ident, method, params=None):
    return {"jsonrpc": "2.0", "id": ident, "method": method, "params": params or {}}

def run_server(messages):
    data = "".join(json.dumps(m) + "\n" for m in messages)
    p = subprocess.run([sys.executable, str(SERVER)], input=data, text=True, capture_output=True, timeout=30, check=True)
    if p.stderr:
        raise AssertionError(f"Unexpected stderr: {p.stderr}")
    return [json.loads(line) for line in p.stdout.splitlines()]

def call(ident, name, arguments):
    return req(ident, "tools/call", {"name": name, "arguments": arguments})

def tool_data(response):
    assert not response["result"]["isError"], response
    return json.loads(response["result"]["content"][0]["text"])

class MCPTests(unittest.TestCase):
    def test_handshake_discovery_resources_and_prompt(self):
        msgs = [req(1, "initialize", {"protocolVersion": "2025-06-18", "capabilities": {}, "clientInfo": {"name": "smoke", "version": "1"}}),
                {"jsonrpc": "2.0", "method": "notifications/initialized"}, req(2, "tools/list"), req(3, "resources/list"),
                req(4, "resources/read", {"uri": "cinematic://guide/niche"}), req(5, "prompts/list"),
                req(6, "prompts/get", {"name": "create_niche_video", "arguments": {"topic": "bread", "niche": "business"}})]
        out = run_server(msgs)
        self.assertEqual(len(out), 6)
        self.assertEqual(out[0]["result"]["protocolVersion"], "2025-06-18")
        self.assertEqual(len(out[1]["result"]["tools"]), 5)
        self.assertTrue(out[2]["result"]["resources"])
        self.assertIn("any niche", out[3]["result"]["contents"][0]["text"].lower())
        self.assertEqual(out[4]["result"]["prompts"][0]["name"], "create_niche_video")
        self.assertIn("bread", out[5]["result"]["messages"][0]["content"]["text"])

    def test_extracted_frame_guide_and_images(self):
        reply = run_server([call(1, "read_skill_guide", {"guide": "visual"})])[0]
        guide = tool_data(reply)
        self.assertIn("reference-frames", guide["content"])
        self.assertEqual(len(list((SKILL_ROOT / "reference-frames").glob("*.jpg"))), 8)
        self.assertIn("rights", (SKILL_ROOT / "reference-frames" / "README.md").read_text().lower())

    def test_agent_compatibility_and_quickstart(self):
        reply = run_server([call(1, "read_skill_guide", {"guide": "compatibility"})])[0]
        guide = tool_data(reply)
        self.assertIn("Text-only agent", guide["content"])
        readme = (ROOT / "README.md").read_text()
        self.assertIn("# Installation", readme)
        self.assertIn("Install the cinematic-narrative-video skill", readme)
        self.assertIn("MCP is optional", readme)
        installation_prompt = readme.split("```text", 1)[1].split("```", 1)[0].strip()
        self.assertLess(len(installation_prompt), 250)
        self.assertIn("https://github.com/selther-core/animated-video-skill-mcp", installation_prompt)
        self.assertNotIn("Do not create a video", installation_prompt)
        resources = run_server([req(1, "resources/list")])[0]["result"]["resources"]
        self.assertIn("cinematic://guide/compatibility", [r["uri"] for r in resources])

    def test_american_voice_guide_and_prompt(self):
        responses = run_server([
            call(1, "read_skill_guide", {"guide": "voice"}),
            req(2, "resources/read", {"uri": "cinematic://guide/voice"}),
            req(3, "prompts/get", {"name": "create_niche_video", "arguments": {"topic": "bread", "niche": "business"}}),
        ])
        guide = tool_data(responses[0])["content"]
        self.assertIn("All spoken voices in this skill must use an American accent", guide)
        self.assertIn("en-US", guide)
        self.assertIn("Voice types to use for each niche", guide)
        self.assertIn("Topic scripts and voice examples", guide)
        self.assertIn("energetic, confidently projected, clear and engaging", guide)
        self.assertIn("Loud does not mean shouting, clipping", guide)
        self.assertIn("The bakery queue", guide)
        self.assertEqual(responses[1]["result"]["contents"][0]["text"], guide)
        prompt = responses[2]["result"]["messages"][0]["content"]["text"]
        self.assertIn("All spoken voices must use an American accent", prompt)

    def test_code_animation_guide_and_demo(self):
        out = run_server([
            call(1, "read_skill_guide", {"guide": "animation"}),
            req(2, "resources/read", {"uri": "cinematic://guide/animation"}),
            req(3, "prompts/get", {"name": "create_niche_video", "arguments": {"topic": "oil", "niche": "education"}}),
        ])
        guide = tool_data(out[0])["content"]
        self.assertIn("do not call an image-generation model", guide.lower())
        self.assertIn("What was inspected—and what cannot be known", guide)
        self.assertEqual(out[1]["result"]["contents"][0]["text"], guide)
        prompt = out[2]["result"]["messages"][0]["content"]["text"]
        self.assertIn("do not use image generation", prompt)
        self.assertIn("style test", prompt)
        demo = (SKILL_ROOT / "examples" / "backyard-vector-demo.html").read_text()
        self.assertIn("window.seek=seek", demo)
        self.assertIn('id="person"', demo)
        self.assertIn('id="diagram-scene"', demo)
        self.assertNotIn("<img", demo.lower())
        self.assertTrue((SKILL_ROOT / "examples" / "render_vector_demo.py").is_file())

    def test_staging_and_current_rig(self):
        replies = run_server([
            call(1, "read_skill_guide", {"guide": "staging"}),
            req(2, "resources/read", {"uri": "cinematic://guide/staging"}),
            call(3, "read_skill_guide", {"guide": "rig"}),
        ])
        guide = tool_data(replies[0])["content"]
        self.assertIn("lighting", guide.lower())
        self.assertIn("cutaway", guide.lower())
        self.assertEqual(guide, replies[1]["result"]["contents"][0]["text"])
        self.assertIn("back arm → torso → near leg → front arm", tool_data(replies[2])["content"])
        demo = (SKILL_ROOT / "examples" / "staging-rig-demo.html").read_text()
        self.assertIn("window.seek=seek", demo)
        self.assertIn('class="backArm"', demo)
        self.assertIn('class="torso"', demo)
        self.assertIn('class="frontArm"', demo)
        self.assertLess(demo.index('class="backArm"'), demo.index('class="torso"'))
        self.assertLess(demo.index('class="torso"'), demo.index('class="frontArm"'))
        self.assertNotIn("<img", demo.lower())
        self.assertNotIn("<audio", demo.lower())

    def test_create_and_no_overwrite(self):
        with tempfile.TemporaryDirectory() as parent:
            folder = str(Path(parent) / "video")
            args = {"directory": folder, "topic": "Forest", "niche": "Fiction", "audience": "Families", "length": "1 minute", "format": "16:9"}
            first, second = run_server([call(1, "create_video_project", args), call(2, "create_video_project", args)])
            self.assertEqual(tool_data(first)["status"], "draft_scaffold_created")
            self.assertTrue(second["result"]["isError"])
            self.assertEqual(json.loads((Path(folder)/"brief.json").read_text())["niche"], "Fiction")
            self.assertTrue((Path(folder)/"timeline.json").is_file())
            self.assertIn("Do not use AI image generation", (Path(folder)/"storyboard.md").read_text())
            self.assertIn("voiced, code-drawn style test", (Path(folder)/"quality_report.md").read_text())

    def test_timeline_and_srt(self):
        good = {"duration_seconds": 10, "shots": [{"start": 0, "end": 4}, {"start": 4, "end": 10}]}
        bad = {"duration_seconds": 10, "shots": [{"start": 0, "end": 4}, {"start": 5, "end": 10}]}
        o = run_server([call(1,"validate_timeline", {"timeline":good}), call(2,"validate_timeline", {"timeline":bad}),
                        call(3,"make_srt", {"cues":[{"start":1.25,"end":2.5,"text":"Hello."}]}),
                        call(4,"make_srt", {"cues":[{"start":2,"end":1,"text":"Bad."}]})])
        self.assertTrue(tool_data(o[0])["timing_valid"])
        self.assertFalse(tool_data(o[1])["timing_valid"])
        self.assertIn("00:00:01,250 --> 00:00:02,500", tool_data(o[2])["srt"])
        self.assertTrue(o[3]["result"]["isError"])

    def test_invalid_tool_and_absent_video(self):
        out = run_server([call(1, "bad_tool", {}), call(2, "inspect_video", {"path": "/path-that-does-not-exist"})])
        self.assertTrue(out[0]["result"]["isError"])
        self.assertTrue(out[1]["result"]["isError"])

if __name__ == "__main__":
    unittest.main()
