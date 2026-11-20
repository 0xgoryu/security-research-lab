# security-research-lab

Personal lab notes and small tools from my smart-contract security research
and bug bounty work.

Everything here is written for learning and for testing on local forks or my
own accounts only. No unpublished findings, no target secrets, and no
credentials live in this repository — see `.gitignore`.

## Layout

- `notes/` — vulnerability patterns and EVM/DeFi concepts, one topic per file
- `tools/` — small, dependency-free Python helpers used during reviews
- `checklists/` — scope verification, dedupe, and pre-submission checklists
- `templates/` — report, PoC, and note templates

## Why this repo exists

I review contracts almost every day. This repo is where the reusable part of
that work lands: patterns I have checked, tools I keep re-writing, and
checklists that stop me from repeating mistakes. One meaningful commit per
day, from real work.

## Start here

- [30-day plan](PLAN-30-DAYS.md)
- [Scope verification checklist](checklists/scope-verification.md)
- [Scope matcher tool](tools/scope_match.py)
