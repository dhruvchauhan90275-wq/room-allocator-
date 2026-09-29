"""
Reporting Module
Generates analytical summaries and breakdown metrics.
"""

from storage import load_data


def generate_summary_report():
    """Generates and prints comprehensive allocation summary report."""
    data = load_data()
    rooms = data.get("rooms", {})
    initial_rooms = data.get("initial_rooms", {})
    students = data.get("students", [])

    print("\n===================================")
    print("      HOSTEL ALLOCATION REPORT")
    print("===================================")

    if not initial_rooms:
        print("No hostel data recorded yet.")
        return

    total_initial = sum(initial_rooms.values())
    total_current = sum(rooms.values())
    total_allocated = len(students)

    print(f"Total Initial Room Units : {total_initial}")
    print(f"Total Allocated Units    : {total_allocated}")
    print(f"Total Remaining Units    : {total_current}\n")

    print("--- Breakdown by Room Type ---")
    header = f"{'Room Type':<25} | {'Initial':<8} | {'Allocated':<9} | {'Remaining':<9}"
    print(header)
    print("-" * len(header))

    for room_type, init_cnt in initial_rooms.items():
        rem_cnt = rooms.get(room_type, 0)
        alloc_cnt = init_cnt - rem_cnt
        print(f"{room_type:<25} | {init_cnt:<8} | {alloc_cnt:<9} | {rem_cnt:<9}")

    print("===================================")