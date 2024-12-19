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

    paded_frame = np.pad(frame, 1, mode="constant") # je vous offre le code pour le zéro padding c'est cadeau !

    """# Étape 1 : 2 boucles for imbriquées pour parcourir la matrice avec bordure (zero padding) element par element.Faites attention à l'index de début et d'arrêt ! (il s'agit de la matrice avec bordure)

       # L'étape 2 et 3 se font au cours de la même itération (attention à l'indentation !)
    
       # Étape 2 : Pour chacun des éléments, calculez le nombre de voisins.
      On fait appelle à la fonction (compute_number_neighbors)
    
    # Étape 3 : Pour chacun des éléments faire les tests (état de l'élément et son nombre de voisin) afin de voir
    si il y a des modifications à faire.
    Si c'est le cas effectuez les modifications directement dans la matrices frame (Attention à l'indice
    utilisé ! )"""
    
    return frame

while True:
    # boucle infini qui affiche toutes les frames successives (ctrl + c pour arrêter le script)
    print(frame)
    frame = compute_next_frame(frame)
