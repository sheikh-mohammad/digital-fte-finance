---
# SKILL.md uses YAML frontmatter. 'name' and 'description' are required. Claude reads description to auto-load. [Book: Ch.39]
name: finance-analyst
description: >
  Perform financial variance analysis decomposing P&L
  variances into volume, price, and mix components.
  Use for budget vs actual, quarterly review, CFO briefings.
# Be specific — this determines when Claude loads the skill autonomously.
---
<!-- Below frontmatter = instructions Claude follows when skill is active. -->
 
# Finance Analyst Skill
<!-- The factory's production unit — domain expertise packaged as reusable capability. [Book: Part 3, Ch.39] -->
 
## Methodology
 
### Step 1: Decomposition
Break each P&L variance into:
- Volume: delta_Q x P_budget
- Price: delta_P x Q_actual
- Mix: residual interaction
<!-- IDFA methodology — Intent-Driven Financial Architecture. [Book: Ch.17] -->
 
### Step 2: Controllability
- Within management control (pricing, headcount)
- Outside control (FX, regulation)
<!-- Makes output CFO-ready. Executives need to know what they can ACT on. -->
 
### Step 3: Forward Implication
State impact on full-year forecast.
 
## Escalation
<!-- Every SKILL.md MUST have escalation. AI executes; professionals judge. [Book: Part 3] -->
- Variance > 15% -> flag for CFO
- Restatement risk -> STOP and escalate
- Multi-jurisdiction tax -> route to tax team