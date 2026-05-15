from encryption_utils import generate_key, load_key, encrypt_message, decrypt_message

# 1. Initialize the key (Do this once)
generate_key()

# 2. Load it
my_key = load_key()

# 3. Test a password
secret = "MySuperSecret123!"
encrypted = encrypt_message(secret, my_key)
print(f"Encrypted: {encrypted}")

decrypted = decrypt_message(encrypted, my_key)
print(f"Decrypted: {decrypted}")