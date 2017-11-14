from Crypto.Cipher import AES
import json

try:
	fh = open("encryptedMikus.json", "rb")
	rawData = fh.read()
	fh.close()

	obj2 = AES.new("This is a key123", AES.MODE_CBC, "This is an IV456")
	decrypted = obj2.decrypt(rawData).strip()
	decrypted = json.loads(decrypted.decode("utf-8"))
	print("Decrypted file: ", decrypted)

	fh = open("payloadMikus.json", "r")
	originalData = json.loads(fh.read())
	fh.close()
	print("Original file: ", originalData)

	print("Verifying input and output are equal")

	if originalData == decrypted:
		print("File contents match")
	else:
		print("Error: input and output do not match")
except e as Exception:
	print(e)
