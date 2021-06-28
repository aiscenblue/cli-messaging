from domains.sender import Sender


class Message:
    sender: Sender = None
    body: str = None

    def __init__(self, sender: Sender, body: str):
        self.sender = sender
        self.body = body

    def print(self):
        if self.sender_id != self.receiver_id:
            return self.send_from()
        else:
            return self.send_to()

    def send_to(self):
        return '@{sender} -> message="{message}"'.format(sender=self.sender.id, message=self.body)

    def send_from(self):
        return '"{message}"=message <- {sender}@'.format(sender=self.sender.id, message=self.body)
