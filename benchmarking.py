import time
import random
import platform

# Check if running on Windows
is_windows = platform.system() == 'Windows'

def measure_execution_time(func, *args, **kwargs):
    """
    Measure the execution time of a function.

    Parameters:
        func (callable): The function to measure.
        args: Positional arguments to pass to the function.
        kwargs: Keyword arguments to pass to the function.

    Returns:
        float: Execution time in seconds.
    """
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    return end_time - start_time

def measure_memory_usage(func, *args, **kwargs):
    """
    Measure the peak memory usage of a function.

    Parameters:
        func (callable): The function to measure.
        args: Positional arguments to pass to the function.
        kwargs: Keyword arguments to pass to the function.

    Returns:
        int: Peak memory usage in bytes.
    """
    if is_windows:
        # Memory usage measurement is not available on Windows
        print("Memory usage measurement is not available on Windows.")
        return None
    else:
        import resource
        start_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        func(*args, **kwargs)
        end_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        return end_memory - start_memory

def example_function(data):
    """
    Example function to benchmark.
    """
    sorted_data = sorted(data)
    return sorted_data

# Example usage:
if __name__ == "__main__":
    # Generate random data for benchmarking
    data_size = 10000
    random_data = [random.randint(0, 1000) for _ in range(data_size)]

    # Measure execution time
    execution_time = measure_execution_time(example_function, random_data)
    print("Execution time:", execution_time, "seconds")

    # Measure memory usage
    memory_usage = measure_memory_usage(example_function, random_data)
    if memory_usage is not None:
        print("Memory usage:", memory_usage, "bytes")

