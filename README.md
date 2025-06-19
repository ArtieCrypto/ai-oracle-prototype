# ai-oracle-prototype
Integrating off-chain AI signals with on-chain data using Pyth oracles

# AI Oracle Signal Prototype

This project demonstrates a modular integration between off-chain AI signals and on-chain smart contract logic using oracle infrastructure. It showcases a hybrid architecture for intelligent, cross-domain asset allocation strategies.

## 🔍 Overview

- **AI signal generation** for macro + crypto asset allocation  
- **On-chain smart contract** for receiving and routing payloads  
- **Oracle interoperability** using mock VAA and real-time price feeds  
- **Professional packaging** for GitHub presentation

## 🧠 AI Signal Engine

Located in the [`ai/`](./ai) folder:

- Python script that simulates asset allocations, crypto subweights, and DeFi yield strategies
- Outputs structured JSON with rationale and confidence metrics
- Built for compatibility with cross-chain messaging systems like Wormhole or LayerZero

## ⚙️ Smart Contract Logic

Located in the [`contracts/`](./contracts) folder:

- `AIOracleIntegration.sol`: Receives encoded signal payloads and external oracle data
- Designed for gas efficiency, modularity, and simulation on Sepolia with Pyth feeds

## 🧪 Testing & Simulation

- [`test/mockVaaTest.js`](./test/mockVaaTest.js): Basic test harness for encoded signal payloads
- Includes example compressed VAA interactions and argument handling for constructor inputs

## 🧱 Architecture

![Architecture Diagram](./docs/architecture-diagram.png)

The prototype reflects a user-centric financial design with an emphasis on:
- Accessibility of DeFi intelligence
- Low-code interfacing between AI and contracts
- Yield strategy transparency

## 📄 Supporting Docs

- [`dev-notes.md`](./docs/dev-notes.md): Setup, tooling, and integration rationale
- [`frontend-mock.txt`](./docs/frontend-mock
