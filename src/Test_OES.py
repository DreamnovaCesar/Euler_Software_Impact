import os
import numpy as np
import pandas as pd

from src.Utils.Config import Config
from src.Utils.DataLoader import DataLoader
from src.Utils.Utils import count_combinations

from src.Decorator.TimerCMD import Timer
from src.Decorator.multiprocessing_info import multiprocessing_info

from typing import Optional, Union, List

from src.Test_DM import DM

class Test_OES(DM):
    """
    Q_values denote the spatial extent of each identified pattern within the 3D image.
    Octo-Voxel Euler Simplified (OES) - A class developed especially for processing Octo-Voxels that uses a simplified 
    method lacking of multiprocessing or the CHUNKS technique.

    Attributes:
    -----------
    Path : str
        The file path for data and convert it into an array.
    Basepath : str
        The base name of the file path.
    Folder : bool
        Flag indicating whether the path is a directory.
    STORAGELIST : np.ndarray
        An array of binary values derived from the ByteStorage.

    Methods:
    --------
    save_to_csv(Combinations_data: Union[np.ndarray, list], Euler_data: Union[np.ndarray, list]) -> None:
        Save the combinations and Euler values to a CSV file.

    get_array(Depth: int, Height: int, Width: int) -> Union[np.ndarray, list]:
        Calculate Combinations_int based on the given STORAGELIST and return them as a numpy array.

    Notes:
    ------
    This class provides methods for processing octovoxel data and calculating Combinations_int based on a given STORAGELIST.

    Examples:
    ---------
    >>> File_path = "data.csv"
    >>> Handler = OES(File_path)
    >>> Result_combinations, Result_euler = Handler.get_array(Depth=3, Height=3, Width=3)
    """
    def __init__(self, 
                 path: str
        ) -> None:
        """
        Initialize OES.

        Parameters:
        ----------
        path : str
            The file path for data and convert it into an array.

        """
        super().__init__(path, None)
        self.Descriptor = "Euler";
    
    # * Class description
    def __str__(self) -> str:
        """
        Return a string description of the object.

        Returns:
        ----------
        None
        """
        return f'''{self.__class__.__name__}: A class for handling Octo-Voxels and obtaining q_values based on the given Storage_list.''';

    # * Deleting (Calling destructor)
    def __del__(self) -> None:
        """
        Destructor called when the object is deleted.

        Returns:
        ----------
        None
        """
        print(f'Destructor called, {self.__class__.__name__} class destroyed.');
    
    def process_octovoxel(self, 
                          File : str, 
                          STORAGELIST : List[np.ndarray], 
                          Depth : int, 
                          Height : int, 
                          Width : int
                          ):
        """
        Calculate Combinations_int based on the given Storage_list and return them as a numpy array.

        Parameters:
        -----------
        File : str
            The name of the file being processed.
        STORAGELIST : List[np.ndarray]
            List of numpy array representations of the binary storage list.
        Depth : int
            The depth dimension of the 3D array.
        Height : int
            The height dimension of the 3D array.
        Width : int
            The width dimension of the 3D array.

        Returns:
        -------
        Tuple[np.ndarray, int]
            A tuple containing an array of Combinations_int and Euler value.

        Notes:
        ------
        - Octovoxel size is set to 2.
        - Euler value is the sum of Combinations_int.
        """

        Arrays = DataLoader.load_data(File)
        
        # * Reshape the array to a 3D array based on the calculated height.
        Arrays = Arrays.reshape(Depth, Height, Width)
        
        # * Create sliding windows for CHUNK for faster access to sub-volumes
        view_CHUNK_2x2x1 = np.lib.stride_tricks.sliding_window_view(Arrays, (Config.Octovoxel_size, Config.Octovoxel_size, 1));
        view_CHUNK_2x1x2 = np.lib.stride_tricks.sliding_window_view(Arrays, (Config.Octovoxel_size, 1, Config.Octovoxel_size));
        view_CHUNK_1x2x2 = np.lib.stride_tricks.sliding_window_view(Arrays, (1, Config.Octovoxel_size, Config.Octovoxel_size));

        # * Resize sliding windows to 1x2x2
        view_CHUNK_2x2x1_resized = view_CHUNK_2x2x1.reshape(-1, 1, Config.Octovoxel_size, Config.Octovoxel_size);
        view_CHUNK_2x1x2_resized = view_CHUNK_2x1x2.reshape(-1, 1, Config.Octovoxel_size, Config.Octovoxel_size);
        # * Convert STORAGELIST to a single numpy array for vectorized comparisons
        STORAGELIST_array = np.array(STORAGELIST)

        # * Count combinations for each sliding window
        Combinations_int_1 = count_combinations([[view_CHUNK_2x2x1_resized]], STORAGELIST_array)
        Combinations_int_2 = count_combinations([[view_CHUNK_2x1x2_resized]], STORAGELIST_array)
        Combinations_int_3 = count_combinations(view_CHUNK_1x2x2, STORAGELIST_array)

        # * Concatenate the three Combinations_int arrays along axis 0, excluding the first value from each
        Concatenated_combinations = np.concatenate([Combinations_int_1[1:], Combinations_int_2[1:], Combinations_int_3[1:]], axis=0)

        return Concatenated_combinations

    @Timer.timer()
    @multiprocessing_info 
    def get_array(self, Depth : int, Height : int, Width : int) -> Union[np.ndarray, list]:
        """
        Calculate Combinations_int based on the given self.STORAGELIST and return them as a numpy array.

        Returns:
        -------
        np.ndarray
            An array of Combinations_int.

        Notes:
        ------
        - Octovoxel size is set to 2.
        - The method calculates Combinations_int by comparing octovoxel patters with elements in `self.STORAGELIST`.

        """
        try:

            if(self.Folder):
                
                Combinations_all = [];
                Euler_all = [];

                # * Filter the list to include only .txt files
                Files = os.listdir(self.Path);
                
                print(f"Processing file... Total : {Files}");

                for i, File in enumerate(Files):
                    
                    print(f"Processing file...");

                    File_path = os.path.join(self.Path, File);
                    print(f"{i} ---- {File_path}");

                    if(Depth != None and Height != None and Width != None):
                
                        Combinations = self.process_octovoxel(File_path, self.STORAGELIST, Depth, Height, Width);

                        # * Return the calculated Combinations_int as a numpy array.
                    
                    Combinations_all.append(Combinations);
                    Euler_all.append(None);

                return Combinations_all, Euler_all, self.Descriptor 
            
            else:

                if(Depth != None and Height != None and Width != None):

                        print(f"Processing file...");

                        Combinations = self.process_octovoxel(self.Path, self.STORAGELIST, Depth, Height, Width);
                        
                        # * Return the calculated Combinations_int as a numpy array.
                        #Combinations_euler = (Combinations * Config._OUTPUT_3D_);
                    
                        Euler = np.sum(None);

                        return Combinations, Euler, self.Descriptor 
            
        except Exception as e:
            # * You can also choose to return a default value or handle the exception differently.
            print(f"An error occurred processing Octovoxel: {e}")
