from dataclasses import dataclass


class PersonL:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address


@dataclass
class Person:
    name: str
    address: str


def main() -> None:
    person = Person(name="Super", address="man")
    print(person.name)


def mainL() -> None:
    person = PersonL(name="Super", address="man")
    print(person.name)


if __name__ == "__main__":
    main()
    mainL()
