from datetime import datetime


def getCurrentTime():
    return datetime.now().strftime("%m-%d-%Y %H:%M:%S")

class Messenger:
    def __init__(self, listeners = []):
        self.listeners = listeners

    def send(self,message):
        for listener in self.listeners:
            listener.recieve(message)

    def receive(self,message):
        # Must be implemented by extending classes
        pass

string_Addition = lambda string , date: f"String: {string}, Date: {date}"


def print_Messages(input_List):
    for i in range(0, input_List.__len__()):
        print(input_List.__getitem__(i))


class SaveMessages(Messenger):
    tmp = 0;
    input_List = list(range(5))
    user_Input = input("Please Enter A String: ").lower()
    while user_Input != "quit" and tmp < 5:
        input_List[tmp] = string_Addition(user_Input,getCurrentTime())
        tmp += 1
        user_Input = input("Please Enter A String: ").lower()
    print_Messages(input_List)
