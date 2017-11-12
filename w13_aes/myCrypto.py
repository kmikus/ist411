from Crypto.Cipher import AES

pad = b" "
print(pad)
obj = AES.new("This is a key123", AES.MODE_CBC, "This is an IV456")
message = input("Enter a message to encrypt: ")
plaintext = message.encode("utf-8")
print(plaintext)
length = 16 - (len(plaintext)%16)
print(length)
plaintext += length*pad
print(plaintext)
ciphertext = obj.encrypt(plaintext)
print(ciphertext)
obj2 = AES.new("This is a key123", AES.MODE_CBC, "This is an IV456")
print(obj2.decrypt(ciphertext))
