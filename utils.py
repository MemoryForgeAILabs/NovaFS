import os
import json

def initialize_demo():
    os.makedirs("symbols", exist_ok=True)
    demo_files = {
        "🔺_alpha.txt": "This file represents priority tasks.",
        "🔵_beta.txt": "This file represents support functions.",
        "🟢_gamma.txt": "This file represents growth initiatives.",
        "🔶_delta.txt": "This file represents innovation paths."
    }

    for file_name, content in demo_files.items():
        with open(os.path.join("symbols", file_name), "w", encoding="utf-8") as f:
            f.write(content)

    symbol_map = {
        "🔺": {"paths": {"🔺_alpha.txt": 1}},
        "alpha": {"paths": {"🔺_alpha.txt": 1}},
        "priority": {"paths": {"🔺_alpha.txt": 1}},
        "🔵": {"paths": {"🔵_beta.txt": 1}},
        "beta": {"paths": {"🔵_beta.txt": 1}},
        "support": {"paths": {"🔵_beta.txt": 1}},
        "🟢": {"paths": {"🟢_gamma.txt": 1}},
        "gamma": {"paths": {"🟢_gamma.txt": 1}},
        "growth": {"paths": {"🟢_gamma.txt": 1}},
        "🔶": {"paths": {"🔶_delta.txt": 1}},
        "delta": {"paths": {"🔶_delta.txt": 1}},
        "innovation": {"paths": {"🔶_delta.txt": 1}}
    }

    with open("symbol_map.json", "w", encoding="utf-8") as f:
        json.dump(symbol_map, f, indent=2, ensure_ascii=False)

    if not os.path.exists("route_log.json"):
        with open("route_log.json", "w", encoding="utf-8") as f:
            f.write("[]")

def load_symbol_db():
    with open("symbol_map.json", "r", encoding="utf-8") as f:
        return json.load(f)
