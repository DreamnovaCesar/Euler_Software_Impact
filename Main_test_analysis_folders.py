

from src.Utils.Config import Config
from src.Utils.Utils import save_to_csv

from src.OCSMM import OCSMM

from src.OEMM import OEMM

from src.OESMM import OESMM

from src.OVMM import OVMM

from src.Decorator.TimerCMD import Timer

@Timer.timer("Execution_main_test_analysis_folders.log")
def main_test_analysis_folders(Folder : str) -> None:

    Images = {
        Config.Folder_3D_matrix_4: [4, 4, 4],
        Config.Folder_3D_matrix_8: [8, 8, 8],
        Config.Folder_3D_matrix_16: [16, 16, 16],
        Config.Folder_3D_matrix_32: [32, 32, 32]
    }

    # * Iterate over each entry in the dictionary
    for File_path, Dimensions in Images.items():

        Dimensions[0] = (Dimensions[0] + 2);
        Dimensions[1] = (Dimensions[1] + 2);
        Dimensions[2] = (Dimensions[2] + 2);

        Test_Octovoxels = OCSMM(File_path);
        Combinations, Descriptor, Descriptor_name = Test_Octovoxels.get_array(Dimensions[0], Dimensions[1], Dimensions[2]);
        save_to_csv(Folder, File_path, Descriptor_name, Combinations, Descriptor);

        Test_Octovoxels = OEMM(File_path);
        Combinations, Descriptor, Descriptor_name = Test_Octovoxels.get_array(Dimensions[0], Dimensions[1], Dimensions[2]);
        save_to_csv(Folder, File_path, Descriptor_name, Combinations, Descriptor);

        Test_Octovoxels = OESMM(File_path);
        Combinations, Descriptor, Descriptor_name = Test_Octovoxels.get_array(Dimensions[0], Dimensions[1], Dimensions[2]);
        save_to_csv(Folder, File_path, Descriptor_name, Combinations, Descriptor);

        Test_Octovoxels = OVMM(File_path);
        Combinations, Descriptor, Descriptor_name = Test_Octovoxels.get_array(Dimensions[0], Dimensions[1], Dimensions[2]);
        save_to_csv(Folder, File_path, Descriptor_name, Combinations, Descriptor);

if __name__ == "__main__":
    main_test_analysis_folders(Config.Folder_data);

    