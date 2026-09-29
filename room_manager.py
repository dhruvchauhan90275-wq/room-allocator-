"""
Room Inventory Manager Module
Handles room types, initial/current counts, and inventory queries.
"""

from storage import load_data, save_data

ROOM_TYPES = {
    1: "3-bedded room",
    2: "4-bedded room",
    3: "Bunk bed room",
    4: "2-bedded room",
    5: "4-bedded flat bed room"
}


def initialize_inventory(inventory_dict):
    """Sets new inventory counts and clears allocations in storage."""
    data = load_data()
    data["rooms"] = inventory_dict.copy()
    data["initial_rooms"] = inventory_dict.copy()
    data["students"] = []
    save_data(data["rooms"], data["initial_rooms"], data["students"])


def get_inventory():
    """Returns current inventory dictionary."""
    data = load_data()
    return data.get("rooms", {})


def get_initial_inventory():
    """Returns initial inventory dictionary."""
    data = load_data()
    return data.get("initial_rooms", {})


def is_room_available(room_type):
    """Checks if at least one room unit of given type is available."""
    rooms = get_inventory()
    return rooms.get(room_type, 0) > 0


def decrement_room_count(room_type):
    """Decrements available room count by 1 unit."""
    data = load_data()
    if data["rooms"].get(room_type, 0) > 0:
        data["rooms"][room_type] -= 1
        save_data(data["rooms"], data["initial_rooms"], data["students"])
        return True
    return False


def display_inventory():
    """Prints formatted current room availability."""
    rooms = get_inventory()
    print("\n===================================")
    print("       CURRENT ROOM AVAILABILITY")
    print("===================================")
    if not rooms:
        print("No inventory setup found.")
        return

    for key, name in ROOM_TYPES.items():
        count = rooms.get(name, 0)
        print(f"{name}: {count} room unit(s) available")