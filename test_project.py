"""
Unit Tests for Hostel Room Allocator
Executing test suite with built-in unittest framework.
"""

import unittest
import os
from pathlib import Path
import storage
import room_manager
import student_manager
import validation


class TestHostelRoomAllocator(unittest.TestCase):

    def setUp(self):
        """Use custom test JSON file to avoid overwriting production data."""
        self.test_file = Path("test_hostel_data.json")
        storage.DATA_FILE = self.test_file
        if self.test_file.exists():
            os.remove(self.test_file)

    def tearDown(self):
        """Clean up test JSON file post execution."""
        if self.test_file.exists():
            os.remove(self.test_file)

    def test_room_inventory_and_allocation(self):
        """Test successful allocation and decrement of inventory."""
        inv = {"3-bedded room": 2, "2-bedded room": 1}
        room_manager.initialize_inventory(inv)

        success, msg = student_manager.allocate_student("Aman", "3-bedded room")
        self.assertTrue(success)
        self.assertIn("Aman has been allocated", msg)

        curr_inv = room_manager.get_inventory()
        self.assertEqual(curr_inv["3-bedded room"], 1)

    def test_unavailable_room_allocation(self):
        """Test allocation attempt when room type count is zero."""
        inv = {"3-bedded room": 0}
        room_manager.initialize_inventory(inv)

        success, msg = student_manager.allocate_student("Rahul", "3-bedded room")
        self.assertFalse(success)
        self.assertIn("currently unavailable", msg)

    def test_invalid_room_type(self):
        """Test checking availability of non-existent room type."""
        inv = {"3-bedded room": 2}
        room_manager.initialize_inventory(inv)

        self.assertFalse(room_manager.is_room_available("10-bedded room"))

    def test_json_save_load(self):
        """Test JSON persistence data integrity."""
        rooms = {"3-bedded room": 5}
        initial = {"3-bedded room": 5}
        students = [{"name": "Priya", "room_type": "3-bedded room"}]

        storage.save_data(rooms, initial, students)
        loaded = storage.load_data()

        self.assertEqual(loaded["rooms"], rooms)
        self.assertEqual(loaded["initial_rooms"], initial)
        self.assertEqual(loaded["students"], students)


if __name__ == "__main__":
    unittest.main()