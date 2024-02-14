

from src.Utils.Config import Config
from src.OEMS import OEMS
from src.OAMS import OAMS
from src.OPMS import OPMS

from src.OES import OES
from src.OAS import OAS
from src.OPS import OPS

from src.Decorator.TimerCMD import Timer

@Timer.timer()
def main_test_analysis(folder : str) -> None:

    Images = {
        r"Codes\Data\Images\Cup - 29 25 41_Matrix.txt": [29, 25, 41],
        r"Codes\Data\Images\Dragon - 42 64 90_Matrix.txt": [42, 64, 90],
        r"Codes\Data\Images\Sphere0 65 65 31_Matrix.txt": [65, 65, 31],
        r"Codes\Data\Images\Sphere2 65 65 31_Matrix.txt": [65, 65, 31],
        r"Codes\Data\Images\Sphere3 65 65 31_Matrix.txt": [65, 65, 31],
        r"Codes\Data\Images\Sphere5 65 65 31_Matrix.txt": [65, 65, 31],
        r"Codes\Data\Images\Torus 67 65 10_Matrix.txt": [67, 65, 10],
        r"Codes\Data\Images\Torush 67 65 10_Matrix.txt": [67, 65, 10],
        r"Codes\Data\Images\Vase 69 53 41_Matrix.txt": [69, 53, 41],
        r"Codes\Data\Images\Object1 6 5 5_Matrix.txt": [6, 5, 5],
        r"Codes\Data\Images\Object2 7 10 9_Matrix.txt": [7, 10, 9]
    }

    # * Iterate over each entry in the dictionary
    for File_path, Dimensions in Images.items():

        Dimensions[0] = (Dimensions[0] + 2);
        Dimensions[1] = (Dimensions[1] + 2);
        Dimensions[2] = (Dimensions[2] + 2);

        Test_Octovoxels = OAMS(File_path, folder);
        Result = Test_Octovoxels.get_array(Dimensions[0], Dimensions[1], Dimensions[2]);

        Test_Octovoxels = OAS(File_path, folder);
        Result = Test_Octovoxels.get_array(Dimensions[0], Dimensions[1], Dimensions[2]);

        Test_Octovoxels = OPMS(File_path, folder);
        Result = Test_Octovoxels.get_array(Dimensions[0], Dimensions[1], Dimensions[2]);

        Test_Octovoxels = OPS(File_path, folder);
        Result = Test_Octovoxels.get_array(Dimensions[0], Dimensions[1], Dimensions[2]);

        Test_Octovoxels = OEMS(File_path, folder);
        Result = Test_Octovoxels.get_array(Dimensions[0], Dimensions[1], Dimensions[2]);

        Test_Octovoxels = OES(File_path, folder);
        Result = Test_Octovoxels.get_array(Dimensions[0], Dimensions[1], Dimensions[2]);

if __name__ == "__main__":
    main_test_analysis(Config.Folder_data);

    