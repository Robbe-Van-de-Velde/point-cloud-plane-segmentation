import open3d as o3d

def ViewMesh(filename):
    mesh = o3d.io.read_triangle_mesh(filename)
    print(mesh)
    o3d.visualization.draw_geometries([mesh])

def ViewPointCloud(filename):
    pcd = o3d.io.read_point_cloud(filename)
    o3d.visualization.draw_geometries([pcd])

def ViewResult():
    filename = "results/result-classified.ply"
    ViewPointCloud(filename)

if __name__ == "__main__":
    ViewPointCloud("data/test1.ply")