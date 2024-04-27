# Implement test cases for Collision Resistance Analysis

import unittest
from collision_analysis import calculate_collision_rate, md5_hash, sha256_hash

class TestCollisionAnalysis(unittest.TestCase):
    def test_collision_rate_md5(self):
        data = ["apple", "banana", "orange", "grape", "kiwi", "pineapple"]
        collision_rate = calculate_collision_rate(md5_hash, data)
        self.assertLessEqual(collision_rate, 0.5)  # Assuming less than 50% collision rate

    def test_collision_rate_sha256(self):
        data = ["apple", "banana", "orange", "grape", "kiwi", "pineapple"]
        collision_rate = calculate_collision_rate(sha256_hash, data)
        self.assertLessEqual(collision_rate, 0.5)  # Assuming less than 50% collision rate

if __name__ == '__main__':
    unittest.main()



