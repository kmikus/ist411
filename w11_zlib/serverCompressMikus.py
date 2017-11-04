# Project: zlib demonstration
# Purpose Details: Use zlib to compress file using remote Pyro4 methods
# Course: IST411
# Author: Kevin Mikus
# Date Developed: 2017-11-02
# Last Date Changed: 2017-11-04
# Rev: 0.3

import Pyro4, zlib, base64

# decompressor class for use on client side
@Pyro4.expose
class Decompressor(object):
	def decomp(self, compdata):
		data = compdata["data"]
		data = base64.b64decode(data)
		payloadDecomp = zlib.decompress(data)
		return payloadDecomp

	def genChecksum(self, data):
		payloadDecomp = self.decomp(data)
		checksum = zlib.crc32(payloadDecomp)
		return checksum

# setup listener
daemon = Pyro4.Daemon()

# find and register nameserver entry for lookup
ns = Pyro4.locateNS()
uri = daemon.register(Decompressor)
ns.register("comp.decompressor", uri)

# start listener
print("Ready")
daemon.requestLoop()
