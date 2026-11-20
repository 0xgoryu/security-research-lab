# 30-day commit plan

Start: Friday 20 November 2026 (Day 1) — Finish: Saturday 19 December 2026 (Day 30)

Rule: exactly one meaningful commit per calendar day, in a public repo, with the git email that matches this GitHub account. Ten commits in one day still count as one day for the Human Passport GitHub stamp.

Before each commit: edit the day's file, add at least a few lines of your own from that day's real review work, run any code once, then commit with the listed message.

| Day | Date | File | Commit message |
|---|---|---|---|
| 1 | Fri 2026-11-20 | README, checklists/scope-verification.md, tools/scope_match.py, templates/report-template.md | `init: security research lab, scope checklist and scope matcher` |
| 2 | Sat 2026-11-21 | notes/solidity/reentrancy.md | `notes: reentrancy pattern and checks` |
| 3 | Sun 2026-11-22 | tools/convert_units.py | `tools: wei/ether unit converter` |
| 4 | Mon 2026-11-23 | notes/solidity/access-control.md | `notes: access control failures` |
| 5 | Tue 2026-11-24 | templates/foundry/PocTemplate.t.sol | `templates: foundry fork PoC template` |
| 6 | Wed 2026-11-25 | notes/solidity/precision-and-rounding.md | `notes: precision loss and rounding` |
| 7 | Thu 2026-11-26 | checklists/dedupe-checklist.md | `checklists: duplicate search before drafting` |
| 8 | Fri 2026-11-27 | notes/solidity/oracle-manipulation.md | `notes: price oracle manipulation` |
| 9 | Sat 2026-11-28 | notes/evm/calldata-layout.md | `notes: calldata layout basics` |
| 10 | Sun 2026-11-29 | checklists/pre-submission-gates.md | `checklists: pre-submission gates` |
| 11 | Mon 2026-11-30 | notes/solidity/flash-loans.md | `notes: flash loan attack surface` |
| 12 | Tue 2026-12-01 | tools/findings_to_table.py | `tools: findings CSV to markdown table` |
| 13 | Wed 2026-12-02 | notes/solidity/proxy-and-upgrades.md | `notes: proxy and upgrade pitfalls` |
| 14 | Thu 2026-12-03 | templates/hunt-notes-template.md | `templates: per-target hunt notes` |
| 15 | Fri 2026-12-04 | notes/solidity/signature-replay.md | `notes: signature replay and permit pitfalls` |
| 16 | Sat 2026-12-05 | tools/address_book.py | `tools: local address label book` |
| 17 | Sun 2026-12-06 | notes/defi/vault-share-inflation.md | `notes: vault share inflation (first-depositor)` |
| 18 | Mon 2026-12-07 | checklists/fork-poc-checklist.md | `checklists: fork PoC discipline` |
| 19 | Tue 2026-12-08 | notes/solidity/denial-of-service.md | `notes: denial of service patterns` |
| 20 | Wed 2026-12-09 | notes/evm/event-logs.md | `notes: event logs and topics` |
| 21 | Thu 2026-12-10 | notes/solidity/front-running-and-mev.md | `notes: front-running and MEV basics` |
| 22 | Fri 2026-12-11 | templates/cvss-worksheet.md | `templates: honest CVSS worksheet` |
| 23 | Sat 2026-12-12 | notes/defi/amm-basics.md | `notes: AMM invariants for reviewers` |
| 24 | Sun 2026-12-13 | tools/redact.py | `tools: redact secrets and addresses before publishing` |
| 25 | Mon 2026-12-14 | notes/solidity/non-standard-tokens.md | `notes: non-standard ERC20 pitfalls` |
| 26 | Tue 2026-12-15 | checklists/duplicate-search-sources.md | `checklists: where duplicates hide` |
| 27 | Wed 2026-12-16 | notes/evm/storage-layout.md | `notes: storage layout essentials` |
| 28 | Thu 2026-12-17 | notes/review-lessons.md | `notes: lessons from closed hunts` |
| 29 | Fri 2026-12-18 | tools/check_commit_ready.sh | `tools: pre-commit sanity check script` |
| 30 | Sat 2026-12-19 | notes/next-60-days.md | `notes: plan for days 31-60 (Active Developer)` |

After Day 30: verify the GitHub stamp in Human Passport (it counts distinct commit days in public repos over the past 3 years), then continue with `notes/next-60-days.md` toward 60 days.
