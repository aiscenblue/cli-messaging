import click

from domains.chat import Chat
from domains.input import Input
from domains.login import Login

from reasons import Reason


def login_attempt():
    login = Login(name=Input.input_name(), email=Input.input_email()).authorize()
    if login is not None:
        click.echo(login)
        login_attempt()
    else:
        Reason.success()
        Chat()


def main():
    login_attempt()


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
