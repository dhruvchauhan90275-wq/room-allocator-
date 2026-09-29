# Hostel Room Allocator

A modular Python-based command-line application designed for college hostel administration to automate room inventory management and student room allocations[cite: 3]. It tracks available room units across multiple categories, processes student allocation requests with input validation[cite: 3, 9], maintains accurate capacity records, and persists system state safely using JSON storage[cite: 3, 8].

---

## 📌 Features

* **Room Inventory Setup**: Configure initial available unit counts across 5 distinct accommodation types[cite: 3, 5].
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
