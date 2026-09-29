# Project Statement: Hostel Room Allocator

## Problem Statement
Hostel administration in educational institutions frequently encounters inefficiencies when manually tracking room availability and allocating rooms to incoming students[cite: 2]. Manual record-keeping leads to over-allocation errors, lack of visibility into real-time vacancy numbers, and data loss upon administrative transitions[cite: 2]. A centralized, reliable, and lightweight software solution is needed to manage room unit inventories, handle student room requests, validate inputs, and safely persist allocation records[cite: 2].

## Project Scope
The **Hostel Room Allocator** is designed as a modular Python-based software tool[cite: 2]. The scope includes:
- Managing 5 distinct hostel room categories (3-bedded, 4-bedded, Bunk bed, 2-bedded, 4-bedded flat bed)[cite: 2].
- Treating room inputs as discrete room units rather than individual bed metrics[cite: 2].
- Processing student allocations on a first-come, first-served basis with availability checks[cite: 2].
- Persisting state using JSON file storage[cite: 2].
- Generating operational reports detailing allocation counts and remaining room capacities[cite: 2].

## Target Users
- Hostel Administrators[cite: 2]
- Chief Wardens[cite: 2]
- Campus Accommodation Officers[cite: 2]

## Objectives
1. Provide an intuitive command-line interface (CLI) for daily hostel operations[cite: 2].
2. Ensure strict input validation to prevent invalid room quantities or system crashes[cite: 2].
3. Implement modular software architecture for clear code separation and maintainability[cite: 2].
4. Deliver lightweight persistence without requiring heavy SQL database servers[cite: 2].
5. Provide automated test coverage to verify system correctness[cite: 2].

## High-Level Features
- **Inventory Setup**: Admin configures available units per room type[cite: 2].
- **Interactive Student Allocation**: Student name and room choice are validated against live inventory[cite: 2].
- **Automatic Fallback Handling**: Informative feedback when requested room types are fully occupied[cite: 2].
- **Reporting Dashboard**: Comparative breakdown of initial, allocated, and remaining room units[cite: 2].
- **State Persistence**: JSON read/write logic ensuring continuous tracking across sessions[cite: 2].

## Expected Outcome
A robust, error-tolerant Python application that simplifies hostel room management, eliminates double-booking errors, and provides clear record-keeping for college administrators[cite: 2].
