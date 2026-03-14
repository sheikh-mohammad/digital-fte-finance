"""Digital FTE: Financial Analyst"""
# You wrote the SPEC; Claude Code generated this. [Book: Part 4, Ch.36]

from agent_factory import AgentFactory


def create_analyst():
    factory = AgentFactory("CLAUDE.md")
    # Reads CLAUDE.md + .claude/ for skills, agents, hooks.
    factory.load_skill("finance-analyst")
    # From .claude/skills/finance-analyst/SKILL.md
    factory.load_skill("banking-ai")
    factory.connect_mcp(".mcp.json")
    factory.deploy_agent("researcher")
    factory.deploy_agent("auditor")
    return factory.build()


# Intent -> Factory -> Outcome.

if __name__ == "__main__":
    create_analyst().run()
