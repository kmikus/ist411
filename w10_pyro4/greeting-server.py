import Pyro4

@Pyro4.expose
class GreetingMaker(object):
	def get_fortune(self, name):
		return "Hello, {0}. Here is your foturne message:\n" \
		"Behold the warranty -- the bold print giveth and the fine print taketh away.".format(name)

daemon = Pyro4.Daemon()
uri = daemon.register(GreetingMaker)

print("Ready. Ojbect uri =", uri)
daemon.requestLoop()
