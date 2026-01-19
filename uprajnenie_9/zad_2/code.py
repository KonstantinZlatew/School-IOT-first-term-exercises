import numpy as np
import matplotlib.pyplot as plt

# Времева ос (1 секунда)
t = np.linspace(0, 1, 1000)

# Честоти на вибрации (Hz)
frequencies = [10, 50, 100, 200]

# Коефициент на преобразуване
k = 5  # V (примерна стойност)

plt.figure(figsize=(14, 4))

for i, f in enumerate(frequencies):
    V = k * np.sin(2 * np.pi * f * t)
    
    plt.subplot(1, len(frequencies), i + 1)
    plt.plot(t, V)
    plt.title(f"Честота: {f} Hz")
    plt.xlabel("Време (s)")
    plt.ylabel("Напрежение (V)")
    plt.grid(True)

plt.suptitle("Пиезоелектрично напрежение при различни честоти на вибрации")
plt.tight_layout()
plt.show()
