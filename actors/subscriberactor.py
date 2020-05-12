from .subscriber import Subscriber


class SubscriberActor(Actor):
	def __init__(self, name, directory, connection, topic):
        super().__init__(self, name, directory)
        self.subscriber = Subscriber(connection, topic)
    
    def receive(self, message):
    	raise NotImplemented("Be sure to implement this.")
	
	def subscribe(self, topic):
        self.subscriber.subscribe(topic)

    # called when receives messages from publisher
    def onreceive(self, message):
        # TODO -receive_messages?  
        pass

    # def get_printer_actor(self):
    #     return self.directory.get_actor('printeractor')

    # def get_web_actor(self):
    #     return self.directory.get_actor('webactor')
    
    # def get_aggregator_actor(self):
    #     return self.directory.get_actor('aggregator')

    # def get_supervisor_actor(self):
    #     return self.directory.get_actor('supervisor')
        
    def get_directory(self):
        return self.directory