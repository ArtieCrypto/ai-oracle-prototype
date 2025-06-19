# AI Signal Engine

This folder contains the off-chain AI signal generator that produces structured asset allocation recommendations for integration with on-chain smart contracts.

## 📊 Purpose

The AI engine simulates dynamic portfolio allocations across:
- **Macro asset classes**: Equities, cash, and crypto
- **Crypto sub-allocations**: BTC, ETH, SOL
- **Tactical yield strategies**: e.g., ETH-stETH Curve LP via Yearn

Each output includes a time-stamped JSON object with contextual commentary and confidence metrics.

## 🤖 How It Works

The signal generator:
- Randomizes realistic portfolio weights within bounded parameters
- Suggests viable DeFi yield strategies based on market trends
- Outputs a reproducible `signal_output.json` file
- Designed for potential integration with cross-chain message payloads

## 📁 Files

- `ai_signal_generator.py`: Python script that generates the full portfolio signal
- `signal_output.json`: Sample AI-generated output (mocked for testing)

## 🌐 Integration Context

This signal engine complements the [`AIOracleIntegration.sol`](../contracts/AIOracleIntegration.sol) smart contract and oracle routing system, forming part of a broader prototype that bridges off-chain intelligence and on-chain execution.

