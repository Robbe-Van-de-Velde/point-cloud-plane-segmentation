import open3d as o3d
import sys

def ConvertMeshToPointCloud(filename):
    mesh = o3d.io.read_triangle_mesh(filename)
    pcd = mesh.sample_points_poisson_disk(32768)
    o3d.io.write_point_cloud("data/point_cloud.ply", pcd)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python mesh_to_point_cloud.py <file>")
        exit(1)
    else:
        filename = sys.argv[1]
        ConvertMeshToPointCloud(filename)