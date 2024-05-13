

from src.Utils.Config import Config
from src.Utils.Utils import save_to_csv

from src.OCSC import OCSC
from src.OCSS import OCSS

from src.OEC import OEC
from src.OES import OES

from src.OESC import OESC
from src.OESS import OESS

from src.OVC import OVC
from src.OVS import OVS

#from src.Test_OES import Test_OES
from src.Decorator.TimerCMD import Timer

@Timer.timer("Execution_main_test_analysis.log")
def main_test_analysis(Folder : str) -> None:

    Images = {
        r'src\Data\Images\1.- Object1_6_5_5_Matrix.txt' : [6, 5, 5],
        r'src\Data\Images\1.- Object2_7_10_9_Matrix.txt' : [7, 10, 9],
        r'src\Data\Images\1.- Cup_29_25_41_Matrix.txt' : [29, 25, 41],
        r'src\Data\Images\1.- Dragon_42_64_90_Matrix.txt' : [42, 64, 90],
        r'src\Data\Images\1.- Sphere0_65_65_31_Matrix.txt' : [65, 65, 31],
        r'src\Data\Images\1.- Sphere2_65_65_31_Matrix.txt' : [65, 65, 31],
        r'src\Data\Images\1.- Sphere3_65_65_31_Matrix.txt' : [65, 65, 31],
        r'src\Data\Images\1.- Sphere5_65_65_31_Matrix.txt' : [65, 65, 31],
        r'src\Data\Images\1.- Torus_67_65_10_Matrix.txt' : [67, 65, 10],
        r'src\Data\Images\1.- Torush_67_65_10_Matrix.txt' : [67, 65, 10],
        r'src\Data\Images\1.- Vase_69_53_41_Matrix.txt' : [69, 53, 41],
        r'src\Data\Images\1.- Cheese_102_102_102_Matrix.txt' : [102, 102, 102],
        r'src\Data\Images\2.- Ardilla_128_128_128_Matrix.txt' : [128, 128, 128],
        r'src\Data\Images\3.- Ajolote_256_256_256_Matrix.txt' : [256, 256, 256],
        #r'src\Data\Images\5.- Esfera_512_512_512_Matrix.txt' : [512, 512, 512]
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

    