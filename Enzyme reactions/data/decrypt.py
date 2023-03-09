# import required module
from cryptography.fernet import Fernet

with open("thekey.txt", "rb") as key:
    secretkey = key.read()

with open("data_2.txt", "rb") as f:
    encrypted = f.read()
    content = Fernet(secretkey).decrypt(encrypted)

with open("decrypted.txt", "wb") as f:
    f.write(content)