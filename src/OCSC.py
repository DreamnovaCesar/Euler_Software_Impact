import os
import numpy as np
import pandas as pd
import multiprocessing

from src.Utils.Config import Config
from src.Utils.DataLoader import DataLoader
from src.CHUNKS import image_into_chunks
from src.Utils.Utils import calculate_contact_surface

from src.Decorator.TimerCMD import Timer
from src.Decorator.multiprocessing_info import multiprocessing_info

from typing import Optional, Union, List, Tuple

from src.DM import DM

class OCSC(DM):
    """
    Q_values denote the spatial extent of each identified pattern within the 3D image.
    Octo-Voxel Contact Surface Chunks (OCSC) - A performance-optimized class for handling Octo-Voxels, 
    leveraging asynchronous approaches and multiprocessing. Utilizes CHUNKS functions for enhanced
    processing of 3D objects, resulting in substantial speed improvements in the Euler Descriptor Extractor.
    Recommended image size: 32x32x32 voxels or larger.
    Smaller images may not yield substantial benefits due to overheads.

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
    save_to_csv(Combinations_data: Union[np.ndarray, list], Contact_surface_data: Union[np.ndarray, list]) -> None:
        Save the combinations and Contact_surface values to a CSV file.

    process_octovoxel(CHUNK: np.ndarray, STORAGELIST: np.ndarray) -> Tuple[np.ndarray, int]:
        Process a sub-volume of octovoxel and return combinations and Contact_surface value.

    get_array(Depth: int, Height: int, Width: int) -> np.ndarray:
        Calculate Combinations_int based on the given Storage_list using multiprocessing.
    """

    def __init__(self,
                 path: str,
                 num_processes: Optional[int] = (multiprocessing.cpu_count() // 2)) -> None:
        """
        Initialize OCSC.

        Parameters:
        ----------
        path : str
            The file path for data and convert it into an array.
        num_processes : Optional[int]
            Number of parallel processes (default: half of available CPU cores).
        """

        super().__init__(path, num_processes)
        self.Descriptor = "Contact_Surface_Async";
    
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
                          CHUNK : np.ndarray, 
                          STORAGELIST : List[np.ndarray]) -> np.ndarray:
        """
        Process a sub-volume of octovoxel and return combinations and Euler value.

        Parameters:
        -----------
        CHUNK : np.ndarray
            Sub-volume of octovoxel.
        STORAGELIST : List[np.ndarray]
            Numpy array representation of the binary storage list.

        Returns:
        -------
        Tuple[np.ndarray, int]
            Combinations array and Euler value.
        """

        Combinations = int(Config.Byte_binary, 2);
        
        # * Create an array to store Combinations_int and initialize it with zeros.
        Combinations_int = np.zeros((Combinations), dtype='int');
        
        # * Create sliding windows for CHUNK for faster access to sub-volumes
        VIEW_CHUNK = np.lib.stride_tricks.sliding_window_view(CHUNK, (Config.Octovoxel_size, Config.Octovoxel_size, Config.Octovoxel_size));
        
        # * Convert STORAGELIST to a single numpy array for vectorized comparisons
        STORAGELIST_array = np.array(STORAGELIST);
        
        # * Vectorized comparison and counting
        for Index in range(len(STORAGELIST)):
            Equal_mask = (VIEW_CHUNK == STORAGELIST_array[Index]).all(axis=(3, 4, 5));
            Combinations_int[Index] += Equal_mask.sum();
        
        return Combinations_int
    
    @Timer.timer("Execution_OCSC.log")
    @multiprocessing_info 
    def get_array(self, Depth : int, Height : int, Width : int):
        """
        Calculate Combinations_int based on the given Storage_list using multiprocessing.

        Parameters:
        -----------
        Depth : int
            Depth dimension of the 3D image.
        Height : int
            Height dimension of the 3D image.
        Width : int
            Width dimension of the 3D image.

        Returns:
        -------
        np.ndarray
            An array of Combinations_int.
        """
        
        try:
        
            if(self.Folder):
                
                Combinations_all = [];
                Contact_surface_all = [];
            
                # * Filter the list to include only .txt files
                Files = os.listdir(self.Path);
                
                print(f"Processing file... Total : {len(Files)}");

                for i, File in enumerate(Files):

                    File_path = os.path.join(self.Path, File);
                    Arrays = DataLoader.load_data(File_path);
                    Arrays = Arrays.reshape(Depth, Height, Width);
                    Contact_surface = calculate_contact_surface(Arrays);

                    print(f"{i} ---- {File_path}");

                    CHUNKS = image_into_chunks(File_path, Depth, Height, Width);

                    with multiprocessing.Pool(processes=self.Num_processes) as pool:
                        # * Use starmap to pass both CHUNKS and STORAGELIST to process_octovoxel
                        Results = pool.starmap_async(self.process_octovoxel, [(CHUNK, self.STORAGELIST) for CHUNK in CHUNKS]);
                        
                        Data = Results.get();

                        # * Extract Results and Contact_surface from the list of results
                        Combination = zip(*Data);

                        #print(Combination);

                    Result_combination = np.sum(Combination, axis=0);

                    Combinations_all.append(Result_combination);
                    Contact_surface_all.append(Contact_surface);
                
                return Combinations_all, Contact_surface_all, self.Descriptor

            else:
                
                print(f"Processing file...");

                Arrays = DataLoader.load_data(self.Path);
                Arrays = Arrays.reshape(Depth, Height, Width);
                Contact_surface = calculate_contact_surface(Arrays);

                CHUNKS = image_into_chunks(self.Path, Depth, Height, Width);

                with multiprocessing.Pool(processes=self.Num_processes) as pool:
                    # * Use starmap to pass both CHUNKS and STORAGELIST to process_octovoxel
                    Results = pool.starmap_async(self.process_octovoxel, [(CHUNK, self.STORAGELIST) for CHUNK in CHUNKS]);
                    
                    Data = Results.get();

                    # * Extract Results and Contact_surface from the list of results
                    #Combination = zip(*Data);

                    #print(Combination);

                Result_combination = np.sum(Data, axis=0);

                return Result_combination, Contact_surface, self.Descriptor

        except Exception as e:
            print(f"Error on the multiprocessing function: {e}")
