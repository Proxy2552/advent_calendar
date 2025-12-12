Pour cette énigme du jour 2 du calendrier de l'avent, on devait trouver des fake ID parmi des plages de différentes ID.
Ce qui caractérise un fake ID d'un bon ID est que le fake ID a une suite de nombre qui se répète.
Notre donnée de départ est une liste avec un ID de début de plage et un ID de fin de plage.
Pour trouver ce que l'on cherche, j'ai procédé en deux étapes: étant donné notre liste de départ, j'ai créé une liste avec tout les nombres de la plage à partir du nombre de début et celui de fin.
Ensuite la difficulté principale venait à trouver comment reconnaitre un nombre comme étant un fake ID. Pour celà, j'ai commencé ar mettre une condition pour que le nombre est un nombre de chiffre paire et ensuite je l'ai séparé en deux morceaux que j'ai ensuite comparé et si ces deux morceaux sont identiques, alors ce nombre est un fake ID.
J'effectue donc ces deux fonctions pour chaques plages et je fabrique une liste avec tout les fake ID de chaque plage. 
Je finis par faire la some de tout ces fake ID.