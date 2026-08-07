import json
import os


FILE = "history/history.json"


def save(data):

    os.makedirs("history", exist_ok=True)

    history = []

    if os.path.exists(FILE):

        with open(FILE) as f:
            history = json.load(f)

    history.append(data)

    with open(FILE, "w") as f:
        json.dump(history, f, indent=4)