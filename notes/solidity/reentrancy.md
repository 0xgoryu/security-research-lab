# Reentrancy

## Summary
A contract that sends value (or calls an untrusted contract) before updating its own state can be re-entered, letting the callee repeat the operation against the stale state.

## Vulnerable pattern
External call first, balance/state update after it — or a cross-function path where one function guards state that another function spends.

## Safe pattern
Checks-Effects-Interactions order, state updated before any external call, and a reentrancy guard on functions that share state.

## Review checks
- Grep for `.call{`, `transfer`, and hook callbacks, then trace whether every state variable they rely on is written before the call.
- Check cross-function and read-only reentrancy, not just the obvious single-function case.
- Confirm the guard covers all entry points that touch the same balances.

## My examples
Worked example (sanitised, no target): a withdraw function that calls
`token.transfer(msg.sender, amount)` and only then does
`balances[msg.sender] -= amount`. Re-entered through a token hook, the second
call reads the stale balance and drains again. Fix: set the balance first,
then transfer, and keep a guard on every entry point that touches the same
balance. When tracing this week, the check that caught the ordering was
following the call graph past the function text — a helper that updates state
in the caller can make an innocent-looking callee safe, and a caller that
defers the update can make a guarded-looking callee unsafe.
