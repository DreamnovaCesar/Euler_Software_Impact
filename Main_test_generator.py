from src.Utils.Config import Config
from src.VoxelGenerator import VoxelGenerator

def main_test_generator():
    
    Voxel_generator = VoxelGenerator(path = Config.Folder_3D_matrix_4 , depth = 4, width = 4, height = 4, num_matrices = 1000);
    Voxel_generator.generate_matrices();

    Voxel_generator = VoxelGenerator(path = Config.Folder_3D_matrix_8 , depth = 8, width = 8, height = 8, num_matrices = 1000);
    Voxel_generator.generate_matrices();

    Voxel_generator = VoxelGenerator(path = Config.Folder_3D_matrix_16 , depth = 16, width = 16, height = 16, num_matrices = 1000);
    Voxel_generator.generate_matrices();

    Voxel_generator = VoxelGenerator(path = Config.Folder_3D_matrix_32, depth = 32, width = 32, height = 32, num_matrices = 1000);
    Voxel_generator.generate_matrices();

    Voxel_generator = VoxelGenerator(path = Config.Folder_3D_matrix_64, depth = 64, width = 64, height = 64, num_matrices = 1000);
    Voxel_generator.generate_matrices();

if __name__ == "__main__":
    main_test_generator();

    