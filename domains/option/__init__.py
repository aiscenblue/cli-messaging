class Option:
    __action: str = None

    def __init__(self, action: str):
        self.__action = action

    def is_join(self):
        return self.__action == "join"

    def is_create(self):
        return self.__action == "create"

