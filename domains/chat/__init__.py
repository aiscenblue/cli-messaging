import random
from typing import List

import click

from Exceptions import InvalidOption
from constants import Method, Layer
from domains.input import Input
from domains.message import Message
from helper import Helper
from reasons import Reason, ErrorReason


class Chat:
    __prefix = "/"
    messages: List[Message] = []

    def __init__(self):
        Reason.welcome()
        Chat.instructions()
        input_command = input(self.__prefix)
        try:
            receiver = Command(input_command).get_receiver()
            if receiver is not None:
                Reason.message_chatting()
                self.send(Message(sender_id=123, receiver_id=receiver, body=Input.input_message()))
            else:
                Reason.message_disconnected()
                Chat()
        except InvalidOption:
            Reason.invalid("Option")
            Chat()

    def send(self, message: Message):
        self.messages.append(message)
        self.print_messages()
        self.send(Message(sender_id=message.sender_id, receiver_id=message.receiver_id, body=Input.input_message()))

    def print_messages(self):
        for _ in self.messages:
            click.echo(_.print())

    @staticmethod
    def instructions():
        Reason.create_group_instruction()
        Reason.join_group_instruction()


class Command:
    receiver: None or int

    def __init__(self, source: str):
        if Helper.has_layer_of(source, Layer.DEFAULT.value):
            [method, receiver] = Helper.split(source)
            if Command.can_create(method):
                self.receiver = Stream().create(receiver)
            else:
                raise InvalidOption(ErrorReason.INVALID_OPTION)
        else:

            raise InvalidOption(ErrorReason.INVALID_OPTION)

    @staticmethod
    def can_create(method: str) -> bool:
        return method == Method.CREATE.value

    def get_receiver(self):
        return self.receiver


class Stream:
    id: int = None
    name: str = None

    def __init__(self):
        pass

    def create(self, receiver: int):
        random_id = random.randint(0, 99999)
        self.name = str(random_id)
        self.id = random_id
        return receiver
