# -*-coding:utf-8 -*

"""fichier testant la fonction afficher_flottant"""

import os

#C:\Users\Bacchus\www\python\packages\modules\module_de_test

from packages.modules.module_de_test.fonctions_diverses import afficher_flottant

# On attend que l'utilisateur saisisse le nombre flottant qu'il désire tester
flotteur = input("Saisissez un nombre flottant : ") 

# test de la fonction afficher_flottant
#test = afficher_flottant(285.32587416722)
test = afficher_flottant(flotteur)

print(test)

os.system("pause")

