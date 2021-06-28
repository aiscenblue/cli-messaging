from typing import List

from domains.message import Message
from domains.sender import Sender
from reasons import Reason


class Chat:
    __sender: Sender = None
    __authors: List[Sender] = []
    __messages: List[Message] = []

    def __init__(self, sender: Sender):
        Reason.welcome()
        self.__sender = sender

    def create(self):
        self.__authors.append(self.__sender)

    def join(self):
        self.__authors.append(self.__sender)

    def send_message(self, content: str):
        message = Message(sender=self.__sender, body=content)
        self.__messages.append(message)
        return self

    @property
    def messages(self) -> List[Message]:
        return self.__messages

    @property
    def sender(self) -> str:
        return str(self.__sender.id)
