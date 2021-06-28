from reasons import Reason


class Input:
    @staticmethod
    def input_name(subject: str = "name") -> str:
        _input: str = str(input(Reason.input(subject)))
        return _input if _input is not None else "anonymous"

    @staticmethod
    def input_email() -> str:
        field = "email"
        _email: str = str(input(Reason.input(field)))
        if _email is None:
            Reason.invalid(field)
            Input.input_email()
        else:
            return _email

    @staticmethod
    def input_message() -> str:
        return str(input(Reason.input("message")))


