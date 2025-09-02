from operator.LIFE_PHI import detect_symbolic_collapse
from models.planetary_model import simulate_orbital_alignment, generate_geomagnetic_vector
from motifs.motif_renderer import (
    plot_alignment_signal,
    plot_geomagnetic_vector,
    plot_entropy_score
)
import numpy as np

# Simulate planetary signals
alignment = simulate_orbital_alignment(days=365)
geomagnetic = generate_geomagnetic_vector(days=365)

# Combine signals
combined_signal = (alignment + geomagnetic) / 2

# Run collapse detection
collapse, entropy = detect_symbolic_collapse(combined_signal)

# Print results
print("🔮 Planetary Fusion Test")
print(f"Collapse Detected: {collapse}")
print(f"Entropy Score: {entropy:.4f}")

# Visualize
plot_alignment_signal(alignment)
plot_geomagnetic_vector(geomagnetic)
plot_entropy_score(entropy, collapse)
