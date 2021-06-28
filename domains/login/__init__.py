from storage import Storage


class Login:
    __name: str = None
    __email: str = None
    __error: str = None

    def __init__(self, **kwargs):
        if kwargs.get("name") is None:
            self.__error = "Invalid name! "
        elif kwargs.get("email") is None:
            self.__error = "Invalid email!"
        else:
            self.__name = kwargs.get("name")
            self.__email = kwargs.get("email")

    def authorize(self) -> str:
        storage = Storage()
        if storage.get_by_name(self.__name) is None or storage.get_by_email(self.__email) is None:
            self.__error = "Authentication failed!"
        return self.__error
