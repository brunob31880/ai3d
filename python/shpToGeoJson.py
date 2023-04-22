import shapefile
import json
import sys

def read_shapefile(ficURL):
    # Ouvrir le fichier shapefile
    sf = shapefile.Reader(ficURL)

    # Récupérer les enregistrements (records) et les champs (fields) du shapefile
    records = sf.records()
    #print(len(records))
    fields = sf.fields[1:]
    #print(fields)
    # Créer la liste des features GeoJSON
    features = []
    for record in records:
        # Créer une feature pour chaque enregistrement (record)
        feature = {'type': 'Feature', 'properties': {}, 'geometry': {'type': 'Point', 'coordinates': []}}
        for i, field in enumerate(fields):
            # Ajouter les propriétés de chaque champ (field) à la feature
            feature['properties'][field[0]] = record[i]
        # Ajouter les coordonnées à la feature   
        shape = sf.shapeRecord(record).shape
        print("SHAPE TYPE =",shape.type)
        feature['geometry']['coordinates'] = [shape.points[0][0], shape.points[0][1]]
        # Ajouter la feature à la liste des features
        features.append(feature)

    # Créer le dictionnaire GeoJSON avec la liste des features
    geojson = {'type': 'FeatureCollection', 'features': features}

    # Écrire le fichier GeoJSON
    with open('fichier.geojson', 'w') as f:
        json.dump(geojson, f)


if __name__ == '__main__':
    #le premier argument passé est le chemin vers le fichier shapefile
    if len(sys.argv) > 1:
        print('Le chemin vers le fichier shapefile est '+sys.argv[1])
        read_shapefile(sys.argv[1])
    