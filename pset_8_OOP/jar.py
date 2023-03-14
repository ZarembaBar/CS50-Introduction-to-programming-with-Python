class Jar:
    def __init__(self, capacity = 12):
        if capacity < 0:
            raise ValueError

        self._capacity = capacity
        self._size = 0

    def __str__(self):
        cookies = ""
        for _ in range(self._size):
            cookies += "🍪"
        return cookies

    def deposit(self, n):
        self._size += n
        if self._size > 12:
            raise ValueError
        return self._size

    def withdraw(self, n):
        self._size -= n
        if self._size < 0:
            raise ValueError
        return self._size

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

jar = Jar()
print(jar.deposit)