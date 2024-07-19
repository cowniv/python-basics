"""Command-line to-do list saved to a JSON file - practicing file I/O."""
import json
import os

FILE = "todos.json"


def load():
    if not os.path.exists(FILE):
        return []
