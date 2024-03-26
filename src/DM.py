from abc import ABC
from abc import abstractmethod

import os
import numpy as np
import multiprocessing

from typing import Optional, Union, List, Tuple

from src.Utils.ByteStorage import ByteStorage
from src.Utils.Utils import is_txt_file

class DM(ABC):
    """
    Q_values denote the spatial extent of each identified pattern within the 3D image.
    Descriptor Manager (DM) - A class for handling Octo-Voxels and obtaining Q_values based on the given ByteStorage.
    Utilizes multiprocessing and asynchronous techniques for significant performance enhancements.
    This analyze each image inside a directory.

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

    save_to_csv(Combinations_data: Union[np.ndarray, list], Volume_data: Union[np.ndarray, list]) -> None:
        Save the combinations and Volume values to a CSV file.

    get_array_multiprocessing(Depth: int, Height: int, Width: int) -> np.ndarray:
        Calculate Combinations_int based on the given Storage_list using multiprocessing.
    """

    def __init__(self,
                 path: str,
                 num_processes: Optional[int] = (multiprocessing.cpu_count() // 2)) -> None:
        """
        Initialize DM.

        Parameters:
        ----------
        Path : str
            The file path for data and convert it into an array.
        Num_processes : Optional[int]
            Number of parallel processes (default: half of available CPU cores).
        """

        self.Path = path;
        self.Basepath = os.path.basename(path);
        self.Folder = False;
        self.Num_processes = num_processes;

        print(self.Path);
        print(self.Basepath);
        print(self.Folder);
        
        self.SLC = ByteStorage;
        self.STORAGELIST = self.SLC.to_numpy_array();

        # * Check if Path is a directory
        if os.path.isdir(self.Path):
            print(f"Is a Directory");
            self.Folder = True;
        # * Check if Path is a file
        elif is_txt_file(self.Path):
            print(f"Is a File txt");
        else:
            print(f"Neither");

    @abstractmethod
    def process_octovoxel(self, 
                          CHUNK : np.ndarray, 
                          STORAGELIST : List[np.ndarray]):
        """
        Save the combinations and Volume values to a CSV file.

        """
        pass

    @abstractmethod
    def get_array(self, Depth: int, Height: int, Width: int) -> None:
        """
        Perform multiprocessing to calculate Combinations_int based on the given self.STORAGELIST.

        """
        pass

