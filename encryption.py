# Implement encryption and decryption algorithms (e.g., AES, DES, RSA)

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

class AESCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, plaintext):
        cipher = AES.new(self.key, AES.MODE_CBC)
        iv = cipher.iv
        ciphertext = cipher.encrypt(pad(plaintext.encode('utf-8'), AES.block_size))
        return iv + ciphertext

    def decrypt(self, ciphertext):
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        plaintext = unpad(cipher.decrypt(ciphertext[AES.block_size:]), AES.block_size)
        return plaintext.decode('utf-8')

# Example usage:
if __name__ == "__main__":
    key = get_random_bytes(16)  # Generate a random 16-byte key
    aes_cipher = AESCipher(key)

    plaintext = "Hello, world!"
    encrypted_data = aes_cipher.encrypt(plaintext)
    decrypted_data = aes_cipher.decrypt(encrypted_data)

    print("Plaintext:", plaintext)
    print("Encrypted:", encrypted_data)
    print("Decrypted:", decrypted_data)
