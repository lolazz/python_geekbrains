class AddStorageError(Exception):
    def __init__(self, text):
        self.text = f"Cant add this equipment:\n {text}"


class Warehouse:
    def __init__(self):
        self.__storage = []

    def add(self, equipment):
        if not isinstance(equipment, Equipment):
            raise AddStorageError(f"Not an equipment")
        self.__storage.append(equipment)

    def __str__(self):
        return f"На складе сейчас {len(self.__storage)} устройств"


class Equipment:
    __required_props = ("type", "model")

    def __init__(self, type: str = None, model: str = ""):
        self.type = type
        self.model = model

        self.department = None

    def __str__(self):
        return f"{self.type} {self.model}"


class Printer(Equipment):
    def __init__(self, **kwargs):
        super().__init__(type='Printer', **kwargs)


class Scanner(Equipment):
    def __init__(self, **kwargs):
        super().__init__(type='Scanner', **kwargs)


class Xerox(Equipment):
    def __init__(self, **kwargs):
        super().__init__(type='Xerox', **kwargs)


storage = Warehouse()
printer = Printer(model="aaaa")
storage.add(printer)
storage.add(Scanner(model="lexmark300"))
storage.add(Xerox(model="F123"))
print(storage)
print(printer)
