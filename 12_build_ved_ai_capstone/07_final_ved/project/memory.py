import json
import os

MEMORY_FILE = "ved_memory.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}

    with open(MEMORY_FILE, "r") as file:
        try:
            return json.load(file)
        except:
            return {}

def save_memory(memory_data):
    with open(MEMORY_FILE, "w") as file:
        json.dump(memory_data, file, indent=4)

def remember(key, value):
    memory = load_memory()
    memory[key] = value
    save_memory(memory)

def recall(key):
    memory = load_memory()
    return memory.get(key, None)
