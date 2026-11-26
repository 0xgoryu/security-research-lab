# Duplicate search checklist

Run before writing a full draft. A public CLEAR is not a guarantee —
private submissions are invisible — but a public HIT is a hard stop.

1. Search the program's disclosed reports for the same root cause.
2. Search published audits of the exact in-scope code (all firms, all years).
3. Search the repo: issues, merged and *unmerged* PRs, security advisories.
4. Search by mechanism, not by title: the vulnerable function name, the
   invariant it breaks, and synonyms for the impact.
5. Check CVEs / GHSA for SDK and library targets.
6. Check the program's known-issues list — anything listed there is dead.
7. Record: sources searched, queries used, date, verdict (CLEAR / RISKY /
   DUPLICATE) and who ran the search.
8. Run a second, independent pass before submitting. RISKY means hold for
   a human decision, not submit-and-hope.
