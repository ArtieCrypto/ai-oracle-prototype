# ai_signal_generator.py

import random
import time
import json

def generate_macro_allocation():
    # Simulate macro-level asset allocation based on mocked market indicators
    equity_weight = round(random.uniform(0.4, 0.6), 2)
    cash_weight = round(random.uniform(0.2, 0.4), 2)
    crypto_weight = round(1 - equity_weight - cash_weight, 2)
    return {
        "equities": equity_weight,
        "cash": cash_weight,
        "crypto": max(0.0, crypto_weight)
    }

def generate_crypto_allocation():
    crypto_weights = {
        "BTC": round(random.uniform(0.2, 0.5), 2),
        "ETH": round(random.uniform(0.3, 0.5), 2),
        "SOL": round(random.uniform(0.0, 0.2), 2)
    }
    total = sum(crypto_weights.values())
    for k in crypto_weights:
        crypto_weights[k] = round(crypto_weights[k] / total, 2)

    yield_opportunity = {
        "strategy": "ETH-stETH LP on Curve",
        "expectedAPR": f"{round(random.uniform(3.5, 5.5), 2)}%",
        "platform": "Yearn"
    }

    return {
        "cryptoAllocation": crypto_weights,
        "YieldFarming": yield_opportunity,
        "confidence": round(random.uniform(0.7, 0.95), 2),
        "commentary": "Elevated ETH staking flows and stable yields from stETH pools"
    }

def generate_full_signal():
    signal = {
        "timestamp": int(time.time()),
        "macroAllocation": generate_macro_allocation(),
        "cryptoStrategy": generate_crypto_allocation()
    }
    return signal

if __name__ == "__main__":
    full_signal = generate_full_signal()

    # Save to JSON file for download
    with open("signal_output.json", "w") as outfile:
        json.dump(full_signal, outfile, indent=2)

    print("✅ Signal saved to signal_output.json")
    print(json.dumps(full_signal, indent=2))
