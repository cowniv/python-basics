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


def show(todos):
    if not todos:
        print("  (nothing to do!)")
    for i, t in enumerate(todos, start=1):
        mark = "x" if t["done"] else " "
        print(f"  {i}. [{mark}] {t['task']}")


def main():
    todos = load()
    menu = "\n[a]dd  [d]one  [r]emove  [l]ist  [q]uit"

    while True:
        print(menu)
        choice = input("> ").lower().strip()

        if choice == "a":
            todos.append({"task": input("Task: "), "done": False})
        elif choice in ("d", "r"):
            show(todos)
            try:
                idx = int(input("Number: ")) - 1
                if choice == "d":
                    todos[idx]["done"] = True
                else:
                    todos.pop(idx)
            except (ValueError, IndexError):
                print("Invalid number.")
        elif choice == "l":
            show(todos)
        elif choice == "q":
            break
