"""
Hostel Room Allocator - CLI Interface
Main entry point controlling the command-line menu and application workflow.
"""

from room_manager import (
    ROOM_TYPES,
    initialize_inventory,
    get_inventory,
    display_inventory
)
from student_manager import allocate_student, get_allocations, display_allocations
from validation import (
    get_non_negative_integer,
    get_non_empty_string,
    get_menu_choice,
    get_yes_no
)
from storage import load_data, save_data, data_exists
from reports import generate_summary_report


def setup_room_inventory():
    """Handles setting up room inventory with user input and reset warnings."""
    current_data = load_data()
    if current_data["students"]:
        print("\n[WARNING] Setting up a new inventory will reset current student allocations!")
        confirm = get_yes_no("Are you sure you want to re-initialize inventory? (y/n): ")
        if not confirm:
            print("Room setup cancelled.")
            return

    print("\n--- Set Up Room Inventory ---")
    print("Enter the available number of room units for each category:\n")
    
    inventory = {}
    for key, room_name in ROOM_TYPES.items():
        count = get_non_negative_integer(f"Enter number of {room_name}s: ")
        inventory[room_name] = count

    initialize_inventory(inventory)
    save_data(get_inventory(), get_inventory(), [])
    print("\n[SUCCESS] Room inventory initialized successfully!")


def process_allocation():
    """Processes allocation for a student based on input and availability."""
    current_data = load_data()
    rooms = current_data["rooms"]

    if not rooms:
        print("\n[ERROR] Inventory not configured. Please set up room availability first.")
        return

    print("\n--- Student Allocation ---")
    student_name = get_non_empty_string("Enter student name: ")

    print("\nAvailable Room Types:")
    for key, name in ROOM_TYPES.items():
        avail = rooms.get(name, 0)
        print(f"  {key}. {name} (Available: {avail})")

    choice = get_menu_choice("Select room choice (1-5): ", 1, 5)
    preferred_type = ROOM_TYPES[choice]

    success, message = allocate_student(student_name, preferred_type)
    if success:
        print(f"\n[SUCCESS] {message}")
    else:
        print(f"\n[FAILURE] {message}")


def main_menu():
    """Main CLI Menu loop."""
    # Ensure file exists or initialize clean state
    if not data_exists():
        save_data({}, {}, [])

    while True:
        print("\n" + "=" * 40)
        print("       HOSTEL ROOM ALLOCATOR")
        print("=" * 40)
        print("1. Set up room availability")
        print("2. Allocate rooms to students")
        print("3. View room availability")
        print("4. View student allocations")
        print("5. View summary report")
        print("6. Exit")
        print("=" * 40)

        choice = get_menu_choice("Enter your choice (1-6): ", 1, 6)

        if choice == 1:
            setup_room_inventory()
        elif choice == 2:
            process_allocation()
        elif choice == 3:
            display_inventory()
        elif choice == 4:
            display_allocations()
        elif choice == 5:
            generate_summary_report()
        elif choice == 6:
            print("\nThank you for using Hostel Room Allocator!")
            break


if __name__ == "__main__":
    main_menu()