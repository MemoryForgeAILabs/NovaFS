import json
import os
from datetime import datetime

# Load maps from JSON files
def load_maps():
    with open("cue_map.json", "r", encoding="utf-8") as f:
        cue_map = json.load(f)
    with open("symbol_map.json", "r", encoding="utf-8") as f:
        symbol_map = json.load(f)
    return cue_map, symbol_map

# Resolve a symbolic cue to a file and route
def resolve_symbolic_cue(cue):
    cue_map, symbol_map = load_maps()

    if cue in cue_map:
        target = cue_map[cue]
        if isinstance(target, dict):
            target = target.get("symbol", None)
        if target and target in symbol_map:
            return {
                "cue": cue,
                "file": symbol_map[target],
                "path": f"{cue} → {symbol_map[target]}"
            }

    if cue in symbol_map:
        return {
            "cue": cue,
            "file": symbol_map[cue],
            "path": f"{cue} → {symbol_map[cue]}"
        }

    return None

# Safe logging with auto-repair for invalid JSON
def log_route(cue, file, path):
    log_file = "glyph_trace.json"

    try:
        with open(log_file, "r", encoding="utf-8") as f:
            log = json.load(f)
        if not isinstance(log, dict) or "history" not in log:
            raise ValueError("Invalid format")
    except (FileNotFoundError, json.JSONDecodeError, ValueError):
        log = {"history": []}

    log_entry = {
        "cue": cue,
        "file": file,
        "path": path,
        "timestamp": datetime.now().isoformat()
    }

    log["history"].append(log_entry)

    with open(log_file, "w", encoding="utf-8") as f:
        json.dump(log, f, ensure_ascii=False, indent=2)
