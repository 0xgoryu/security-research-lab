# Calldata layout

## Summary
Calldata is the raw input to a contract call: a 4-byte function selector followed by ABI-encoded arguments in 32-byte words. Reading it fluently makes manual review and PoC debugging much faster.

## Vulnerable pattern
Not a vulnerability by itself — but misunderstood padding, dynamic offsets, or `abi.encodePacked` with multiple dynamic types create hash collisions and parsing bugs in the contracts that consume calldata.

## Safe pattern
Use strict `abi.decode`, avoid `encodePacked` for hashing multiple dynamic values, and validate lengths before slicing calldata manually.

## Review checks
- Decode the selector first: does it match the function you think ran?
- For dynamic types, verify offset and length words before trusting the payload.
- Check any manual calldata slicing for missing length bounds.

## My examples
<!-- Add one sanitised example from this week's own review before committing.
     No unpublished findings, no target secrets. -->
