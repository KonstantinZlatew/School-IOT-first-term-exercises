import matplotlib.pyplot as plt

# Работни цикли
duty_cycles = [0.01, 0.02, 0.05, 0.10, 0.15, 0.20, 0.25]

# Консумации
I_active = 5e-3   # 5 mA
I_sleep = 10e-6   # 10 µA

# Средни токове
avg_currents_mA = []

for dc in duty_cycles:
    I_avg = dc * I_active + (1 - dc) * I_sleep
    avg_currents_mA.append(I_avg * 1000)  # в mA

# Визуализация
plt.figure(figsize=(9, 5))
plt.bar([f"{int(dc*100)}%" for dc in duty_cycles], avg_currents_mA)
plt.xlabel("Работен цикъл (%)")
plt.ylabel("Среден ток (mA)")
plt.title("Зависимост на средната консумация от работния цикъл")
plt.grid(axis="y")
plt.tight_layout()
plt.show()

# Табличен изход
print("Duty Cycle | Среден ток (mA)")
print("----------------------------")
for dc, i in zip(duty_cycles, avg_currents_mA):
    print(f"{int(dc*100):>3}%       | {i:.4f}")
