# calculator/history.py

import json
from typing import List,Dict,Union
from pathlib import Path

HISTORY_FILE = "history.json"

def load_history() -> List[Dict[str,Union[str,float]]]:
    """Load calculation history from JSON file. Returns empty list if file doesn't exist."""
    path = Path(HISTORY_FILE)
    if not path.exists():
        return []
    try:
        with open(HISTORY_FILE,'r') as f:
            return json.load(f)
    except (json.JSONDecodeError,FileNotFoundError):
        return []

def save_history(history: List[Dict[str, Union[str, float]]]) -> None:
    """Save the current history to JSON file."""
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)

def add_to_history(operation: str, a: float, b: float, result: float) -> None:
    """Add a new calculation to the history."""
    history = load_history()
    entry = {
        "operation": operation,
        "a": a,
        "b": b,
        "result": result
    }
    history.append(entry)
    save_history(history)

def clear_history() -> None:
    """Clear all history by overwriting the file with an empty list."""
    save_history([])