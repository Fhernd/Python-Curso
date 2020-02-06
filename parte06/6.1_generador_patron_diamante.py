import plac
# Generador de patrón diamante

#     #
#    ###
#   #####
#  #######
# #########
#  #######
#   #####
#    ###
#     #

def generador_patron_diamente(filas=6, simbolo='#'):
    "Imprime un patrón tipo diamante a partir de cierta cantidad de filas y un símbolo específico."

    filas = 9

    for i in range(1, filas + 1):
        i = i - (filas//2 +1)
        if i < 0:
            i = -i
        print(" " * i + simbolo * (filas - i*2) + " "*i)
    
if __name__ == "__main__":
    plac.call(generador_patron_diamente)
    # plac es una alternativa a argparse