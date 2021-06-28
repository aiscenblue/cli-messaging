class Helper:
    @staticmethod
    def find(name: str, items: []):
        return list(filter(lambda x: x == name, items))

    @staticmethod
    def find_action(source: str):
        Helper.split(source)

    @staticmethod
    def split(source: str):
        separator = ":"
        return source.split(separator)

    @staticmethod
    def has_layer_of(source: str, layer: int) -> bool:
        return len(Helper.split(source)) == layer

    @staticmethod
    def get_id(source: str):
        layer_of = 2
        return source[layer_of - 1] if Helper.has_layer_of(source, layer_of) else None

