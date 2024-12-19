import numpy as np

frame = np.array([[0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 1, 1, 1, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0]])

def compute_number_neighbors(padded_frame, index_line, index_column):

    """Cette fonction prend en entrée la matrice avec bordure etrenvoie le nombre de cellules voisines vivantes."""

    neighbors = 0
    for i in range(index_line-1, index_line+2):
        for j in range(index_column-1, index_column+2):
            if i != index_line or j != index_column:
                neighbors += padded_frame[i, j]
    return neighbors

def compute_next_frame(frame):
    """Cette fonction prend en entrée une frame et calcule la frame suivante à partir des règles du jeu de la vie"""

    padded_frame = np.pad(frame, 1, mode="constant")  # Ajout du padding
    new_frame = np.copy(frame)  # Créer une copie de la matrice pour stocker la prochaine génération

    for i in range(1, padded_frame.shape[0] - 1):  # Parcourir les cellules de la matrice avec padding
        for j in range(1, padded_frame.shape[1] - 1):
            # Calcul du nombre de voisins pour l'élément courant
            neighbors = compute_number_neighbors(padded_frame, i, j)

            # Appliquer les règles du jeu de la vie
            if padded_frame[i, j] == 1:  # La cellule est vivante
                if neighbors < 2 or neighbors > 3:
                    new_frame[i - 1, j - 1] = 0  # La cellule meurt
            elif padded_frame[i, j] == 0:  # La cellule est morte
                if neighbors == 3:
                    new_frame[i - 1, j - 1] = 1  # La cellule devient vivante

    return new_frame

    """# Étape 1 : 2 boucles for imbriquées pour parcourir la matrice avec bordure (zero padding) element par element.Faites attention à l'index de début et d'arrêt ! (il s'agit de la matrice avec bordure)

       # L'étape 2 et 3 se font au cours de la même itération (attention à l'indentation !)
    
       # Étape 2 : Pour chacun des éléments, calculez le nombre de voisins.
      On fait appelle à la fonction (compute_number_neighbors)
    
    # Étape 3 : Pour chacun des éléments faire les tests (état de l'élément et son nombre de voisin) afin de voir
    si il y a des modifications à faire.
    Si c'est le cas effectuez les modifications directement dans la matrices frame (Attention à l'indice
    utilisé ! )"""
    
    

while True:
    # boucle infini qui affiche toutes les frames successives (ctrl + c pour arrêter le script)
    print(frame)
    frame = compute_next_frame(frame)
