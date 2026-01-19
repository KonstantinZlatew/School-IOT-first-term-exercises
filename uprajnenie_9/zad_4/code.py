import numpy as np
import matplotlib.pyplot as plt

# Параметри
C = 1.0          # F
R_charge = 100   # Ω
V_src = 3.3      # V

# Различни времена за зареждане (s)
charge_times = [5, 10, 20, 30, 40, 50]

# Различни товари за разреждане (Ω)
R_loads = [100, 200, 500, 1000]

# Времева ос (до 50 секунди)
t = np.linspace(0, 50, 2000)

# --- 1) Зареждане за различни периоди ---
plt.figure(figsize=(10, 5))
for Tch in charge_times:
    t_ch = t[t <= Tch]
    V_charge = V_src * (1 - np.exp(-t_ch / (R_charge * C)))
    plt.plot(t_ch, V_charge, label=f"Зареждане до {Tch}s")

plt.xlabel("Време (s)")
plt.ylabel("Vc (V)")
plt.title("Зареждане на суперкондензатор (C=1F, Rcharge=100Ω, Vsrc=3.3V)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# --- 2) Разреждане през различни товари ---
# Приемаме, че кондензаторът е зареден до напрежението при 50s зареждане
V0 = V_src * (1 - np.exp(-50 / (R_charge * C)))

plt.figure(figsize=(10, 5))
for R_load in R_loads:
    V_discharge = V0 * np.exp(-t / (R_load * C))
    plt.plot(t, V_discharge, label=f"Rload={R_load}Ω")

plt.xlabel("Време (s)")
plt.ylabel("Vc (V)")
plt.title(f"Разреждане на суперкондензатор (начално V0={V0:.2f}V)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# --- 3) Числови резултати: напрежение след 5..50s зареждане ---
print("Напрежение след зареждане:")
for Tch in charge_times:
    Vt = V_src * (1 - np.exp(-Tch / (R_charge * C)))
    print(f"t = {Tch:2d} s -> Vc = {Vt:.3f} V")

print(f"\nНачално напрежение за разреждане (след 50s): V0 = {V0:.3f} V")
