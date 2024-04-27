# Implement test cases for Cuckoo Hashing

import unittest
from cuckoo_hashing import CuckooHashTable

class TestCuckooHashTable(unittest.TestCase):
    def test_insert_and_lookup(self):
        hash_table = CuckooHashTable(size=10)
        hash_table.insert("key1", "value1")
        hash_table.insert("key2", "value2")
        hash_table.insert("key3", "value3")

        self.assertEqual(hash_table.lookup("key1"), "value1")
        self.assertEqual(hash_table.lookup("key2"), "value2")
        self.assertEqual(hash_table.lookup("key3"), "value3")

    def test_delete(self):
        hash_table = CuckooHashTable(size=10)
        hash_table.insert("key1", "value1")
        hash_table.insert("key2", "value2")
        hash_table.insert("key3", "value3")

        self.assertTrue(hash_table.delete("key1"))
        self.assertIsNone(hash_table.lookup("key1"))

    def test_collision(self):
        hash_table = CuckooHashTable(size=2)
        hash_table.insert("key1", "value1")
        hash_table.insert("key2", "value2")
        hash_table.insert("key3", "value3")

        self.assertEqual(hash_table.lookup("key1"), "value1")
        self.assertEqual(hash_table.lookup("key2"), "value2")
        self.assertEqual(hash_table.lookup("key3"), "value3")

if __name__ == '__main__':
    unittest.main()


