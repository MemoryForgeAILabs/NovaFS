# reset_logs.py
import json
import os

TRACE_FILE = "glyph_trace.json"

def reset_trace_log():
    # Create a clean log structure
    empty_log = {
        "history": []
    }

    # Overwrite existing log or create a new one
    with open(TRACE_FILE, "w", encoding="utf-8") as file:
        json.dump(empty_log, file, indent=2)
    print("✅ glyph_trace.json has been reset.\n")

if __name__ == "__main__":
    print("🧹 Resetting NovaFS trace logs...")
    reset_trace_log()
    input("🔄 Press Enter to continue...")
