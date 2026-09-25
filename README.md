# CURT Inventory Assistant

A small assistant for querying CURT's parts inventory, built for the CURT GEN-AI recruitment technical task.

## Status

This submission includes:
- ✅ SQLite inventory database, seeded with 12 parts
- ✅ Data access layer (`app/database/repository.py`)
- ✅ Phase 1: rule-based assistant (`app/phase1/assistant.py`) supporting:
  - "How many [item] do we have?"
  - "Where is the [item]?"
  - "List all items in [category]."
- ✅ CLI to interact with Phase 1 (`app/phase1/cli.py`)

Not completed due to time constraints as a Gen-AI beginner:
- Phase 2 (LLM-powered backend with function calling)
- Streamlit frontend
- Automated tests

## Setup

1. Create and activate a virtual environment:

python -m venv .venv
.venv\Scripts\Activate.ps1

2. Install dependencies (none required yet — Phase 1 uses only the Python standard library).
3. Set up the database:

python -m app.database.schema
python -m app.database.seed

4. Run the assistant:

python -m app.phase1.cli


## Architecture

User → CLI → Phase 1 assistant (keyword/regex parsing) → Data access layer → SQLite


The assistant never writes raw SQL directly — all database access goes through `app/database/repository.py` (`get_part`, `get_by_category`, `update_quantity`, `get_all_parts`).

## Edge case handling

- Item names are matched case-insensitively and with partial matching (e.g. "brake pad" matches "Brake Pads"), so minor misspellings/partial names still work.
- Questions missing an item name (e.g. "how many do we have?") are detected and the assistant asks for clarification instead of erroring.
- Unrecognized questions return a helpful message listing supported question formats.

## Reflection

Given the time available, I prioritized building a genuinely working, well-understood Phase 1 over a partially-built Phase 2. The database and data-access layer were built first so both phases could eventually share them. With more time, I would add Phase 2 with Gemini function calling, a Streamlit UI, and automated tests for the regex-based query parsing.