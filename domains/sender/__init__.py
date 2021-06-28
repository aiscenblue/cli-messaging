import random


class Sender:
    id: bytes
    name: str

    def __init__(self, name: str):
        self.name = name
        self.id = random.randbytes()
