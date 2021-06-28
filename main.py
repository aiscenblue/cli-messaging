from typing import List

import click

from domains.chat import Chat
from domains.input import Input
from domains.message import Message
from domains.option import Option
from domains.sender import Sender
from reasons import Reason


def messaging(chat: Chat):
    Reason.message_chatting()
    chat.send_message(Input.input_message())
    view_messages(me=chat.sender, messages=chat.messages)
    messaging(chat)


def view_messages(me: str, messages: List[Message]):
    for message in messages:
        if me == message.sender.id:
            click.echo('me -> "{body}" '.format(body=message.body))
        else:
            click.echo('"{body}" <- {id}'.format(body=message.body, id=message.sender.id))


def input_action(chat: Chat):
    action = Option(action=Input.action())
    if action.is_create():
        chat.create()
        messaging(chat)
    elif action.is_join():
        chat.join()
        messaging(chat)
    else:
        Reason.invalid("Action")
        Reason.input("Action")
        input_action(chat)


def main():
    chat = Chat(sender=Sender(Input.input_name()))
    click.echo("Login as: {name}".format(name=chat.sender))
    input_action(chat)


if __name__ == '__main__':
    main()

