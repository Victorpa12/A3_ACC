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

    def connect(self, x, y, z ,w):
        pa = self.get_num(x, y)
        pb = self.get_num(z, w)
        #print(pa, pb)
        self._con[pa][pb] = "O"
        self._con[pb][pa] = "O"

    def verifica_quadrados(self):
        for i in range(self._x -1):
            for j in range(self._y -1):
                
                cons = 0

                # esq-cima e dir-cima
                ni = self.get_num(i, j)
                nj = self.get_num(i + 1, j)

                if self._con[ni][nj] == 'O':
                    cons = cons + 1

                # dir-cima e dir-baixo
                ni = self.get_num(i + 1, j)
                nj = self.get_num(i + 1, j + 1)
                
                if self._con[ni][nj] == 'O':
                    cons = cons + 1

                # dir-baixo e esq-baixo
                ni = self.get_num(i + 1, j + 1)
                nj = self.get_num(i, j + 1)
                
                if self._con[ni][nj] == 'O':
                    cons = cons + 1

                # esq-baixo e esq-cima
                ni = self.get_num(i, j + 1)
                nj = self.get_num(i, j)
                
                if self._con[ni][nj] == 'O':
                    cons = cons + 1

                if cons == 4:
                    print(f"({i}, {j}), ({i+1}, {j}), " +
                          f"({i+1}, {j+1}), ({i}, {j+1})")

    def mostra_tabuleiro(self):

        linha = 0

        while(linha != self._y):

            #########
            for i in range(self._x -2):

                pa = self.get_num(linha, i)
                pb = self.get_num(linha, i+1)

                # print(linha, i, linha, i+1)
                # print(pa, pb)

                if self._con[pa][pb] == 'O':
                    print(".__", end="")
                else:
                    print(".  ", end="")
            print('.')

            #########
            for i in range(self._x -1):

                pa = self.get_num(linha, i)
                pb = self.get_num(linha + 1, i)
                if self._con[pa][pb] == 'O':
                    print("|  ", end="")
                else:
                    print("   ", end="")

            print('\n', end='')
            linha += 1
        print(''.join(['.  ' for i in range(self._x -1)]))
            
                


    def __str__(self):
        ss = ""
        for i in range(self._x * self._y):
            for j in range(self._x * self._y):
                ss += " " + self._con[i][j]
            ss += "\n"
        return ss