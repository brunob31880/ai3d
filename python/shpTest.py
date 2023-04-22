import shapefile

# Ouverture du fichier shapefile en lecture seule
sf = shapefile.Reader('../src/datas/BDALTIV/SRC_BDALTIV2_PPK_25M_WGS84G.shx')

# Affichage des informations de la couche (nombre d'enregistrements, type géométrique, etc.)
print("ShapeFile ",sf)
print("Fields ",sf.fields)

# Boucle à travers les enregistrements et affichage des informations de chaque enregistrement
for shape_rec in sf.shapeRecords():
    print("Record=",shape_rec.record)
    print("Shape=",shape_rec.shape.points)
    #print("Points=",shape_rec.shape.points)

# Fermeture du fichier shapefile
sf.close()