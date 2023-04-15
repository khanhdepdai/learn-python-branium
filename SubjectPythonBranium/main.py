class s:
    def __init__(self, a, b):
        self.a = a
        self.b = b


def a(list):
    list[0], list[1] = list[1], list[0]


e = s(5, 6)
y = s(8, 9)
list = [e, y]
a(list)
print(list[0].a, list[1].a)
