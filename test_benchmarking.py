import unittest
import random  # Add this import statement
from benchmarking import measure_execution_time, measure_memory_usage, example_function

class TestBenchmarking(unittest.TestCase):
    def test_execution_time(self):
        # Generate random data for benchmarking
        data_size = 10000
        random_data = [random.randint(0, 1000) for _ in range(data_size)]

        # Measure execution time
        execution_time = measure_execution_time(example_function, random_data)
        self.assertIsInstance(execution_time, float)

    def test_memory_usage(self):
        # Generate random data for benchmarking
        data_size = 10000
        random_data = [random.randint(0, 1000) for _ in range(data_size)]

        # Measure memory usage
        memory_usage = measure_memory_usage(example_function, random_data)
        if memory_usage is not None:
            self.assertIsInstance(memory_usage, int)

if __name__ == '__main__':
    unittest.main()