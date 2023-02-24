import open3d as o3d
from scipy.spatial import ConvexHull
import numpy as np
import os
import csv

def CalculateSurfaces():
    results = {}

    # Iterate over all files in directory
    print("Calculating surface areas...")
    for i, filename in enumerate(os.listdir("data/planes")):
        file_path = os.path.join("data/planes", filename)

        # Load pointcloud from file
        pcd = o3d.io.read_point_cloud(file_path)
        points = np.asarray(pcd.points)

        # Compute the surface area
        surface_area = ConvexHull(points, qhull_options='QJ').area / 2

        results[i + 1] = surface_area

    # Write the results to a csv file
    with open("data/results/results.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["Segment", "Surface area"])
        for key, value in results.items():
            writer.writerow([key, value])


# def LegacyCalculateSurfaces():
#     results = {}
#     # Check if directory exists, if not create it
#     if not os.path.exists("meshes"):
#         os.makedirs("meshes")

#     # Iterate over all files in directory
#     for i, filename in enumerate(os.listdir("meshes")):
#         file_path = os.path.join("meshes", filename)

#         if os.path.isfile(file_path):
#             # Load mesh from file
#             mesh = o3d.io.read_triangle_mesh(file_path)

#             # Compute the surface area
#             surface_area = mesh.get_surface_area()

#             results[i + 1] = surface_area

#     if not os.path.exists("results"):
#             os.makedirs("results")

#     # Write the results to a csv file
#     with open("results/results.csv", "w") as f:
#         writer = csv.writer(f)
#         writer.writerow(["Plane", "Surface area"])
#         for key, value in results.items():
#             writer.writerow([key, value])
