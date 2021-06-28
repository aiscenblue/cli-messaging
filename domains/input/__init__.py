from reasons import Reason


class Input:
    @staticmethod
    def input_name(subject: str = "name") -> str:
        _input: str = str(input(Reason.input(subject)))
        return _input if _input is not None else "anonymous"

    @staticmethod
    def action() -> str:
        return str(input(Reason.input("Action")))

    @staticmethod
    def input_message() -> str:
        return str(input(Reason.input("message")))


