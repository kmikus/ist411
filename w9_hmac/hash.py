import hashlib

try:
	data = '{"payload":"hashLab"}'
	checksum = hashlib.md5(data.encode()).hexdigest()
	print("MD5: ", checksum)
	checksum = hashlib.sha1(data.encode()).hexdigest()
	print("sha1: ", checksum)
	checksum = hashlib.sha256(data.encode()).hexdigest()
	print("sha256: ", checksum)
except:
	print("Log exception: ", sys.exc_info()[0])
