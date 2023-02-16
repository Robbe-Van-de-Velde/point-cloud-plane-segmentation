import sys
import os
from plane_detection import DetectPlanes
from plane_to_mesh import PlanesToMeshes
from surface_calculator import CalculateSurfaces
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
            DetectPlanes(filename)
            PlanesToMeshes()
            CalculateSurfaces()
            ViewResult()


    
