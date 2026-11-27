# Price oracle manipulation

## Summary
If a lending or settlement path reads a spot price that one trade can move — a single DEX pool, a short TWAP window, an unvalidated feed — the price becomes an attacker input.

## Vulnerable pattern
Spot `getReserves` pricing; Chainlink answers used without staleness or deviation checks; TWAP windows shorter than the capital needed to move them.

## Safe pattern
Medianised or time-weighted prices over meaningful windows, staleness and sanity bounds on feeds, and liquidity-aware caps on how much a price can affect per block.

## Review checks
- Identify every price read and follow it to its source.
- Ask: what capital moves this price 10%? For how long must it hold?
- Check stale-price handling: what happens if the feed stops updating?

## My examples
<!-- Add one sanitised example from this week's own review before committing.
     No unpublished findings, no target secrets. -->
