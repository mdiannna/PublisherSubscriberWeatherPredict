
# channel=topic
class Publisher():
	# def __init__(connection, routing_key, topic):
	def __init__(self, connection, topic):
		self.connection = connection
		self.topic = topic

	# equivalent to send
	def publish(self, message):
		conn, hostname, port = self.connection
		# conn.sendto(message, (UDP_IP, UDP_PORT))
		conn.sendto(message, (hostname, port))


	def close(self):
		# TODO
		pass





# Example:
# publisher = Publisher(connection=conn,
# ...                       exchange="feed", routing_key="importer")
# >>> publisher.send({"import_feed": "http://cnn.com/rss/edition.rss"})
# >>> publisher.close()