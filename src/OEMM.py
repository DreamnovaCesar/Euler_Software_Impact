import os
import numpy as np
import pandas as pd
import multiprocessing

from src.Utils.Config import Config
from src.Utils.DataLoader import DataLoader

from src.Decorator.TimerCMD import Timer
from src.Decorator.multiprocessing_info import multiprocessing_info

from typing import Optional, Union, List, Tuple

from src.DM import DM

class OEMM(DM):
    """
    Q_values denote the spatial extent of each identified pattern within the 3D image.
    Octo-Voxel Euler Multi Manager (OEMM) - Asynchronous approaches and multiprocessing are employed in a class created
    specifically to handle Octo-Voxels, resulting in significant improvements in speed in the Euler Descriptor Extractor.

    Attributes:
    -----------
    Path : str
        The file path for data and convert it into an array.
    Basepath : str
        The base name of the file path.
    Folder : bool
        Indicates whether the provided path is a directory.
    Num_processes : Optional[int]
        Number of parallel processes (default: half of available CPU cores).
    SLC : ByteStorage
        Instance of ByteStorage for handling binary storage lists.
    STORAGELIST : np.ndarray
        Numpy array representation of the binary storage list.

    Methods:
    --------
    save_to_csv(Combinations_data: Union[np.ndarray, list], Euler_data: Union[np.ndarray, list]) -> None:
        Save the combinations and Euler values to a CSV file.

    process_octovoxel(CHUNK: np.ndarray, STORAGELIST: np.ndarray) -> Tuple[np.ndarray, int]:
        Process a sub-volume of octovoxel and return combinations and Euler value.

    get_array(Depth: int, Height: int, Width: int) -> np.ndarray:
        Calculate Combinations_int based on the given Storage_list using multiprocessing.
    """
    def __init__(self,
                 path: str,
                 num_processes: Optional[int] = (multiprocessing.cpu_count() // 2)) -> None:
        """
        Initialize OEMM.

        Parameters:
        ----------
        Path : str
            The file path for data and convert it into an array.
        Num_processes : Optional[int]
            Number of parallel processes (default: half of available CPU cores).
        """
        super().__init__(path, num_processes)
        self.Descriptor = "Euler_Async";
    
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
        Arrays = Arrays.reshape(Depth, Height, Width);
        
        # * Create sliding windows for CHUNK for faster access to sub-volumes
        VIEW_CHUNK = np.lib.stride_tricks.sliding_window_view(Arrays, (Config.Octovoxel_size, Config.Octovoxel_size, Config.Octovoxel_size));
        
        # * Convert STORAGELIST to a single numpy array for vectorized comparisons
        STORAGELIST_array = np.array(STORAGELIST);
        
        # * Vectorized comparison and counting
        for index in range(len(STORAGELIST)):
            Equal_mask = (VIEW_CHUNK == STORAGELIST_array[index]).all(axis=(3, 4, 5));
            Combinations_int[index] += Equal_mask.sum();

        # * Return the calculated Combinations_int as a numpy array.
        Combinations = (Combinations_int * Config._OUTPUT_3D_);
        Euler = np.sum(Combinations);

        print(f"Processing file... {File_path} ----------- {Euler}");

        return Combinations_int, Euler
            
    @Timer.timer("Execution_OEMM.log")
    @multiprocessing_info    
    def get_array(self, Depth: int, Height: int, Width: int) -> None:
        """
        Perform multiprocessing to calculate Combinations_int based on the given self.STORAGELIST.

        Parameters:
        -----------
        Depth : int
            The depth dimension of the 3D array.
        Height : int
            The height dimension of the 3D array.
        Width : int
            The width dimension of the 3D array.

        Returns:
        -------
        Tuple[List[np.ndarray], List[int], str]
            A tuple containing arrays of Combinations_int, Euler values, and the descriptor obtained by processing multiple files in parallel.

        Notes:
        ------
        - If the `Path` attribute indicates a directory, the method processes all .txt files in that directory.
        - Utilizes multiprocessing to parallelize the calculation for each file.
        - Combinations_int and Euler values are accumulated across all processed files.
        - The results are saved to a CSV file using the `save_to_csv_euler` method.
        - The final result is the sum of Combinations_int across all files.

        """
        
        if self.Folder:
            Combinations_all = []
            Euler_all = []

            # * Filter the list to include only .txt files
            Files = os.listdir(self.Path);
            print(f"Processing files... Total: {len(Files)}");
    
            with multiprocessing.Pool(processes=self.Num_processes) as pool:
                # * Use starmap to pass both file paths and STORAGELIST to process_octovoxel
                Results = pool.starmap_async(self.process_octovoxel, [(File, self.STORAGELIST, Depth, Height, Width) for File in Files]);

                Data = Results.get();

                # * Extract Results and Euler from the list of results
                Combinations, Euler = zip(*Data);
        
                '''Result_combination = np.sum(Combination, axis=0);
                Result_euler = np.sum(Euler, axis=0);'''
                
                for _, (C, E) in enumerate(zip(Combinations, Euler)):

                    Combinations_all.append(C);
                    Euler_all.append(E);

            return Combinations_all, Euler_all, self.Descriptor 
        else:
            return None



