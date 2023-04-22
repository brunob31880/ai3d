import shapefile
import json

# Ouvrir le fichier shapefile
sf = shapefile.Reader('chemin/vers/fichier.shp')

# Récupérer les enregistrements (records) et les champs (fields) du shapefile
records = sf.records()
fields = sf.fields[1:]

# Créer la liste des features GeoJSON
features = []
for record in records:
    # Créer une feature pour chaque enregistrement (record)
    feature = {'type': 'Feature', 'properties': {}, 'geometry': {'type': '', 'coordinates': []}}
    for i, field in enumerate(fields):
        # Ajouter les propriétés de chaque champ (field) à la feature
        feature['properties'][field[0]] = record[i]
    # Ajouter les coordonnées à la feature
    shape = sf.shapeRecord(record).shape
    if shape.shapeType == shapefile.POINT:
        feature['geometry']['type'] = 'Point'
        feature['geometry']['coordinates'] = [shape.points[0][0], shape.points[0][1]]
    elif shape.shapeType == shapefile.POLYLINE:
        feature['geometry']['type'] = 'LineString'
        feature['geometry']['coordinates'] = [list(coord) for coord in shape.points]
    elif shape.shapeType == shapefile.POLYGON:
        feature['geometry']['type'] = 'Polygon'
        feature['geometry']['coordinates'] = [[[coord[0], coord[1]] for coord in part] for part in shape.parts]
    # Ajouter la feature à la liste des features
    features.append(feature)

# Créer le dictionnaire GeoJSON avec la liste des features
geojson = {'type': 'FeatureCollection', 'features': features}

# Écrire le fichier GeoJSON
with open('chemin/vers/fichier.geojson', 'w') as f:
    json.dump(geojson, f)
