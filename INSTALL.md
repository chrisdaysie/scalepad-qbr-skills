# Install the ScalePad QBR Skill Kit

This kit contains 18 portable skills for agents using ScalePad MCP tools. The recommended installation uses [`skill-kit.json`](skill-kit.json) as the exact package definition. Skill descriptions and instructions remain in the listed Markdown files.

## Requirements

- An agent host that can install named Markdown skills, instruction files, or equivalent prompt resources.
- An authenticated ScalePad MCP connection available to the agent at runtime.
- Human approval immediately before any `/qbr-apply` write. Every other skill is read-only.
- Optional `load_skill` support for automatic composition. Without it, invoke the selected specialist directly or let the coordinator read its installed instructions.

## Recommended GitHub import

Give the importer the repository URL:

```text
https://github.com/chrisdaysie/scalepad-qbr-skills
```

A safe importer should:

1. Resolve the requested branch, tag, or default branch to one immutable Git commit SHA.
2. Fetch `skill-kit.json` from that SHA and validate its schema.
3. Fetch every listed skill from the same SHA.
4. Verify that commands, paths, frontmatter names, entry points, and version agree.
5. Preview the repository, kit ID, version, entry points, commands, and resolved commit SHA.
6. Install the already-fetched files atomically after approval.
7. Record the repository URL for display and the commit SHA as the exact installed revision.

Do not preview from one revision and install from a mutable branch later. Do not discover additional skills by scanning the README or repository.

### Kit identity

For a GitHub source, identify the installed kit by:

```text
(provider, host, GitHub repository ID, manifest ID)
```

For this repository, the manifest ID is `scalepad-qbr`. The repository ID comes from GitHub and must not be copied into the manifest. Repository renames and transfers retain identity; forks receive their own repository ID and therefore their own kit identity.

`entryPoints` contains recommended starting commands. It does not make the other listed skills private or unavailable.

## Manual installation

Use `skill-kit.json` as the checklist even when the host cannot import it directly.

### Skill-native hosts

Upload every listed Markdown file as one skill. Use its frontmatter `name` as the command. Install the complete list when you want `/qbr` and other coordinators to compose specialists through `load_skill`.

### Agent Skills-style hosts

Place each listed file in its own skill folder as `SKILL.md`:

```text
<skills-root>/
├── qbr/SKILL.md
├── qbr-prep/SKILL.md
├── qbr-apply/SKILL.md
└── ...15 more skills
```

The Markdown content does not need to be rewritten. Invoke the host's equivalent of `/qbr`, `$qbr`, or a named-skill action.

### Prompt or custom-assistant hosts

Attach only the smallest relevant specialist set. Start with `/qbr-prep` for a complete plan or a focused skill such as `/saas-evidence` for a narrow review. If the host cannot retrieve another installed skill, composition is manual and reduced coverage should be disclosed.

### SDK and workflow orchestrators

Register each manifest entry as a named instruction resource. Pass stable client and record IDs, explicit dates, and timezone between steps. Keep write tools unavailable to read-only skills and place the approval boundary immediately before `/qbr-apply` executes a write.

## Convert for an AI IDE

`skill-kit.json` is intentionally independent of any IDE's packaging convention. An IDE or adapter can convert the kit without parsing the README or changing the canonical prompts:

1. Resolve and fetch the manifest and listed files from one commit SHA.
2. Iterate the manifest's `skills` array in order.
3. Parse each file's `name` and `description` frontmatter and verify that `name` matches `command`.
4. Emit the host's required wrapper while preserving the Markdown instructions.
5. Register `command` as the stable skill or slash-command name and `qbr` as the recommended entry point.
6. Map `load_skill` to the host's named-skill resolver when available. Otherwise retain direct specialist invocation and disclose reduced automatic composition.
7. Preserve the read-only boundary for every skill except `/qbr-apply`, including its preview and explicit-approval requirement.
8. Record the source repository and commit SHA with the generated package so it can be reproduced and updated safely.

Common conversions are:

| Host capability | Conversion |
| --- | --- |
| Skill folders | Copy each source file to `<skills-root>/<command>/SKILL.md`. |
| Slash commands | Register `command` as the command name, `description` as discovery metadata, and the Markdown body as its instructions. |
| Rules or prompt libraries | Store each skill as a separately retrievable instruction resource; do not make all 18 globally active. |
| Multi-agent or workflow SDKs | Register each command as a named prompt resource and implement `load_skill` as an allowlisted lookup over the installed manifest set. |

Generated host-specific files are installation artifacts, not new sources of truth. Update them by reconverting a validated pinned revision rather than editing them independently.

## Verify the source checkout

Run the dependency-free validator before installing or publishing a revision:

```bash
python3 scripts/validate-skills.py
```

It verifies the manifest's exact install list, safe paths, unique commands and paths, frontmatter alignment, entry points, version parity, skill references, and README catalog links.

After installation, confirm that:

- `/qbr` is available as the recommended entry point.
- Specialist commands are directly available.
- A coordinator can load an available specialist when the host exposes `load_skill`.
- `/qbr-apply` still previews the exact write batch and waits for explicit approval.

## Update an installation

Resolve the desired Git ref to a new commit SHA and repeat the same fetch, validation, preview, and atomic-install flow. Treat it as an update only when the provider, host, GitHub repository ID, and manifest ID match the installed identity. Show command, file, version, and permission-boundary changes before approval.

Never replace the recorded installed SHA until the new revision has installed successfully.

## Troubleshooting

- **A referenced skill cannot load:** confirm it is listed in the manifest, installed, and available to the user on the current turn.
- **`load_skill` is unavailable:** invoke the specialist directly; do not substitute an unrelated tool.
- **A ScalePad operation is missing:** verify the MCP connection, product access, and live tool contract. Record reduced coverage instead of inventing a fallback.
- **Manifest validation fails:** stop the installation. Do not fall back to README scraping or an unpinned branch.
- **A fork appears as a new kit:** expected; forks have distinct GitHub repository IDs.

Removing the skills does not delete or roll back any ScalePad records previously created through an approved write.
