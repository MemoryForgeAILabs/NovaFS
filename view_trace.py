import json
import os
from datetime import datetime

TRACE_FILE = "glyph_trace.json"
OUTPUT_FILE = "view_trace_output.txt"

def load_trace():
    if not os.path.exists(TRACE_FILE):
        print("No glyph trace found.")
        return []

    with open(TRACE_FILE, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            return data.get("history", [])
        except json.JSONDecodeError:
            print("Error reading glyph_trace.json.")
            return []

def format_entry(entry):
    timestamp = datetime.fromisoformat(entry["timestamp"]).strftime("%Y-%m-%d %H:%M:%S")
    return (
        f"🧠 Cue: {entry['cue']}\n"
        f"📄 File: {entry['file']}\n"
        f"🧭 Path: {entry['path']}\n"
        f"🕒 Time: {timestamp}\n"
        f"{'-'*40}\n"
    )

def display_trace(trace):
    print("╔════════════════════════════════════════════╗")
    print("║         🧠 NOVAFS - MEMORY TRACE LOG        ║")
    print("╚════════════════════════════════════════════╝\n")

    output = []
    for entry in trace:
        formatted = format_entry(entry)
        print(formatted, end='')
        output.append(formatted)

    # Save to file
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.writelines(output)

    print(f"\n📁 Output saved to: {OUTPUT_FILE}")

if __name__ == "__main__":
    trace = load_trace()
    if trace:
        display_trace(trace)
    input("\n🔄 Press Enter to continue...")
