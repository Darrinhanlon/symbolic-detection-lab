import numpy as np

def detect_symbolic_collapse(signal, threshold=0.85):
    """
    Detects symbolic collapse events in a signal using LIFE–PHI logic.
    Returns a tuple: (collapse_detected, entropy_score)
    """
    if np.mean(signal) == 0:
        return False, 0.0  # Avoid division by zero

    entropy = np.std(signal) / np.mean(signal)
    collapse = entropy < threshold
    return collapse, entropy
