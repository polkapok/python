# -*-coding:utf-8 -*

"""module decomposer contenant la fonction entier_reste"""

import os

""""Cette fonction retourne la partie entière et le reste de entier / divise_par"""
def entier_reste(entier, divise_par):
	p_e = entier // divise_par
	reste = entier % divise_par
	#return p_e, reste
	print(p_e, reste)

# test de la fonction entier_reste
if __name__ == "__main__":
    entier_reste(25, 3)
    os.system("pause")