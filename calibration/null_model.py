import numpy as np
from operator.LIFE_PHI import detect_symbolic_collapse

def generate_noise_signal(size=365, noise_level=1.0):
    """
    Generates a synthetic noise signal with adjustable randomness.
    """
    return np.random.normal(loc=10, scale=noise_level, size=size)

def run_null_trials(trials=10, threshold=0.85):
    """
    Runs multiple null trials and records collapse detection results.
    """
    results = []
    for _ in range(trials):
        signal = generate_noise_signal()
        collapse, entropy = detect_symbolic_collapse(signal, threshold)
        results.append((collapse, entropy))
    return results
