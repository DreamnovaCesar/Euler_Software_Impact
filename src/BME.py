import os
import numpy as np
import pandas as pd

from src.Utils.Config import Config
from src.Utils.DataLoader import DataLoader
from src.Utils.NibbleStorage import NibbleStorage

from src.Decorator.TimerCMD import Timer
from src.Decorator.multiprocessing_info import multiprocessing_info

from src.DM import DM
from typing import Optional, Union, List, Tuple

class BME(DM):
    """
    Bit-Quads analysis is employed for calculating the Euler characteristic of binary images.
    Bit-Quads Multi Euler (BME) - A class for Bit-Quads and obtaining Q_values based on the given NibbleStorage 

    Attributes:
    -----------
    Path : str
        The file path for data and convert it into an array.
    Connectivity : int
        Connectivity value.

    Methods:
    --------
    get_array() -> np.ndarray:
        Calculate Combinations_int based on the given Storage_list and return them as a numpy array.

    Notes:
    ------
    This class provides methods for processing octovoxel data and calculating Combinations_int based on a given Storage_list.

    Examples:
    ---------

    """
    def __init__(self, 
                 path: str,
                 connectivity : int = 8
        ) -> None:
        """
        Initialize ME.

        Parameters:
        ----------
        path : str
            The file path for data and convert it into an array.
        Connectivity : int
        Connectivity value.

        """

        super().__init__(path, None, None)

        self.Connectivity = connectivity;

        self.SLC = NibbleStorage;
        self.STORAGELIST = self.SLC.to_numpy_array();

        if(self.Connectivity == 4):
            self._CONNECTIVITY_ = Config._OUTPUT_2D_4_;
            self._C_ = "C4";
        elif(self.Connectivity == 8):
            self._CONNECTIVITY_ = Config._OUTPUT_2D_8_;
            self._C_ = "C8";
        else:
            raise ValueError("Invalid connectivity value. Supported values are 4 or 8.");

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

    #@Timer.timer()
    def process_octovoxel(self, 
                          File : str, 
                          STORAGELIST : List[np.ndarray], 
                          Depth : int, 
                          Height : int, 
                          Width : int) -> Tuple[np.ndarray, int]:
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

        Combinations = int(Config.Byte_binary, 2);
        
        # * Create an array to store Combinations_int and initialize it with zeros.
        Combinations_int = np.zeros((Combinations), dtype='int');
        
        File_path = os.path.join(self.Path, File);
        Arrays = DataLoader.load_data(File_path);

        # * Reshape the array to a 3D array based on the calculated height.
        Arrays = Arrays.reshape(Height, Width);
        
        # * Create sliding windows for CHUNK for faster access to sub-volumes
        VIEW_CHUNK = np.lib.stride_tricks.sliding_window_view(Arrays, (Config.Bitquads_size, Config.Bitquads_size));
        
        # * Convert STORAGELIST to a single numpy array for vectorized comparisons
        STORAGELIST_array = np.array(STORAGELIST);
        
        # * Vectorized comparison and counting
        for index in range(len(STORAGELIST)):
            Equal_mask = (VIEW_CHUNK == STORAGELIST_array[index]).all(axis=(3, 4, 5));
            Combinations_int[index] += Equal_mask.sum();

        # * Return the calculated Combinations_int as a numpy array.
        Combinations = (Combinations_int * Config._OUTPUT_2D_8_);
        Euler = np.sum(Combinations);

        print(f"Processing file... {File_path} ----------- {Euler}");

        return Combinations_int, Euler
    
    @Timer.timer("Execution_BME.log")
    @multiprocessing_info   
    def get_array(self, Height : int, Width : int) -> np.ndarray:
        """
        Calculate Combinations_int based on the given Storage_list and return them as a numpy array.

        Returns:
        -------
        np.ndarray
            An array of Combinations_int.

        """
        try:

            if(self.Folder):
                
                Combinations_all = [];
                Euler_all = [];

                # * Filter the list to include only .txt files
                Files = os.listdir(self.Path);
                
                print(f"Processing file... Total : {len(Files)}");

                for i, File in enumerate(Files):
                    
                    File_path = os.path.join(self.Path, File);
                    print(f"{i} ---- {File_path}");

                    if(Height != None and Width != None):
                
                        Combinations_int, Euler = self.process_octovoxel(File_path, self.STORAGELIST, Height, Width);
                    
                        #print(f"Combinations = {Combinations}, Euler = {Euler}");
                    
                    Combinations_all.append(Combinations_int);
                    Euler_all.append(Euler);

                return Combinations_all, Euler_all
            
            else:

                if(Height != None and Width != None):

                        print(f"Processing file...");

                        Combinations, Euler = self.process_octovoxel(File_path, self.STORAGELIST, Height, Width);

                        return Combinations, Euler
            
        except Exception as e:
            # * You can also choose to return a default value or handle the exception differently.
            print(f"An error occurred processing {self.__class__.__name__}: {e}")
