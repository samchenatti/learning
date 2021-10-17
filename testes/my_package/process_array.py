import numpy as np


def double_and_concat_array(original_array: np.array) -> np.array:
    """
    Doubles and concats the array with the original data

    Args:
        original_array: the original NumPy array

    Returns:
        The new array
    """
    doubled_array = 2 * original_array

    return np.concatenate(
        [
            original_array,
            doubled_array
        ]
    )
