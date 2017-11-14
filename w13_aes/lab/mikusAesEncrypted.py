from Crypto.Cipher import AES
import json

try:
	fh = open("payloadMikus.json", "r")
	jsonData = json.loads(fh.read())
	fh.close()
	payload = json.dumps(jsonData)

	pad = b" "
	print("Padding: ", pad)
	obj = AES.new("This is a key123", AES.MODE_CBC, "This is an IV456")
	plaintext = payload.encode("utf-8")
	print("Plaintext: ", plaintext)
	length = 16 - (len(plaintext)%16)
	print("Mod length: ", length)
	plaintext += length*pad
	print("Padded plaintext: ", plaintext)
	ciphertext = obj.encrypt(plaintext)
	print("Ciphertext: ", ciphertext)

	fh = open("encryptedMikus.json", "wb")
	fh.write(ciphertext)
	fh.close()
except Exception as e:
	print(e)
