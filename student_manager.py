"""
Student Allocation Manager Module
Handles student allocations, availability verification, and record retrieval.
"""

from storage import load_data, save_data
from room_manager import is_room_available, decrement_room_count


def allocate_student(student_name, room_type):
    """
    Attempts to allocate a student to a room type.
    Returns (bool success, str message)
    """
    if not is_room_available(room_type):
        return False, f"Sorry, {room_type}s are currently unavailable."

    if decrement_room_count(room_type):
        data = load_data()
        record = {"name": student_name, "room_type": room_type}
        data["students"].append(record)
        save_data(data["rooms"], data["initial_rooms"], data["students"])
        return True, f"{student_name} has been allocated a {room_type}."
    
    return False, "Allocation failed due to system error."


def get_allocations():
    """Returns list of allocated student records."""
    data = load_data()
    return data.get("students", [])


def display_allocations():
    """Prints formatted list of all allocated students."""
    students = get_allocations()
    print("\n===================================")
    print("       STUDENT ALLOCATIONS")
    print("===================================")
    if not students:
        print("No student allocations found.")
        return

    for idx, student in enumerate(students, 1):
        print(f"{idx}. {student['name']} -> {student['room_type']}")