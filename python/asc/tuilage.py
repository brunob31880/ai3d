import numpy as np

# Charger le fichier asc
filename = 'nom_du_fichier.asc'
with open(filename, 'r') as f:
    lines = f.readlines()

# Extraire les informations d'en-tête
ncols = int(lines[0].split()[1])
nrows = int(lines[1].split()[1])
xllcorner = float(lines[2].split()[1])
yllcorner = float(lines[3].split()[1])
cellsize = float(lines[4].split()[1])
NODATA_value = float(lines[5].split()[1])

# Convertir les données en tableau numpy
data = np.genfromtxt(lines[6:], dtype=float, delimiter=' ')

# Définir le nombre de tuiles à générer
n = 4  # nombre de tuiles = 2^n

# Calculer la taille de chaque tuile
tile_size = int(nrows / (2 ** n))

# Parcourir le fichier et extraire les valeurs pour chaque tuile
for i in range(2 ** n):
    for j in range(2 ** n):
        # Déterminer les indices de début et de fin pour chaque tuile
        row_start = i * tile_size
        row_end = row_start + tile_size
        col_start = j * tile_size
        col_end = col_start + tile_size
        
        # Extraire les valeurs pour chaque tuile
        tile_data = data[row_start:row_end, col_start:col_end]
        
        # Écrire les valeurs dans un nouveau fichier asc pour chaque tuile
        tile_filename = f'tile_{i}_{j}.asc'
        with open(tile_filename, 'w') as f:
            f.write(f'ncols {tile_size}\n')
            f.write(f'nrows {tile_size}\n')
            f.write(f'xllcorner {xllcorner + col_start * cellsize}\n')
            f.write(f'yllcorner {yllcorner + (nrows - row_end) * cellsize}\n')
            f.write(f'cellsize {cellsize}\n')
            f.write(f'NODATA_value {NODATA_value}\n')
            np.savetxt(f, tile_data, fmt='%.2f', delimiter=' ')
