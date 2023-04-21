class RSA:
    def __init(self, p: int, q: int):
        self.p = p
        self.q = q
        self.phi: int = (p-1)*(q-1)
        self.N: int = p * q

    def __init__(self, p: int, q: int, e: int, d: int):
        self.__init(p, q)
        self.e = e
        self.d = d

    def encrypt(self, message: int):
        return (message**self.e % self.N)

    def decrypt(self, code: int):
        return (code**self.d % self.N)


def main():
    a = RSA(17, 11, 107, 3)
    print(a.decrypt(4))


if __name__ == "__main__":
    main()
