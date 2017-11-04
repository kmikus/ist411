# Project: zlib demonstration
# Purpose Details: Use zlib to compress file using remote Pyro4 methods
# Course: IST411
# Author: Kevin Mikus
# Date Developed: 2017-11-02
# Last Date Changed: 2017-11-04
# Rev: 0.3

import zlib, sys, Pyro4, base64
try:
	# read file in binary mode
	print("Reading in file")
	payload = open("payloadMikus.json", "rb")
	data = payload.read()
	print("Original payload: ", data)
	payload.close()

	# compress the byte array file contents into string object
	print("Compressing the payload")
	payloadComp = zlib.compress(data)
	print("Compressed payload: ", payloadComp)

	# generate checksum
	checksum = zlib.crc32(data)
	print("Checksum: ", checksum)

	# setup Pyro4 decompressor object
	decompressor = Pyro4.Proxy("PYRONAME:comp.decompressor")

	# decompress the string object using remote Pyro4 call
	payloadDecomp = decompressor.decomp(payloadComp)
	print("Decompressed payload: ", payloadDecomp)
	payloadDecomp = base64.b64decode(payloadDecomp['data'])
	print("Decoded payload: ", payloadDecomp)

	# generate decompressed checksum
	checksumGen = zlib.crc32(payloadDecomp)
	print("Decompressed checksum: ", checksumGen)

	# verify checksum
	if checksum == checksumGen:
		print("Checksum matches")
	else:
		print("Error: checksum mismatch")
except Exception as e:
	print(e)
