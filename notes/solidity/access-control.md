# Access control failures

## Summary
A privileged action that can be called by anyone — because the check is missing, applied to the wrong function, or bypassable through an unguarded initialiser or upgrade path.

## Vulnerable pattern
`onlyOwner` on the setter but not on the function that moves funds; an `initialize()` anyone can call on a fresh proxy; role checks done in the UI only.

## Safe pattern
Every state-changing privileged function checks a role on-chain; initialisers are locked on the implementation and called exactly once through the proxy.

## Review checks
- List every external/public state-changing function and its modifier.
- Check initialise/upgrade paths separately from normal functions.
- Verify role admin assignment: who can grant the role that the check relies on?

## My examples
<!-- Add one sanitised example from this week's own review before committing.
     No unpublished findings, no target secrets. -->
