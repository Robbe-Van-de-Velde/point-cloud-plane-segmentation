import open3d as o3d
import os

def PlanesToMeshes():
    # Check if directory exists, if not create it
    if not os.path.exists("planes"):
        os.makedirs("planes")

    # Iterate over all files in directory
    for filename in os.listdir("planes"):
        file_path = os.path.join("planes", filename)
        mesh_file = filename.replace("plane", "mesh")
        if os.path.isfile(file_path):
            print(f"Converting {filename} to mesh...")

            # Load point cloud from file
            pcd = o3d.io.read_point_cloud(file_path)

            # Estimate normals for the point cloud
            pcd.estimate_normals()

            # Create a mesh from the point cloud, with ball pivoting
            radii = [0.005, 0.01, 0.02, 0.04]
            rec_mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(
                pcd, o3d.utility.DoubleVector(radii))

            # Write the mesh to file
            if not os.path.exists("meshes"):
                os.makedirs("meshes")

            o3d.io.write_triangle_mesh(os.path.join("meshes", mesh_file), rec_mesh)

    print("Successfully converted planes to meshes.")