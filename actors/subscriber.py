# channel=topic
import socket

class Subscriber():
	# def __init__(connection, queue, topic, routing_key):
	def __init__(self, connection, topic):
		self.connection = connection
		self.topic = topic
		# self.queue = queue
		# self.routing_key = routing_key

	# def subscribe(connection, topic):
	# 	# TODO
	# 	pass

	# equivalent to wait
	def receive_messages(self):
		# sock = socket.socket(socket.AF_INET, # Internet
		sock, hostname, port = self.connection
		UDP_IP = "127.0.0.1"
		UDP_PORT = 5005

		# sock.bind((hostname, port))
		# sock.bind(("127.0.0.1", port))
		sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
		# sock.close()
		# sock.bind((UDP_IP, UDP_PORT))



		sock.bind(("127.0.0.1", 5006))

		while True:
			print("waiting...")
			data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
			print("received message:" + data)


	def fetch(self):
		# TODO
		pass

	def close(self):
		# TODO:
		pass


# consumer = Consumer(connection=conn, queue="feed",
# ...                     exchange="feed", routing_key="importer")

# >>> def import_feed_callback(message_data, message):
# ...     feed_url = message_data["import_feed"]
# ...     print("Got feed import message for: %s" % feed_url)
# ...     # something importing this feed url
# ...     # import_feed(feed_url)
# ...     message.ack()
# >>> consumer.register_callback(import_feed_callback)
# >>> consumer.wait() # Go into the consumer loop.


# receiving message without callback:
# message = consumer.fetch()