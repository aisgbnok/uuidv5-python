import uuid


def print_hi(name):
    uuid4 = uuid.UUID('00000000-0000-0000-0000-000000000000')
    uid = uuid.uuid5(uuid4, "Windows Terminal")

    print(uid)


if __name__ == '__main__':
    print_hi('PyCharm')
