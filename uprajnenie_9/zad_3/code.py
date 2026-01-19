import numpy as np
import matplotlib.pyplot as plt

# Коефициент на Зеебек (типична стойност за BiTe TEG)
S = 200e-6  # V/°C

# Температурна разлика
delta_T = np.arange(1, 51, 1)  # от 1 до 50 °C

# Различни товарни съпротивления (Ω)
R_loads = [10, 50, 100, 500]

# Изчисляване на напрежението
V = S * delta_T

plt.figure(figsize=(10, 6))

for R in R_loads:
    P = V**2 / R
    plt.plot(delta_T, P * 1e6, label=f"R = {R} Ω")

plt.xlabel("ΔT (°C)")
plt.ylabel("Мощност (µW)")
plt.title("Генерирана мощност от TEG при различни ΔT и товар")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Примерни числови резултати
print("Примерни стойности:")
for dt in [5, 20, 50]:
    v = S * dt
    p = v**2 / 100
    print(f"ΔT = {dt} °C → V = {v*1000:.2f} mV, P (R=100Ω) = {p*1e6:.2f} µW")
