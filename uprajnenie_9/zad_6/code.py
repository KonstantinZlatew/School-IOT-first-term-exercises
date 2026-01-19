import numpy as np
import matplotlib.pyplot as plt

# Параметри
P_tx = 0.1       # W
G = 2            # усилване
A_eff = 0.01     # m²
d = np.linspace(1, 10, 100)  # разстояние (m)

# Плътност на мощността
P_density = (P_tx * G) / (4 * np.pi * d**2)

# Получена мощност
P_received = P_density * A_eff

# Визуализация
plt.figure(figsize=(9, 5))
plt.plot(d, P_received * 1e6, linewidth=2)
plt.xlabel("Разстояние (m)")
plt.ylabel("Получена мощност (µW)")
plt.title("Получена RF мощност от Wi-Fi рутер")
plt.grid(True)
plt.tight_layout()
plt.show()

# Числови примери
print("Примерни стойности:")
for dist in [1, 2, 5, 10]:
    Pd = (P_tx * G) / (4 * np.pi * dist**2)
    Pr = Pd * A_eff
    print(f"d = {dist:2d} m → P ≈ {Pr*1e6:.3f} µW")
