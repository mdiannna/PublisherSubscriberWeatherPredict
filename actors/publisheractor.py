from .publisher import Publisher


class PublisherActor(Actor):
	def __init__(self, name, directory, connection, topic):
        super().__init__(self, name, directory)
        self.publisher = Publisher(connection, topic)
    
    def receive(self, message):
    	raise NotImplemented("Be sure to implement this.")
	
	def publish(self, message):
		self.publisher.publish(message)

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