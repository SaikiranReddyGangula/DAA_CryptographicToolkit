# Implement test cases for Encryption and Decryption

import unittest
from encryption import AESCipher

class TestEncryption(unittest.TestCase):
    def test_encrypt_decrypt(self):
        key = b'Sixteen byte key'
        aes_cipher = AESCipher(key)

        plaintext = "Hello, world!"
        encrypted_data = aes_cipher.encrypt(plaintext)
        decrypted_data = aes_cipher.decrypt(encrypted_data)

        self.assertEqual(decrypted_data, plaintext)

if __name__ == '__main__':
    unittest.main()


