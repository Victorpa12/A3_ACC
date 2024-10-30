from sys import argv
from tabuleiro import Tabuleiro
def main(args):
    x = args [1]
    y = args [2]
    tab = Tabuleiro (int (x), int (y))
    tab.connect(4,3, 3,3)
    tab.connect(2,1, 1,2)

    print(tab)

    for j in range(int(y)):
        for i in range(int(x)):
            print(i, j, "==>", tab.get_num(i,j))


main(argv)

#o shazam da o cu(><//__//><)