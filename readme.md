🎄Calendrier de l'Avent - Jour 2 : Identification des Fake IDs
Ce projet résout l'énigme du Jour 2, qui consiste à trouver la somme totale des ID de produits invalides à l'intérieur de plusieurs plages numériques.

Notre donnée de départ est une liste de bornes d'intervalles : [début1, fin1, début2, fin2, ...].



1️⃣ Partie 1 : Répétition Exactement Deux Fois

🔍 Règle du Fake ID

Un ID est invalide s'il est composé d'une séquence de chiffres ($M$) répétée exactement deux fois ($MM$).

Exemples : $55$, $6464$, $123123$.


🛠️ Méthode

1. Génération des Nombres : Pour chaque plage [A, B], on crée une liste contenant tous les nombres entre $A$ et $B$ (fonction intervale).

2. Détection (fake_id1) : Pour chaque nombre, on vérifie :
- Il doit avoir un nombre pair de chiffres.
- On le divise en deux moitiés égales. Si la première moitié = la deuxième moitié, c'est un Fake ID.

3.Calcul : On somme tous les Fake IDs trouvés dans l'ensemble des plages.



2️⃣ Partie 2 : Répétition Au Moins Deux Fois

🔍 Nouvelle Règle du Fake ID

Un ID est invalide s'il est composé d'une séquence de chiffres ($M$) répétée au moins deux fois ($MM$, $MMM$, $MMMM$, etc.).

Exemples : $12341234$, $123123123$, $1111111$.


🛠️ Méthode

La première étape de génération des nombres est conservée. Seule la détection change (fake_id2).

1. Détection (fake_id2) : Pour chaque ID analysé, on cherche si une sous-séquence $M$ peut le reconstituer par répétition.

2. Vérification par Diviseur : On teste toutes les longueurs de séquence ($k$) possibles, où $k$ est un diviseur de la longueur totale de l'ID ($L$), à condition que $k$ soit inférieur ou égal à $L/2$ (ce qui garantit au moins deux répétitions).

3. Validation : Si l'ID est égal à la sous-séquence $M$ répétée $R$ fois ($R = L/k$), il est marqué comme Fake ID.



📈 Résultat

On effectue ensuite la somme de tous les nouveaux Fake IDs identifiés.
