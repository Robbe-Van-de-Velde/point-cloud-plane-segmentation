import sys
import os
from plane_detection.plane_detection import DetectPlanes
from plane_detection.plane_to_mesh import PlanesToMeshes
from plane_detection.surface_calculator import CalculateSurfaces
from view_data import ViewPointCloud, ViewMesh, ViewResult

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <file>")
        exit(1)
    else:
        filename = sys.argv[1]
        if not os.path.exists(filename):
            print(f"The file {filename} does not exists")
        else:
            print("Detecting planes...")
            DetectPlanes(filename)

            print("Converting planes to meshes...")
            PlanesToMeshes()

            print("Calculating surface areas...")
            CalculateSurfaces()

            print("Viewing point cloud...")
            ViewResult()


    
