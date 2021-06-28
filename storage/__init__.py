import random
from enum import Enum

class Storage:
    __email = "aiscenblue@gmail.com"
    __name = "aiscenblue"

    def get_by_email(self, email: str) -> str:
        return self.__email if self.__email == email else None

    def get_by_name(self, name: str) -> str:
        return self.__name if self.__name == name else None

    def find_by_name(self, name: str) -> str:
        return name

    def create(self, name: str) -> int:
        return random.randint()


class StorageType(Enum):
    GROUP = "group"
