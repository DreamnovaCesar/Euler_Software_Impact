

from src.Utils.Config import Config
from src.Utils.Utils import save_to_csv

from src.OCSC import OCSC
from src.OCSMM import OCSMM
from src.OCSS import OCSS

from src.OEC import OEC
from src.OEMM import OEMM
from src.OES import OES

from src.OESC import OESC
from src.OESMM import OESMM
from src.OESS import OESS

from src.OVC import OVC
from src.OVMM import OVMM
from src.OVS import OVS

from src.Decorator.TimerCMD import Timer

@Timer.timer()
def main_test_analysis(Folder : str) -> None:

    Images = {
        Config.Folder_3D_matrix_4: [4, 4, 4],
        Config.Folder_3D_matrix_8: [4, 4, 4],
        Config.Folder_3D_matrix_16: [4, 4, 4],
        Config.Folder_3D_matrix_32: [4, 4, 4]
    }

    # * Iterate over each entry in the dictionary
    for File_path, Dimensions in Images.items():

        Dimensions[0] = (Dimensions[0] + 2);
        Dimensions[1] = (Dimensions[1] + 2);
        Dimensions[2] = (Dimensions[2] + 2);

        Test_Octovoxels = OCSC(File_path);
        Combinations, Descriptor, Descriptor_name = Test_Octovoxels.get_array(Dimensions[0], Dimensions[1], Dimensions[2]);
        save_to_csv(Folder, File_path, Descriptor_name, Combinations, Descriptor);

        Test_Octovoxels = OCSS(File_path);
        Combinations, Descriptor, Descriptor_name = Test_Octovoxels.get_array(Dimensions[0], Dimensions[1], Dimensions[2]);
        save_to_csv(Folder, File_path, Descriptor_name, Combinations, Descriptor);

        Test_Octovoxels = OVC(File_path);
        Combinations, Descriptor, Descriptor_name = Test_Octovoxels.get_array(Dimensions[0], Dimensions[1], Dimensions[2]);
        save_to_csv(Folder, File_path, Descriptor_name, Combinations, Descriptor);

        Test_Octovoxels = OVS(File_path);
        Combinations, Descriptor, Descriptor_name = Test_Octovoxels.get_array(Dimensions[0], Dimensions[1], Dimensions[2]);
        save_to_csv(Folder, File_path, Descriptor_name, Combinations, Descriptor);

        Test_Octovoxels = OESC(File_path);
        Combinations, Descriptor, Descriptor_name = Test_Octovoxels.get_array(Dimensions[0], Dimensions[1], Dimensions[2]);
        save_to_csv(Folder, File_path, Descriptor_name, Combinations, Descriptor);

        Test_Octovoxels = OESS(File_path);
        Combinations, Descriptor, Descriptor_name = Test_Octovoxels.get_array(Dimensions[0], Dimensions[1], Dimensions[2]);
        save_to_csv(Folder, File_path, Descriptor_name, Combinations, Descriptor);

        Test_Octovoxels = OEC(File_path);
        Combinations, Descriptor, Descriptor_name = Test_Octovoxels.get_array(Dimensions[0], Dimensions[1], Dimensions[2]);
        save_to_csv(Folder, File_path, Descriptor_name, Combinations, Descriptor);

        Test_Octovoxels = OES(File_path);
        Combinations, Descriptor, Descriptor_name = Test_Octovoxels.get_array(Dimensions[0], Dimensions[1], Dimensions[2]);
        save_to_csv(Folder, File_path, Descriptor_name, Combinations, Descriptor);

if __name__ == "__main__":
    main_test_analysis(Config.Folder_data);

    