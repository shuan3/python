from one import one


def two():
    one()


def two_on_two():
    print("two on two")


if __name__ == "__main__":
    two()
else:
    print("two is being imported")
