# **Claude Code *Project Lab***

## **Explore a real Agent Factory project.**

This is a simulated Digital FTE project — a real Claude Code project built using the Agent Factory methodology. Every file is genuine: `settings.json` with hooks, `SKILL.md` with YAML frontmatter, agents, plugins, and MCP configs. Click any file to see the real artifact, annotated.

> *Open a file. Read the source. Learn. Build.*

### [CLAUDE.md](./CLAUDE.md)

How your Digital FTE remembers identity, constraints, and workflow across sessions. Your project's persistent memory.

### [Settings & Permissions](.claude/settings.json)

Configure behaviour, tool access, lifecycle hooks, and safety guardrails. All in one settings.json.

### [Custom Slash Commands (***deprecated***)](.claude/commands/deploy-fte.md)

Saved workflows you can invoke with a keystroke.

### [Skills](.claude/skills/finance-analyst/SKILL.md)

Teach your Digital FTE specialised domain knowledge it loads autonomously when needed.

### [MCP Servers](.mcp.json)

Connect to external tools, APIs, and services via a standard protocol.

### [Hooks](.claude/settings.json)

Run custom scripts automatically before or after your agent's tool calls.

### [Subagents](.claude/agents/researcher.md)

Custom subagents with YAML frontmatter. Built-in: Explore (fast search), Plan (read-only research), general-purpose (all tools).

### [Plugins](.claude-plugin/plugin.json)

Package skills, agents, hooks, and MCP servers into shareable, distributable extensions.

### [Specs & Evals](./specs/digital-fte.spec.md)

Define what the FTE must do with typed contracts, then measure quality with LLM-as-judge.