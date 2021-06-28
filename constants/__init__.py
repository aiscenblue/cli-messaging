from enum import Enum

from Exceptions import MethodNotFound, EntityNotFound
from helper import Helper
from reasons import ErrorReason


class Method(Enum):
    CREATE = "create"
    JOIN = "join"

    @staticmethod
    def find(source: str):
        layer_placement = Layer.DEFAULT.value
        if Helper.has_layer_of(source, layer_placement):
            method: str = Helper.split(source)[layer_placement - 1]
            return Helper.find(method, Method)
        else:
            raise MethodNotFound(ErrorReason.METHOD_404)


class Layer(Enum):
    DEFAULT = 2

    @staticmethod
    def find(source: str):
        return len(Helper.split(source))




