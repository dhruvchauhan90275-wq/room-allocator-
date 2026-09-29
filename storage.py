"""
Data Persistence Module using JSON and pathlib.
"""

import json
from pathlib import Path

DATA_FILE = Path("hostel_data.json")


def data_exists():
    """Checks if persistence file exists."""
    return DATA_FILE.exists()


def load_data():
    """
    Loads JSON data safely.
    Returns standardized dictionary schema.
    """
    default_structure = {
        "rooms": {},
        "initial_rooms": {},
        "students": []
    }

    if not DATA_FILE.exists():
        return default_structure

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, dict):
                return default_structure
            return {
                "rooms": data.get("rooms", {}),
                "initial_rooms": data.get("initial_rooms", {}),
                "students": data.get("students", [])
            }
    except (json.JSONDecodeError, OSError):
        print("\n[WARNING] Corrupted or invalid JSON data file encountered. Resetting state.")
        return default_structure


def save_data(rooms, initial_rooms, students):
    """Saves rooms, initial_rooms, and students data safely to JSON."""
    data = {
        "rooms": rooms,
        "initial_rooms": initial_rooms,
        "students": students
    }
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        return True
    except OSError as e:
        print(f"\n[ERROR] Failed to save data: {e}")
        return False