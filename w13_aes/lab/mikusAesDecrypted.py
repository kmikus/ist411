from Crypto.Cipher import AES
import json

fh = open("encryptedMikus.json", "rb")
rawData = fh.read()
fh.close()

obj2 = AES.new("This is a key123", AES.MODE_CBC, "This is an IV456")
decrypted = obj2.decrypt(rawData).strip()
print(decrypted)
