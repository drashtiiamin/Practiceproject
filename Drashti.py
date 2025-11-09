import numpy as np
def calculate_mean(data):
    """Calculate the mean of a list of numbers."""
    if not data:
        return 0
    return np.mean(data)
def calculate_median(data):
    """Calculate the median of a list of numbers."""
    if not data:
        return 0
    return np.median(data)
def calculate_mode(data):
    """Calculate the mode of a list of numbers."""
    if not data:
        return None
    values, counts = np.unique(data, return_counts=True)
    max_count_index = np.argmax(counts)
    return values[max_count_index]