from datetime import datetime
def getCurrentTime():
    return datetime.now().strftime("%m-%d-%Y %H:%M:%S")

class Messenger:
    def __init__(self,listeners=[]):
        self.listeners = listeners


    def send(self,message):
        for listener in self.listeners:
            listener.revieve(message)

    def receive(self,message):
        pass