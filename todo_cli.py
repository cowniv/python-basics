"""Command-line to-do list saved to a JSON file - practicing file I/O."""
import json
import os

FILE = "todos.json"


def load():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save(todos):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, indent=2)
