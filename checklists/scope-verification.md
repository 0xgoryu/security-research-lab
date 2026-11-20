# Scope verification checklist

Run this before testing or reporting anything. A target being *named* in a
brief is not the same as it being *in scope*.

1. Open the live program brief, not a cached copy or an aggregator summary.
2. Find the exact section heading the target sits under:
   - "In scope" / "Targets" heading -> in scope.
   - "Out of scope targets" heading -> stop, even if the name looks familiar.
3. Note the exact target form: domain pattern, contract address, repo, or
   SDK package and version. A repo name is not a tenant, and a tenant is not
   a repo.
4. Check the deployed address against the brief. If the live deployment
   points to a different implementation address than the brief lists,
   verify that address separately before trusting any result.
5. Record the reward table and the submission gates (fees, KYC / identity
   verification, PoC required or not) from the live page.
6. Record what is explicitly excluded: known issues, audit findings,
   automated scanning, specific vulnerability classes.
7. Only test accounts, tenants, and assets the program provisioned or that
   you created for the program. Never test self-created lookalike tenants
   when the brief only covers program-provisioned ones.
8. Save the date and a link to the brief next to the hunt notes.

Lesson baked in: one report was once submitted against a repository that sat
under the brief's "Out of scope targets" heading. Reading the heading, not
just the target list, would have caught it in ten seconds.
