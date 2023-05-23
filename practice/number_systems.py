import math


class Quaternion:
    def __init__(self, r: float, i: float, j: float, k: float) -> None:
        self.r, self.i, self.j, self.k = r, i, j, k

    def __round__(self, ndigits=0):
        self.r = round(self.r, ndigits)
        self.i = round(self.i, ndigits)
        self.j = round(self.j, ndigits)
        self.k = round(self.k, ndigits)

        return self

    def __str__(self) -> str:
        return f"{self.r} + {self.i}i + {self.j}j + {self.k}k"

    def __add__(self, Q):
        r: float = self.r + Q.r
        i: float = self.i + Q.i
        j: float = self.j + Q.j
        k: float = self.k + Q.k
        return Quaternion(r, i, j, k)

    def __iadd__(self, Q):
        self = self + Q
        return self

    def __sub__(self, Q):
        Q *= UnitQ.neg1
        return self + Q

    def __isub__(self, Q):
        self = self - Q
        return self

    def __mul__(self, Q):
        r = self.r * Q.r - self.i * Q.i - self.j * Q.j - self.k * Q.k
        i = self.r * Q.i + self.i * Q.r + self.j * Q.k - self.k * Q.j
        j = self.r * Q.j - self.i * Q.k + self.j * Q.r + self.k * Q.i
        k = self.r * Q.k + self.i * Q.j - self.j * Q.i + self.k * Q.r
        return Quaternion(r, i, j, k)

    def __imul__(self, Q):
        self = self * Q
        return self

    def inv(self):
        coefficient = Quaternion(
            1/(self.r**2 + self.i**2 + self.j**2 + self.k**2), 0, 0, 0)
        return coefficient*Quaternion(self.r, -self.i, -self.j, -self.k)

    def conj(self):
        i = UnitQ.i
        j = UnitQ.j
        k = UnitQ.k

        return Quaternion(-1/2, 0, 0, 0)*(self + i*self*i + j*self*j + k*self*k)

    def norm(self) -> float:
        return math.sqrt(self.r**2 + self.i**2 + self.j**2 + self.k**2)

    def dist(self, Q):
        return (self - Q).norm()

    def unit(self):
        return Quaternion(self.norm(), 0, 0, 0).inv() * self


class UnitQ:
    neg1 = Quaternion(-1, 0, 0, 0)
    r = Quaternion(1, 0, 0, 0)
    i = Quaternion(0, 1, 0, 0)
    j = Quaternion(0, 0, 1, 0)
    k = Quaternion(0, 0, 0, 1)


def main():
    p = Quaternion(0.5, 0.5, 0.5, 0.5)
    q = Quaternion(-4, -3, -2, -1)
    print(p.unit())


if __name__ == '__main__':
    main()
