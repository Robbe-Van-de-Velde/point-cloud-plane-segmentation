import os
from plane_detection.plane_detection import DetectPlanes
from plane_detection.surface_calculator import CalculateSurfaces
from view_data import ViewPointCloud, ViewMesh, ViewResult



def SegmentPointCloud(filename):
    # Check if the file exists
    print("Checking if the file exists...")
    if not os.path.exists(filename):
        print(f"The file {filename} does not exists")
        exit(1)

    print("Preparing project...")

    # Make the necessary directories
    print("Making the necessary directories...")
    if not os.path.exists("data/planes"):
        os.makedirs("data/planes")
    if not os.path.exists("data/results"):
        os.makedirs("data/results")

    print("Detecting planes...")
    DetectPlanes(filename)

    print("Calculating surface areas...")
    CalculateSurfaces()

    print("Viewing point cloud...")
    ViewResult()
