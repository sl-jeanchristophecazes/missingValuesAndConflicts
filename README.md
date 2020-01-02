# missingValuesAndConflicts


## missingValues.py
Quelques fonction utiles pour voir les valeurs manquantes dans un tableau pandas d'une part.

Permet d'obtenir la liste des colonnes qui contiennent des valeurs nan / inf / -inf .

Permet d'obtenir la liste des valeurs pour chacune des colonnes .

## conflictingValues.py
D'autre part, on peut aussi voir les colonnes ayant des conflits de typage. 

Ainsi la fonction conflictingDataTypes renvoie pour chaque colonne la liste des différents types présents et les conflicts.

Par exemple, une colonne qui contient a la fois des str et des floats .