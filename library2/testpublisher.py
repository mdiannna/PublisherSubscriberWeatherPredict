from messagebroker import MessageBroker
from subscriber import Subscriber
from publisher import Publisher


UDP_PORT = 5006

messageBroker = MessageBroker("localhost", UDP_PORT)
connection = messageBroker.createConnection()

mPublisher = Publisher(connection, "topic1")
for i in range(1, 5000):
	mPublisher.publish("Hello!")
	print("publish!")

# mSubscriber =  Subscriber(connection, "topic1")
# # mSubscriber.fetch()
# mSubscriber.receive_messages()
