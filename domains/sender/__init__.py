import random


class Sender:
    id: int
    name: str

    def __init__(self, name: str):
        self.name = name
        self.id = Sender.generate_id()

    @staticmethod
    def generate_id():
        return random.randint(0, 99999)
