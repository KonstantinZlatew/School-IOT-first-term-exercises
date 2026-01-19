import numpy as np
import matplotlib.pyplot as plt

# Параметри на PV клетката
A = 10e-4        # площ в m² (10 cm²)
eta = 0.15       # ефективност 15%

# Осветеност
E_indoor = np.linspace(10, 100, 50)     # W/m² (вътрешна)
E_outdoor = np.linspace(100, 1000, 50)  # W/m² (външна)

# Мощност
P_indoor = A * eta * E_indoor
P_outdoor = A * eta * E_outdoor

# Числови примери
print(f"Минимална вътрешна мощност: {P_indoor[0]*1000:.2f} mW")
print(f"Максимална вътрешна мощност: {P_indoor[-1]*1000:.2f} mW")
print(f"Минимална външна мощност: {P_outdoor[0]*1000:.2f} mW")
print(f"Максимална външна мощност: {P_outdoor[-1]*1000:.2f} mW")

# Визуализация
plt.figure(figsize=(10, 6))

plt.plot(E_indoor, P_indoor * 1000, label="Вътрешна среда", color="blue", linewidth=2)
plt.plot(E_outdoor, P_outdoor * 1000, label="Външна среда", color="orange", linewidth=2)

plt.xlabel("Осветеност (W/m²)")
plt.ylabel("Генерирана мощност (mW)")
plt.title("Генерирана мощност от PV клетка при различна осветеност")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
