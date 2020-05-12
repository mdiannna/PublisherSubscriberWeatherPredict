# channel=topic
import socket


class MessageBroker():
	def __init__(self, hostname, port):
		self.hostname = hostname
		self.port = port

	def createConnection(self):
		sock = socket.socket(socket.AF_INET, # Internet
		                     socket.SOCK_DGRAM) # UDP

		return sock, self.hostname, self.port


	def subscribe(self):
		pass

	def publish(self):
		pass



# class BrokerConnection():
# 	hostname = "localhost"
# 	port = 0
# 	userid = ""
# 	password = ""
# 	virtual_host = ""

# 	def __init__(hostname, port, userid, password, virtual_host):
# 		# TODO
# 		pass


#conn =  BrokerConnection(hostname="localhost", port=5672,
# ...                           userid="test", password="test",
# ...                           virtual_host="test")