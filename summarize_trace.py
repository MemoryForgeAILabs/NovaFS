import json
from collections import Counter

def summarize_trace(file_path="glyph_trace.json"):
    try:
        with open(file_path, "r") as f:
            trace = json.load(f)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return

    total_branches = len(trace)
    cycles = set()
    max_depth = 0
    status_counter = Counter()

    for entry in trace:
        cycles.add(entry["cycle"])
        status_counter[entry["status"]] += 1
        max_depth = max(max_depth, entry["depth"])

    print("\n📊 NovaFS Trace Summary")
    print("-" * 30)
    print(f"Total cycles       : {len(cycles)}")
    print(f"Total branches     : {total_branches}")
    print(f"Alive branches     : {status_counter['alive']}")
    print(f"Decayed branches   : {status_counter['decayed']}")
    print(f"Max depth reached  : {max_depth}")
    print("-" * 30)

if __name__ == "__main__":
    summarize_trace("glyph_trace.json")
