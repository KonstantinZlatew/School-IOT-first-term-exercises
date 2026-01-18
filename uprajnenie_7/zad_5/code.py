import numpy as np
import time

# Размер на матриците (намали, ако забива)
N = 200

# Генериране на случайни матрици
A = np.random.rand(N, N)
B = np.random.rand(N, N)

print(f"Умножение на матрици {N}x{N}...")

# --- ВАРИАНТ 1: CPU стил (вложени цикли) ---
C_cpu = np.zeros((N, N), dtype=np.float64)

start_time = time.perf_counter()
for i in range(N):
    for j in range(N):
        s = 0.0
        for k in range(N):
            s += A[i, k] * B[k, j]
        C_cpu[i, j] = s
cpu_time = time.perf_counter() - start_time
print(f"CPU време (Loops): {cpu_time:.4f} секунди")

# --- ВАРИАНТ 2: Accelerator стил (NumPy/BLAS) ---
# Малък warm-up (понякога първото извикване има overhead)
_ = np.dot(A[:10, :10], B[:10, :10])

start_time = time.perf_counter()
C_acc = np.dot(A, B)
acc_time = time.perf_counter() - start_time
print(f"Accelerator време (NumPy): {acc_time:.6f} секунди")

# Проверка за коректност (позволяваме малка числена разлика)
max_diff = np.max(np.abs(C_cpu - C_acc))
print(f"Макс. разлика между резултатите: {max_diff:e}")

# Ускорение
speedup = cpu_time / acc_time if acc_time > 0 else float('inf')
print(f"\nХардуерното ускорение (като ефект) е: {speedup:.2f} пъти по-бързо!")
