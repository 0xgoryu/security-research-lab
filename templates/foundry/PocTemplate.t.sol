// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "forge-std/Test.sol";

/// @notice Minimal fork-PoC skeleton.
/// Run: forge test --fork-url $RPC --fork-block-number <BLOCK> -vvv
/// Rules: fork or local only, own accounts only, run the proof twice.
contract PocTemplateTest is Test {
    address internal attacker = makeAddr("attacker");
    address internal victim = makeAddr("victim");

    function setUp() public {
        // vm.createSelectFork("mainnet", BLOCK);
        // Label the in-scope target and deal test balances here.
    }

    function test_Poc() public {
        // 1. Record the state before (balances / storage).
        // 2. Execute the suspect path as `attacker`.
        // 3. Assert the concrete impact, not just that a call succeeded.
        // 4. Add a control run showing the honest path does NOT give
        //    the same result.
    }
}
