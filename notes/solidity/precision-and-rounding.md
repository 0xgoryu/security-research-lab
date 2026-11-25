# Precision loss and rounding

## Summary
Integer division truncates. When a protocol divides before it multiplies, or rounds in the user's favour in a loop, small losses compound into real value — or brick withdrawals.

## Vulnerable pattern
`amount / total * share` ordering; fees rounded down to zero for small amounts; exchange rates that can round a deposit to zero shares.

## Safe pattern
Multiply before dividing, use a vetted fixed-point library, round against the user on deposits and in the protocol's favour on fees, and reject zero-output operations.

## Review checks
- Grep for `/` before `*` in share/fee math.
- Test dust amounts: does a tiny deposit mint zero shares but still take the funds?
- Check rounding direction on every fee and share conversion, both ways.

## My examples
<!-- Add one sanitised example from this week's own review before committing.
     No unpublished findings, no target secrets. -->
