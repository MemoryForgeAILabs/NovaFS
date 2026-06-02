import random
import time
import os
import json

def simulate_branching(symbols, cycles=11, max_branches=4):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("🌱 NOVAFS - SYMBOLIC ROOT SIMULATION 🌱\n")
    branches = [{'path': [s], 'depth': 1} for s in symbols]
    glyph_trace = []

    for cycle in range(cycles):
        new_branches = []
        print(f"🌿 Cycle {cycle + 1}:\n")
        for b in branches:
            entry = {
                "cycle": cycle + 1,
                "depth": b["depth"],
                "path": b["path"],
                "timestamp": time.time()
            }
            if random.random() < 0.25:  # decay chance
                print("  " * b['depth'] + f"🟥 {' → '.join(b['path'])} (decayed)")
                entry["status"] = "decayed"
                glyph_trace.append(entry)
                continue

            print("  " * b['depth'] + f"🟩 {' → '.join(b['path'])}")
            entry["status"] = "alive"
            glyph_trace.append(entry)

            for _ in range(random.randint(1, max_branches)):
                new_symbol = random.choice(symbols)
                new_branches.append({'path': b['path'] + [new_symbol], 'depth': b['depth'] + 1})

        branches = new_branches
        time.sleep(1.2)
        print("\n" + "=" * 42 + "\n")

    # Save log
    with open("glyph_trace.json", "w") as f:
        json.dump(glyph_trace, f, indent=2)

    print("📄 Trace log saved as 'glyph_trace.json'")
    input("⏸️  Press Enter to review and exit...")

if __name__ == "__main__":
    simulate_branching(["alpha", "gamma", "delta"])
