import json
import os
from datetime import datetime

ROUTE_LOG_PATH = "route_log.json"

def load_route_log():
    if not os.path.exists(ROUTE_LOG_PATH):
        print("❌ No route log found.")
        return []

    try:
        with open(ROUTE_LOG_PATH, 'r', encoding='utf-8') as f:
            data = f.read().strip()
            if not data:
                print("⚠️ Route log is empty.")
                return []
            return json.loads(data)
    except json.JSONDecodeError:
        print("⚠️ Route log is corrupted or not valid JSON.")
        return []

def display_routes(routes):
    if not routes:
        return

    print("\n📖 ROUTE HISTORY:\n")
    for entry in routes:
        cue = entry.get("cue", "❓")
        file = entry.get("file", "❓")
        path = entry.get("path", "❓")
        time = entry.get("timestamp", "❓")
        print(f"🧠 Cue: {cue}\n📄 File: {file}\n📁 Path: {path}\n🕒 Time: {time}\n{'-'*40}")

def main():
    print("╔════════════════════════════════════╗")
    print("║     📊 NOVAFS ROUTE LOG VIEWER     ║")
    print("╚════════════════════════════════════╝")
    routes = load_route_log()
    display_routes(routes)

if __name__ == "__main__":
    main()
