# Implement functions to analyze collision resistance of hashing techniques

import hashlib


def calculate_collision_rate(hash_function, data):
    """
    Calculate the collision rate for a given hash function and dataset.

    Parameters:
        hash_function (callable): The hash function to be used.
        data (list): List of input data to hash.

    Returns:
        float: Collision rate (number of collisions / total number of inputs).
    """
    hashed_values = [hash_function(item) for item in data]
    unique_hashes = len(set(hashed_values))
    total_hashes = len(hashed_values)
    collision_rate = 1.0 - (unique_hashes / total_hashes)
    return collision_rate


def md5_hash(data):
    """
    Calculate MD5 hash for input data.

    Parameters:
        data: Data to be hashed.

    Returns:
        str: MD5 hash value.
    """
    return hashlib.md5(data.encode()).hexdigest()


def sha256_hash(data):
    """
    Calculate SHA-256 hash for input data.

    Parameters:
        data: Data to be hashed.

    Returns:
        str: SHA-256 hash value.
    """
    return hashlib.sha256(data.encode()).hexdigest()


# Example usage:
if __name__ == "__main__":
    data = ["apple", "banana", "orange", "grape", "kiwi", "pineapple"]

    md5_collision_rate = calculate_collision_rate(md5_hash, data)
    sha256_collision_rate = calculate_collision_rate(sha256_hash, data)

    print("Collision rate for MD5:", md5_collision_rate)
    print("Collision rate for SHA-256:", sha256_collision_rate)

