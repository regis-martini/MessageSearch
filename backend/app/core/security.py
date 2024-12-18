from cryptography.fernet import Fernet

# Generate a key (run once and save securely)
# key = Fernet.generate_key()
key = b"your-secure-key-here"
cipher = Fernet(key)


def encrypt_message(message: str) -> str:
    return cipher.encrypt(message.encode()).decode()


def decrypt_message(encrypted_message: str) -> str:
    return cipher.decrypt(encrypted_message.encode()).decode()
