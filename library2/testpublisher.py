from messagebroker import MessageBroker
from subscriber import Subscriber
from publisher import Publisher
import time

UDP_PORT = 5006

messageBroker = MessageBroker("localhost", UDP_PORT)
connection = messageBroker.createConnection()

mPublisher = Publisher(connection, "topic1")
for i in range(1, 100):
	mPublisher.publish("Hello!")
	print("publish!")
	time.sleep(1);

# mSubscriber =  Subscriber(connection, "topic1")
# # mSubscriber.fetch()
# mSubscriber.receive_messages()


# Reading list:
# https://wiki.python.org/moin/UdpCommunication
# https://en.wikipedia.org/wiki/Message_broker
# https://medium.com/@xaviergeerinck/an-introduction-to-message-brokers-9bd203b4ebbd
# https://github.com/ask/kombu
# https://docs.celeryproject.org/projects/kombu/en/stable/userguide/examples.html
# https://github.com/ask/carrot/