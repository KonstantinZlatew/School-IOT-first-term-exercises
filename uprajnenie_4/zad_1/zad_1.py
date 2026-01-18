import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def adc_quantization_stats(N, Vref):
    steps = 2**N
    lsb = Vref / steps
    emax = lsb / 2               # worst-case ±LSB/2
    erms = lsb / np.sqrt(12)     # RMS for uniform quantization noise
    return steps, lsb, emax, erms

# 1) Параметри за изследване
N_values = np.arange(8, 17)                 # 8..16 bits
Vref_values = np.array([1.8, 2.5, 3.3, 5.0]) # избрани Vref стойности

# 2) Таблица (N x Vref)
rows = []
for Vref in Vref_values:
    for N in N_values:
        steps, lsb, emax, erms = adc_quantization_stats(N, Vref)
        rows.append({
            "N (bits)": N,
            "Vref (V)": Vref,
            "Steps": steps,
            "LSB (V)": lsb,
            "Emax (±V)": emax,
            "Erms (V)": erms
        })

df = pd.DataFrame(rows)
display(df)

# Удобна “матрица” само за Emax
pivot_emax = df.pivot(index="N (bits)", columns="Vref (V)", values="Emax (±V)")
display(pivot_emax)

# 3) Графика 1: Emax спрямо N за различни Vref
plt.figure()
for Vref in Vref_values:
    sub = df[df["Vref (V)"] == Vref]
    plt.plot(sub["N (bits)"], sub["Emax (±V)"], marker='o', label=f"Vref={Vref}V")
plt.xlabel("Разредност N (bits)")
plt.ylabel("Макс. квантова грешка |Emax| (V)")
plt.title("Зависимост на квантова грешка от N при различни Vref")
plt.grid(True)
plt.legend()
plt.show()

# 4) Графика 2: Emax спрямо Vref за избрани N
N_pick = [8, 10, 12, 16]
plt.figure()
for N in N_pick:
    sub = df[df["N (bits)"] == N]
    plt.plot(sub["Vref (V)"], sub["Emax (±V)"], marker='o', label=f"N={N}")
plt.xlabel("Vref (V)")
plt.ylabel("Макс. квантова грешка |Emax| (V)")
plt.title("Зависимост на квантова грешка от Vref при различни N")
plt.grid(True)
plt.legend()
plt.show()

# 5) (Бонус) Реална квантова грешка за конкретен Vin
def quantize_and_error(N, Vref, Vin):
    steps = 2**N
    # clamp
    Vin = np.clip(Vin, 0, Vref)
    code = np.floor((Vin / Vref) * steps).astype(int)
    code = np.clip(code, 0, steps-1)
    Vq = (code / steps) * Vref
    err = Vin - Vq
    return code, Vq, err

Vin_test = 1.65
N_test = 10
Vref_test = 3.3

code, Vq, err = quantize_and_error(N_test, Vref_test, Vin_test)
steps, lsb, emax, erms = adc_quantization_stats(N_test, Vref_test)

print(f"Vin={Vin_test}V, N={N_test}, Vref={Vref_test}V")
print(f"Code={code}, Vq={Vq:.6f}V, Error={err:.6f}V")
print(f"LSB={lsb:.6f}V, MaxError=±{emax:.6f}V")
