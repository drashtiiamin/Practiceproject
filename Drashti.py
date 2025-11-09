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
def calculate_standard_deviation(data):
    """Calculate the standard deviation of a list of numbers."""
    if not data:
        return 0
    return np.std(data)     
def calculate_variance(data):
    """Calculate the variance of a list of numbers."""
    if not data:
        return 0
    return np.var(data)
def calculate_range(data):
    """Calculate the range of a list of numbers."""
    if not data:
        return 0
    return np.max(data) - np.min(data)
def calculate_percentile(data, percentile):
    """Calculate the given percentile of a list of numbers."""
    if not data:
        return 0
    return np.percentile(data, percentile)
def calculate_correlation(data1, data2):
    """Calculate the correlation coefficient between two lists of numbers."""
    if not data1 or not data2 or len(data1) != len(data2):
        return 0
    return np.corrcoef(data1, data2)[0, 1]
def calculate_regression_slope(data1, data2):
    """Calculate the slope of the linear regression line between two lists of numbers."""
    if not data1 or not data2 or len(data1) != len(data2):
        return 0
    A = np.vstack([data1, np.ones(len(data1))]).T
    slope, _ = np.linalg.lstsq(A, data2, rcond=None)[0]
    return slope
def calculate_regression_intercept(data1, data2):
    """Calculate the intercept of the linear regression line between two lists of numbers."""
    if not data1 or not data2 or len(data1) != len(data2):
        return 0
    A = np.vstack([data1, np.ones(len(data1))]).T
    _, intercept = np.linalg.lstsq(A, data2, rcond=None)[0]
    return intercept    
