# Security Policy

## Supported versions

Security fixes, if provided, are intended for the latest commit on `main`. There are no published versioned releases or guaranteed response times. Update your local copy and review the changes before testing again.

## Reporting a vulnerability

Do **not** publish credentials, private videos or audio, personal information, full local paths, or a working exploit in a public issue.

Use the repository's **Security → Advisories → Report a vulnerability** option to report privately **if it is enabled**. If that option is unavailable, contact the maintainer through an existing private channel before disclosing details. No separate security email is currently listed; do not assume one exists. The maintainer can enable GitHub private vulnerability reporting in repository settings.

Include the affected commit, operating system, Python and MCP client versions, impact, steps to reproduce with harmless sample data, and any suggested mitigation. Redact tokens, private media, personal information, unrelated paths, and model/provider credentials. Coordinate disclosure with the maintainer where possible; no response or remediation timeline is promised.

## Security boundary

This project is an agent skill and an **optional local stdio MCP server**, not a sandbox or an authenticated remote service. The server runs with the permissions of the user launching the MCP client. Only connect it to clients you trust and do not expose its stdio interface publicly or over a network without a separate security design.

- `create_video_project` creates a new directory and draft files at a client-supplied path. The parent must exist and an already-existing destination is refused, but the server is not restricted to a workspace. A failure during creation can leave a partial directory. Review the destination and run with the least permissions appropriate to the task.
- `inspect_video` resolves a client-supplied local file path and executes the `ffprobe` found on `PATH` with a fixed argument list, no shell, and a 30-second timeout. Use a trusted `PATH` and a maintained `ffprobe`. The subprocess parses supplied media; untrusted media can exploit parser vulnerabilities or refer to external resources. The server does not provide network isolation or a parser sandbox.
- The server reads bundled guide files and returns their contents and, for the guide tool, local paths to the client. Project briefs and file paths are supplied by the client. The server itself does not explicitly upload files or include telemetry, but the client, model provider, `ffprobe`, or other tools may process or transmit data according to their own behavior and settings.
- Requests, returned guide text, media metadata, and any material read or produced by an agent can be untrusted. The server does not enforce content authenticity, fact accuracy, copyright clearance, safety, or resource limits for all inputs. Review agent actions and outputs; a timeline check is not a security or quality review.

For further setup, capabilities and limitations, see [the MCP guide](mcp/README.md). For the example-frame rights notice, see [reference-frame study images](.agents/skills/cinematic-narrative-video/reference-frames/README.md).
