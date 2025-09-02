import matplotlib.pyplot as plt

def plot_alignment_signal(signal, title="Orbital Alignment Signal"):
    plt.figure(figsize=(10, 4))
    plt.plot(signal, color='blue', linewidth=2)
    plt.title(title)
    plt.xlabel("Days")
    plt.ylabel("Alignment Value")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_geomagnetic_vector(vector, title="Geomagnetic Vector"):
    plt.figure(figsize=(10, 4))
    plt.plot(vector, color='green', linewidth=2)
    plt.title(title)
    plt.xlabel("Days")
    plt.ylabel("Geomagnetic Intensity")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_entropy_score(entropy, collapse_flag):
    color = 'red' if collapse_flag else 'gray'
    plt.figure(figsize=(6, 4))
    plt.bar(["Entropy Score"], [entropy], color=color)
    plt.title("Symbolic Collapse Detected" if collapse_flag else "Stable Signal")
    plt.ylim(0, 2)
    plt.tight_layout()
    plt.show()
