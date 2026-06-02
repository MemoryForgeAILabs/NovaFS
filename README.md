# NovaFS Symbolic Routing Demo

NovaFS is a proof-of-concept symbolic routing engine. It demonstrates how simple symbolic cues can drive intelligent retrieval and memory systems.

This lean prototype is designed to be easy to understand and extend.

> **⚠️ Status: Archived (2026).** NovaFS is no longer actively developed and is published here as a public reference. The problem it explored — turning natural-language *intent* into the correct database query or data route **deterministically, without embeddings or vector search** — is now handled more flexibly by modern natural-language-to-SQL (NL→DB) query models. This repo preserves the symbolic-routing kernel and its glass-box design. See [Background & Context](#-background--context) and [Why this is archived](#-why-this-is-archived).

---

## 🚀 Overview

NovaFS lets you:

✅ Define symbolic cues in `cue_map.json`  
✅ Map those cues to files in `symbol_map.json`  
✅ Route cues to file paths via a simple command-line interface  
✅ Log every routing event for transparent traceability

This project can serve as a foundation for more advanced systems in AI memory, search, and knowledge management.

---

## 📖 Background & Context

The code in this repository is the **kernel** of a larger idea. The core
premise of NovaFS was *deterministic semantic routing*:

> Map a natural-language query to the **correct** data — the right file,
> table, or knowledge category — using fixed, inspectable rules instead of
> embeddings or vector similarity search.

The toy demo here routes symbolic cues (`alpha`, `🔺`) to files. In its more
developed form the same mechanism grew into a **semantic abstraction layer**
that could answer one plain-language question (e.g. *"check brake history"*)
across several wildly different database schemas — from free-text notes to
fully normalized tables — without the caller needing to know where the data
lived.

The design favored a few principles consistently:

- **Deterministic** — the same input always resolves to the same route, so
  behavior is reproducible.
- **Glass-box / auditable** — every routing decision is logged with the cue,
  the chosen path, and a timestamp. No black box.
- **No model in the hot path** — routing is keyword/concept matching plus a
  lightweight reinforcement-and-decay weighting of paths that succeed or fail
  over time. Fast and cheap.
- **Concept-first** — queries route to stable *concepts*, decoupling user
  intent from the volatile structure of whatever store sits underneath.

The trade-off was deliberate and, ultimately, decisive: it **traded
flexibility for predictability**. A rule-based router cannot handle ambiguous
or novel phrasing the way a learned model can.

---

## 🪦 Why this is archived

The specific job NovaFS did well — translating natural language into the
right query/route over structured data — is now done directly, and more
flexibly, by **natural-language-to-database (NL→DB / NL→SQL) query models**.
Those models close exactly the gap NovaFS's deterministic approach left open:
handling ambiguous, unseen, and conversational phrasing without hand-built
concept maps and routing tables to maintain.

Given that, the project is no longer worth actively developing. It is kept
public as a compact, readable reference for:

- the **symbolic-routing kernel** (see `routing_engine.py`),
- the **glass-box, deterministic** design stance, and
- the path **reinforcement/decay** weighting idea.

If you're solving the NL→data problem today, reach for an NL→SQL model first.
NovaFS is here to illustrate an alternative point in the design space — one
that prizes determinism and auditability — not as something to build on.

---

## ⚙️ Installation

1. **Clone this repository:**

   ```
   git clone https://github.com/MemoryForgeAILabs/NovaFS.git
   ```

2. **Navigate to the project folder:**

   ```
   cd NovaFS
   ```

3. *(Optional)* Create and activate a virtual environment:

   **Windows:**
   ```
   python -m venv .venv
   .venv\Scripts\activate
   ```

   **macOS/Linux:**
   ```
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. **Install dependencies:**

   *(Note: this project uses only standard Python libraries.)*

---

## 💻 Usage

### 1. Initialize the demo (first run only)

This creates the `symbols/` files and a fresh `symbol_map.json`:

```
python init_demo.py
```

### 2. Launch the symbolic terminal

```
python nova_terminal.py
```

You'll get an interactive prompt. Enter a symbolic cue — a word like
`alpha`, `beta`, `growth` or a glyph like `🔺`, `🔵` — and NovaFS routes
it to the associated memory file:

```
🔍 Enter a symbolic cue (e.g. 🔺, alpha, vision), or type 'exit': alpha

✅ FILE FOUND: 🔺_alpha.txt
🔗 ROUTE USED: alpha → 🔺_alpha.txt
```

Type `exit` to quit. Every routing event is logged for traceability.

### 3. Review the routing history

```
python view_trace.py          # human-readable memory trace
python route_log_viewer.py    # detailed route log
```

---

## 🗂️ File Descriptions

- `routing_engine.py`: Core logic for cue resolution and logging
- `nova_terminal.py`: Command-line interface
- `cue_map.json`: Symbolic cue definitions
- `symbol_map.json`: Mapping from symbols to file paths
- `route_log.json`: Routing event log

---

## 📄 Example `cue_map.json`

```json
{
  "alpha": {"symbol": "🔺", "weight": 1.0},
  "beta": {"symbol": "🔵", "weight": 1.0}
}
```

---

## 📄 Example `symbol_map.json`

```json
{
  "🔺": {
    "paths": {
      "🔺_alpha.txt": 1
    }
  }
}
```

---

## 🧹 Resetting Logs

To clear all routing history:

1. Open `route_log.json`
2. Replace its contents with:

```json
[]
```

---

## 🛡️ License & Disclaimer

Released under the [MIT License](LICENSE).

This project is provided for demonstration purposes only.  
No warranty is expressed or implied.

---

## 🌟 Vision

NovaFS demonstrates that even a minimal Python prototype can create a symbolic routing engine.  
It offers a framework for future development in semantic search, AI memory systems, and adaptive context management.

---
