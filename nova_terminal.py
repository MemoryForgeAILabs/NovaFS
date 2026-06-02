from routing_engine import resolve_symbolic_cue, log_route

def main():
    print("╔══════════════════════════════════════╗")
    print("║     🔁 NOVAFS - SYMBOLIC TERMINAL     ║")
    print("╚══════════════════════════════════════╝")
    print()

    cue_list = [
        '🔺', 'alpha', 'priority',
        '🔵', 'beta', 'support',
        '🟢', 'gamma', 'growth',
        '🔶', 'delta', 'innovation'
    ]

    print(f"🧠 Stored Symbols: {cue_list}")
    print()

    while True:
        cue = input("🔍 Enter a symbolic cue (e.g. 🔺, alpha, vision), or type 'exit': ")
        if cue.strip().lower() == 'exit':
            break

        result = resolve_symbolic_cue(cue.strip())

        if result:
            print(f"\n✅ FILE FOUND: {result['file']}")
            print(f"🔗 ROUTE USED: {result['path']}")
            log_route(cue, result['file'], result['path'])
        else:
            print("\n⚠️ No match found. Try a different cue.")

        input("\n🔄 Press Enter to continue...\n")

if __name__ == "__main__":
    main()
