from operator.LIFE_PHI import detect_symbolic_collapse
import numpy as np

# Synthetic signal: normal distribution
signal = np.random.normal(loc=10, scale=2, size=100)

collapse, entropy = detect_symbolic_collapse(signal)

print(f"Collapse Detected: {collapse}")
print(f"Entropy Score: {entropy:.4f}")
