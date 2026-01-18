from cryptography.fernet import Fernet

# --- Симулация на "Secure Element" (Hardware Root of Trust) ---
class SecureElement:
    def __init__(self):
        # Този ключ се генерира "вътре" и не се дава навън (в симулацията)
        self.__hardware_key = Fernet.generate_key()
        self.__cipher = Fernet(self.__hardware_key)

    def encrypt_data(self, message: str) -> bytes:
        return self.__cipher.encrypt(message.encode())

    def decrypt_data(self, token: bytes) -> str:
        return self.__cipher.decrypt(token).decode()

# --- Потребителски код (Приложение) ---
tpm_chip = SecureElement()

message = "Firmware Update v2.0 - Secret Code: 1234"
print(f"Оригинално съобщение: {message}")

# 1) Криптиране чрез "хардуера"
encrypted_msg = tpm_chip.encrypt_data(message)
print(f"Криптирано (в паметта): {encrypted_msg}")

# 2) Декриптиране чрез "хардуера" (успешно)
decrypted_msg = tpm_chip.decrypt_data(encrypted_msg)
print(f"Декриптирано легално: {decrypted_msg}")

# 3) Опит за "хакване" (без достъп до вътрешния ключ)
try:
    fake_key = Fernet.generate_key()
    fake_cipher = Fernet(fake_key)
    fake_cipher.decrypt(encrypted_msg)
except Exception as e:
    print(f"\n[!] ГРЕШКА при хакване: Невалиден ключ! ({e})")

print("\nИзвод: Без достъп до хардуерния ключ, данните не могат да бъдат декриптирани.")
