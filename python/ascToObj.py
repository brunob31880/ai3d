import open3d as o3d
import pywavefront
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_file", help="the path to the input file (.asc)")
parser.add_argument("output_file", help="the path to the output file (.obj)")
args = parser.parse_args()

# Chargement du fichier .asc en utilisant open3d
mesh = o3d.io.read_triangle_mesh(args.input_file)

# Conversion en un objet Wavefront en utilisant pywavefront
#py_mesh = pywavefront.Wavefront(args.output_file, strict=True)
#py_mesh.vertices = mesh.vertices
#py_mesh.triangles = mesh.triangles

# Écriture du fichier .obj en utilisant pywavefront
#py_mesh.write()
