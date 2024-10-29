from sys import argv
from tabuleiro import Tabuleiro
def main(args):
    x = args [1]
    y = args [2]
    tab = Tabuleiro (int (x), int (y))
    tab.connect(4, 3)
    print(tab)

main(argv)