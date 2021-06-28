import click


class Reason:
    @staticmethod
    def success():
        click.echo("Success!")

    @staticmethod
    def created(subject: str):
        click.echo("{sub} created!".format(sub=subject))

    @staticmethod
    def invalid(subject: str):
        click.echo("Invalid {sub}!".format(sub=subject))

    @staticmethod
    def exist(subject: str):
        click.echo("{sub} already exist!".format(sub=subject))

    @staticmethod
    def welcome():
        click.echo("===== ENCRYPTED MESSAGE =====")

    @staticmethod
    def input(field: str):
        return "Input your {name}: ".format(name=field)

    @staticmethod
    def create_group_instruction():
        click.echo("/create:{id} -> to create a group")

    @staticmethod
    def join_group_instruction():
        click.echo("/join:{id} -> to join a group")

    @staticmethod
    def message_disconnected():
        click.echo(ErrorReason.MESSAGE_DISCONNECTED)

    @staticmethod
    def message_chatting():
        click.echo("You can now chat!")


class ErrorReason:
    LAYER_404 = "Layer not found!"
    ENTITY_404 = "Entity not found!"
    METHOD_404 = "Method not found!"
    INVALID_OPTION = "Invalid option!"
    MESSAGE_DISCONNECTED = "Message is disconnected..."
