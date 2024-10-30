class Tabuleiro:

    _x: int
    _y: int
    _con: list[list[str]]

    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y
        self._con = [
            ['x' for i in range(x*y)]
              for j in range(x*y)]

    def get_num(self, x, y):
        return x + (self._x * y)
    
    def connect(self, x, y, z, w):
        pa = self.get_num(x, y)
        pb = self.get_num(z, w)
        print(pa, pb)
        self._con[pa][pb] = "O"
        self._con[pb][pa] = "O"

    def __str__(self):

        ss = ""

        for i in range(self._x * self._y):
            for j in range (self._x * self._y):
                ss += " " + self._con[i][j]
            ss += "\n"

        return ss
        