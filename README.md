
HOSTEL ROOM ALLOCATOR - COMPLETE PROJECT BUNDLE

--------------------------------------------------------------------------------
SECTION 1: REPOSITORY DESCRIPTION
--------------------------------------------------------------------------------

Hostel Room Allocator is a modular Python CLI application created for college hostel administration to automate room tracking and student room assignments[cite: 3]. Designed with strict adherence to clean software architecture, it manages room inventory as discrete units, handles student preferences, validates user inputs to prevent runtime errors, and persists data using JSON storage[cite: 3, 8, 9, 11]. Built entirely with the Python Standard Library (`json`, `pathlib`, `unittest`)[cite: 3].


--------------------------------------------------------------------------------
SECTION 2: README.md
--------------------------------------------------------------------------------

# Hostel Room Allocator

A modular Python-based command-line application designed for college hostel administration to automate room inventory management and student room allocations[cite: 3]. It tracks available room units across multiple categories, processes student allocation requests with input validation, maintains accurate capacity records, and persists system state safely using JSON storage[cite: 3, 8, 9].

---

## 📌 Features

* **Room Inventory Setup**: Configure initial available unit counts across 5 distinct accommodation types.
* **Real-time Student Allocation**: Process student allocations with automatic live availability checks and immediate inventory updates[cite: 3, 10, 11].
* **Robust Input Validation**: Prevents CLI crashes when handling non-numeric inputs, negative values, out-of-range menu options, or blank text fields[cite: 3, 9].
* **JSON State Persistence**: Preserves inventory counts and student allocation records across program restarts using `hostel_data.json`[cite: 3, 8].
* **Analytical Reporting**: Generates summary statistics detailing initial room units, total allocations, and remaining capacities broken down by category[cite: 3, 7].
* **Automated Unit Testing**: Includes a full suite of unit tests written with Python's built-in `unittest` module[cite: 3, 6].

---

## 🛠️ Technologies & Tools Used

* **Language**: Python 3 (3.8+)[cite: 3]
* **Built-in Standard Modules**:
  * `json` — For JSON data serialization and file persistence[cite: 3, 8]
  * `pathlib` — For cross-platform file path management[cite: 3, 8]
  * `unittest` — For automated regression testing[cite: 3, 6]
  * `os` — For temporary test file cleanup
* **Development & Tools**: Git, GitHub, VS Code[cite: 3]

---

## 📋 Prerequisites

* **Python 3.8 or higher** installed on your machine[cite: 3].
* No external third-party dependencies or `pip install` commands required — the project relies exclusively on the Python Standard Library[cite: 3, 4].

---

## 🚀 Steps to Install and Run

### 1. Installation
Clone the repository to your local machine:
```bash
git clone [https://github.com/dhruvchauhan90275-wq/room-allocator-.git](https://github.com/dhruvchauhan90275-wq/room-allocator-.git)
cd room-allocator
2. ExecutionRun the main program script:Bashpython main.py
(On Linux/macOS, use python3 main.py if required)🧪 Instructions for TestingTo run the automated unit test suite using Python's built-in test runner:Bashpython -m unittest test_project.py

📊 Sample Test Data
Initial Inventory Setup
3-bedded room: 2 units
  4-bedded room: 2 units
 Bunk bed room: 1 unit
 2-bedded room: 1 unit
 4-bedded flat bed room: 1 unit
 Sample AllocationsStudent:
 Aman | Choice:
 2-bedded room -> Status: Allocated[cite:
 3, 5]Student: Rohan | Choice: 3-bedded room -> Status: Allocated
  Student: Priya | Choice:
 3-bedded room -> Status: Allocated
  Student: Rahul | Choice: 2-bedded room -> Status: Rejected (Unavailable)[cite: 6]
Sample Storage Data (hostel_data.json)JSON{
    "rooms": {
        "3-bedded room": 0,
        "4-bedded room": 2,
        "Bunk bed room": 1,
        "2-bedded room": 0,
        "4-bedded flat bed room": 1
    },
    "initial_rooms": {
        "3-bedded room": 2,
        "4-bedded room": 2,
        "Bunk bed room": 1,
        "2-bedded room": 1,
        "4-bedded flat bed room": 1
    },
    "students": [
        {"name": "Aman", "room_type": "2-bedded room"},
        {"name": "Rohan", "room_type": "3-bedded room"},
        {"name": "Priya", "room_type": "3-bedded room"}
    ]
}
📂 Project StructurePlaintextroom-allocator/
├── main.py                # Command-line menu driver and execution loop
├── room_manager.py        # Room inventory business logic and capacity checks
├── student_manager.py     # Student room allocation processing
├── validation.py         # Input validation routines to prevent CLI crashes
├── storage.py            # JSON file read/write data persistence operations
├── reports.py            # Allocation breakdown and analytics report generator
├── test_project.py       # Automated unit testing suite
├── hostel_data.json      # Saved application data state
├── requirements.txt      # Dependency specification (Standard Library notice)
├── README.md             # Project documentation
├── statement.md          # Academic problem statement and scope
└── .gitignore            # Git ignore configuration
📝 Important NotesRoom Count Semantics:
Entering 5 for 3-bedded rooms indicates 5 available room units, not 15 individual beds. Allocating a room decrements the unit count by
 1.   Safety Confirmation: Re-initializing the room inventory while student records exist will request confirmation to prevent accidental loss of student allocations.
🔮 Future Enhancements
Student room cancellation and reallocation workflows.Administrator password authentication before altering room availability.Student record search and room lookup.PDF/CSV export functionality for summary reports


