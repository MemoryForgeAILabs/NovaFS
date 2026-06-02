# NovaFS Symbolic Routing Demo

NovaFS is a proof-of-concept symbolic routing engine. It demonstrates how simple symbolic cues can drive intelligent retrieval and memory systems.

This lean prototype is designed to be easy to understand and extend.

---

## 🚀 Overview

NovaFS lets you:

✅ Define symbolic cues in `cue_map.json`  
✅ Map those cues to files in `symbol_map.json`  
✅ Route cues to file paths via a simple command-line interface  
✅ Log every routing event for transparent traceability

This project can serve as a foundation for more advanced systems in AI memory, search, and knowledge management.

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
