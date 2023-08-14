# -----------------------------------------------------------
# filename: test_fernet_encryption.py
#
# Description: Unit test for the Encryptor class.
# Github Repo: https://github.com/Tamandeep-Singh/File-Encrypt
# Released under MIT License 
# -----------------------------------------------------------


import unittest
import sys
sys.path.insert(0, '/home/tam/projects/file-encrypt/lib')
from fernet_encrypt import FernetEncrypt

class TestFernetEncrypt(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Setup an instance of FernetEncrypt"""
        cls.fernet_encrypt = FernetEncrypt()
        cls.dummy_data = "gAAAAABjrKop0gi3kqmCQDZajeBbgbpqlIviMSHbo7jP7-g2Nfn3_gQVMD4JxK3kUbh-gcP-G_vag28fEOvU0ahDF5ikjZIUi6H8RTJHAVeLAaSxQa-oWkCxPNhUmylnP_gwQMqNs870krALJ1oABQzlqLWa3d8ZmQ=="
        cls.dummy_data_bytes = FernetEncrypt.get_bytes(cls.dummy_data)
        cls.plain_text = "this is a demo test file to be passed onto the file encryptor"
        cls.plain_text_bytes = FernetEncrypt.get_bytes(cls.plain_text)

    def test_key(self):
        """Valid Fernet Key must be base64 encoded and have length 44 and must be same from the present key file."""
        key_len = len(self.fernet_encrypt.key)
        key_str = self.fernet_encrypt.key.decode('utf-8')
        self.assertEqual(key_len, 44)
        self.assertEqual(key_str, "RRqtotimX-hLNK-RC-Ra0imxFIwWyHGuEzVYsKyhIXE=")

    def test_decrypt(self):
        """Test that the decrypted bytes match with the regular plain text provided by the file"""
        self.assertEqual(self.fernet_encrypt.decrypt(self.dummy_data_bytes), self.plain_text_bytes)
    

if __name__ == "__main__":
    """Run main unittest for testing FernetEncrypt."""
    unittest.main()