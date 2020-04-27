from messagebroker import MessageBroker
from subscriber import Subscriber
from publisher import Publisher


UDP_PORT = 5006

messageBroker = MessageBroker("localhost", UDP_PORT)
connection = messageBroker.createConnection()

mSubscriber =  Subscriber(connection, "topic1")
# mSubscriber.fetch()
mSubscriber.receive_messages()
