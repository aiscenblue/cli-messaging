class Message:
    def __init__(self, sender_id: int, receiver_id: int, body: str):
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.body = body

    def print(self):
        if self.sender_id != self.receiver_id:
            return self.send_from()
        else:
            return self.send_to()

    def send_to(self):
        return '@{sender} -> message="{message}"'.format(sender=self.sender_id, message=self.body)

    def send_from(self):
        return '"{message}"=message <- {sender}@'.format(sender=self.sender_id, message=self.body)
