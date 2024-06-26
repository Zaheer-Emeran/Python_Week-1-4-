from datetime import datetime
import time

def getCurrentTime():
    return datetime.now().strftime("%m-%d-%Y %H:%M:%S")


class Messenger:
    def __init__(self, listeners=[]):
        self.listeners = listeners

    def send(self, message):
        for listener in self.listeners:
            listener.recieve(message)

    def receive(self, message):
        # Must be implemented by extending classes
        pass


string_Addition = lambda string, date, string_Position: f"String {string_Position}: {string}, Date: {date}"


def print_Messages(input_List):
    for i in range(0, input_List.__len__()):
        print(input_List.__getitem__(i))


MESSAGE_COUNT = 10
EXIT_PROGRAM = "QUIT"


class TooManyMessagesException:
    # Raise an exception if MAX_MESSAGES limit has been reached
    def exception_Message(self):
        print("\n" + f"Value is above {MESSAGE_COUNT}! No more messages are allowed!" + "\n")


class SaveMessages(Messenger):
    tooManyMessagesException = TooManyMessagesException()
    tmp = 0;
    input_List = list(range(MESSAGE_COUNT))
    user_Input = None
    try:
        while user_Input != EXIT_PROGRAM:
            user_Input = input(
                f"Please Enter A String or ({EXIT_PROGRAM}) to exit the program (String Number: {tmp + 1}): ").upper()

            input_List[tmp] = string_Addition(user_Input, getCurrentTime(), (tmp + 1))
            tmp += 1
            if user_Input == EXIT_PROGRAM:
                print("\n" + "Quit has been called, Program will now end!" + "\n")
                break

    except:
        tooManyMessagesException.exception_Message()

    for i in range (0 , tmp):
            print(input_List[i])



