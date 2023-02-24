import numpy as np
import open3d as o3d
from plane_detection.color_generator import GenerateColors

def SaveResult(planes):
    pcds = o3d.geometry.PointCloud()
    for plane in planes:
        pcds += plane

    o3d.io.write_point_cloud("data/results/result.ply", pcds)

# Detect planes solely based on RANSAC
def DetectPlanes(filename):
    # Load in point cloud
    print("Loading point cloud...")
    pcd = o3d.io.read_point_cloud(filename)
    planes = []

    # Preprocess the point cloud
    print("Preprocessing point cloud...")
    pcd.voxel_down_sample(voxel_size=0.01)
    pcd.remove_statistical_outlier(nb_neighbors=20, std_ratio=2.0)
    pcd.remove_radius_outlier(nb_points=16, radius=0.05)
    pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))

    # Segment the planes
    print("Segmenting planes...")
    while len(pcd.points) >= 3:
        # Use RANSAC to segment the plane
        plane_model, inliers = pcd.segment_plane(distance_threshold=0.01, ransac_n=3, num_iterations=1000)

        # Extract the inlier points
        inlier_cloud = pcd.select_by_index(inliers)

        # Extract the outlier points
        pcd = pcd.select_by_index(inliers, invert=True)

        # Add the plane to the list of planes
        planes.append(inlier_cloud)

    # Generate random colors for each plane
    colors = GenerateColors(len(planes))

    print("Planes detected: " + str(len(planes)))

    # Loop through each plane and save it to a file
    print("Saving planes...")
    for i, plane in enumerate(planes):
        r = colors[i][0] / 255
        g = colors[i][1] / 255
        b = colors[i][2] / 255

        plane.paint_uniform_color([r, g, b])
        o3d.io.write_point_cloud("data/planes/plane_" + str(i + 1) + ".ply", plane)
    
    # Save the result
    print("Saving result...")
    SaveResult(planes)