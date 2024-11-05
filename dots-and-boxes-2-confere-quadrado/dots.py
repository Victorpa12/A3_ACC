from sys import argv
from tabuleiro import Tabuleiro

def main(args):
    x = args[1]
    y = args[2]
    tab = Tabuleiro(int(x), int(y))
    
    tab.connect(2,2,  2,3)
    tab.connect(2,3,  3,3)
    tab.connect(3,3,  3,2)
    tab.connect(3,2,  2,2)
    
    tab.verifica_quadrados()
    #print(tab)

    # for j in range(int(y)):
    #     for i in range(int(x)):        
    #         print(i, j, "==>", tab.get_num(i, j))

    tab.mostra_tabuleiro()

main(argv)