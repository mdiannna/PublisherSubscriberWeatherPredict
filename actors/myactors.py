import gevent
from gevent.queue import Queue
from enum import Enum
from gevent import Greenlet
import json
import sseclient
import pprint

from .actors import Actor, States, Work
from .requestoriot import RequestorIoT
from .printeractor import PrinterActor
from .directory import Directory
from .webactor import WebActor
from .aggregator import Aggregator

from . import prettyprint
from .workersupervisor import WorkerSupervisor

 

from .messagebroker import MessageBroker
from .subscriber import Subscriber
import time

UDP_PORT = 5006


class Pool(Actor):
    def __init__(self):
        super().__init__()
        directory = Directory()

        messageBroker = MessageBroker("localhost", UDP_PORT)
        connection = messageBroker.createConnection()


        self.printer_actor = PrinterActor('PrinterActor')
        self.web_actor = WebActor('WebActor')
        # topic: IoT
        self.requestorIot = RequestorIoT('Client', directory, connection, "IoT")
        self.supervisor = WorkerSupervisor("Supervisor", directory)
        self.aggregator = Aggregator("Aggregator", directory)

        directory.add_actor("printeractor", self.printer_actor)
        directory.add_actor("webactor", self.web_actor)
        directory.add_actor("supervisor", self.supervisor)
        directory.add_actor("client", self.requestorIot)
        directory.add_actor("aggregator", self.aggregator)

    def start(self):
        self.printer_actor.start()
        self.web_actor.start()
        self.requestorIot.start()
        self.supervisor.start()
        self.aggregator.start()
        
        self.requestorIot.inbox.put('start')
        self.supervisor.inbox.put('start')
        gevent.joinall([self.requestorIot, self.supervisor])

    def get_actors(self):
        return [self.requestorIot, self.supervisor, self.web_actor, self.printer_actor, self.aggregator]
