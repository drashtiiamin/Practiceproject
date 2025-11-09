import numpy as np
def calculate_mean(data):
    """Calculate the mean of a list of numbers."""
    if not data:
        return 0
    return np.mean(data)
