import os
import numpy as np
import pandas as pd
import multiprocessing

from src.Utils.Config import Config
from src.Utils.DataLoader import DataLoader
from src.Utils.Utils import calculate_area

from src.Decorator.TimerCMD import Timer
from src.Decorator.multiprocessing_info import multiprocessing_info

from typing import Optional, Union, List

from src.OM import OM

class OAMM(OM):
    """
    Q_values denote the spatial extent of each identified pattern within the 3D image.
    Octo-Voxel Area Multi Manager (OAMM) - A class for handling Octo-Voxels and obtaining Q_values based on the given ByteStorage.
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
    __str__() -> str:
        Return a string description of the object.

    save_to_csv_area(Combinations_data: Union[np.ndarray, list], Area_data: Union[np.ndarray, list]) -> None:
        Save the combinations and Area values to a CSV file.

    process_octovoxel(CHUNK: np.ndarray, STORAGELIST: np.ndarray) -> Tuple[np.ndarray, int]:
        Process a sub-volume of octovoxel and return combinations and Area value.

    get_array_multiprocessing(Depth: int, Height: int, Width: int) -> np.ndarray:
        Calculate Combinations_int based on the given Storage_list using multiprocessing.
    """

    def __init__(self,
                 path: str,
                 dest_path : str,
                 num_processes: Optional[int] = (multiprocessing.cpu_count() // 2)) -> None:
        """
        Initialize OAMM.

        Parameters:
        ----------
        Path : str
            The file path for data and convert it into an array.
        Num_processes : Optional[int]
            Number of parallel processes (default: half of available CPU cores).
        """

        super().__init__(path, dest_path, num_processes)

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

    def save_to_csv(self, 
                    Combinations_data : Union[np.ndarray, list], 
                    Area_data : Union[np.ndarray, list]
                    ) -> None:
        """
        Save the combinations and Area values to a CSV file.

        Parameters:
        -----------
        Combinations : np.ndarray
            The array of combinations to be saved.

        Area : np.ndarray
            The array of Area values.
        """

        _Is_list = False;
    
        if(isinstance(Combinations_data, list) and isinstance(Area_data, list)):
            _Is_list = True;       
        
        Dataframe_completed = pd.DataFrame();

        try:
            
            if(_Is_list):

                for _, (Combination, Area) in enumerate(zip(Combinations_data, Area_data)):
                    
                    #print(Area);
                    #print(f"Combinations_data shape: {Combination.shape}")
                    #print(f"Area_data shape: {Area.shape}")
                    #print(f"{Combination} ------ {Area}");

                    print(f"Combinations len {Combination.shape[0]}");
                    
                    Combination = Combination.reshape((1, Combination.shape[0]));

                    print(f"Combinations len reshape {Combination.shape[0]}, {Combination.shape[1]}");

                    '''print("\n");
                    print(f"{Combination} ------ {Area}");
                    print("\n");'''
                    print(f"Rows : {Combination.shape[0]} ------ Columns : {Combination.shape[1]}");

                    # * Convert the combinations array to a Pandas DataFrame
                    Dataframe_combination = pd.DataFrame(Combination, columns=[f"Voxel {i+1}" for i in range(Combination.shape[1])]);

                    # * Add the 'Area' column to the DataFrame
                    Dataframe_combination['Area'] = Area;

                    # * Append the new data to the DataFrame
                    Dataframe_completed = pd.concat([Dataframe_completed, Dataframe_combination], ignore_index=True);
                    
                    print(Dataframe_completed);
                
                # * Check if the folder exists, create it if not
                if not os.path.exists(self.Dest_path):
                    os.makedirs(self.Dest_path);

                Base_name = f"Combinations_And_Area_{self.Basepath}_async.csv";

                print(f"Combinations_And_Area_{self.Basepath}_async.csv");

                # * Save the DataFrame to a CSV file
                File_path = os.path.join(self.Dest_path, Base_name);
                Dataframe_completed.to_csv(File_path, index=False);

            else:   
                    Combination = Combinations_data;
                    Area = Area_data;

                    #print(f"Combinations_data shape: {Combination.shape}")
                    #print(f"Area_data shape: {Area.shape}")
                    #print(f"{Combination} ------ {Area}");

                    print(f"Combinations len {Combination.shape[0]}");
                    Combination = Combination.reshape((1, Combination.shape[0]));
                    print(f"Combinations len reshape {Combination.shape[0]}, {Combination.shape[1]}");
                    print(f"Rows : {Combination.shape[0]} ------ Columns : {Combination.shape[1]}");

                    # * Convert the combinations array to a Pandas DataFrame
                    Dataframe_combination = pd.DataFrame(Combination, columns=[f"Voxel {i+1}" for i in range(Combination.shape[1])]);

                    # * Add the 'Area' column to the DataFrame
                    Dataframe_combination['Area'] = Area;

                    print(Dataframe_combination);
                
                    # * Check if the folder exists, create it if not
                    if not os.path.exists(self.Dest_path):
                        os.makedirs(self.Dest_path);

                    Base_name = f"Combinations_And_Area_{self.Basepath}_async.csv";

                    print(f"Combinations_And_Area_{self.Basepath}_async.csv");

                    # * Save the DataFrame to a CSV file
                    File_path = os.path.join(self.Dest_path, Base_name);
                    Dataframe_combination.to_csv(File_path, index=False);
                
            print(f"Combinations and Area values saved to {File_path}");
        
        except Exception as e:
            print(f"An error occurred while saving to CSV: {e} {self.__class__.__name__}")

    def process_octovoxel(self, 
                          File : str, 
                          STORAGELIST : List[np.ndarray], 
                          Depth : int, 
                          Height : int, 
                          Width : int):
        """
        Calculate Combinations_int based on the given Storage_list and return them as a numpy array.

        Parameters:
        -----------
        File : str
            The name of the file being processed.
        STORAGELIST : np.ndarray
            Numpy array representation of the binary storage list.
        Depth : int
            The depth dimension of the 3D array.
        Height : int
            The height dimension of the 3D array.
        Width : int
            The width dimension of the 3D array.

        Returns:
        -------
        Tuple[np.ndarray, int]
            A tuple containing an array of Combinations_int and Area value.

        Notes:
        ------
        - Octovoxel size is set to 2.
        - Area value is the sum of Combinations_int.

        """

        Combinations = int(Config.Byte_binary, 2);
        
        # * Create an array to store Combinations_int and initialize it with zeros.
        Combinations_int = np.zeros((Combinations), dtype='int');
        File_path = os.path.join(self.Path, File);
        Arrays = DataLoader.load_data(File_path);
        
        print(f"Processing files... Total: {File}")

        # * Reshape the array to a 3D array based on the calculated height.
        Arrays = Arrays.reshape(Depth, Height, Width);

        Area = calculate_area(Arrays);

        for i in range(Arrays.shape[0] - 1):
            for j in range(Arrays.shape[1] - 1):
                for k in range(Arrays.shape[2] - 1):
                    for index in range(len(STORAGELIST)):
                        if np.array_equal(np.array(Arrays[i:Config.Octovoxel_size + i, 
                                                          j:Config.Octovoxel_size + j, 
                                                          k:Config.Octovoxel_size + k]), 

                                        np.array(STORAGELIST[index])):                       
                            
                            Combinations_int[index] += 1;

                            #print(Combinations_int)

        # * Return the calculated Combinations_int as a numpy array.
        #Combinations = (Combinations_int * Config._OUTPUT_3D_);
    
        #Area = np.sum(Combinations);

        #print(f"Combinations = {Combinations_int}, Area = {Area}");

        return Combinations_int, Area;

    @Timer.timer()
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
        np.ndarray
            An array of Combinations_int obtained by processing multiple files in parallel.

        Notes:
        ------
        - If the `Path` attribute indicates a directory, the method processes all .txt files in that directory.
        - Utilizes multiprocessing to parallelize the calculation for each file.
        - Combinations_int and Area values are accumulated across all processed files.
        - The results are saved to a CSV file using the `save_to_csv_area` method.
        - The final result is the sum of Combinations_int across all files.

        """
        
        if self.Folder:
            Combinations_all = [];
            Area_all = [];

            # * Filter the list to include only .txt files
            Files = os.listdir(self.Path);
            print(f"Processing files... Total: {len(Files)}");
    
            with multiprocessing.Pool(processes=self.Num_processes) as pool:
                # * Use starmap to pass both file paths and STORAGELIST to process_octovoxel
                Results = pool.starmap_async(self.process_octovoxel, [(File, self.STORAGELIST, Depth, Height, Width) for File in Files]);

                Data = Results.get();

                # * Extract Results and Area from the list of results
                Combination, Area = zip(*Data);

                '''Result_combination = np.sum(Combination, axis=0);
                Result_area = np.sum(Area, axis=0);'''
                
                for _, (C, E) in enumerate(zip(Combination, Area)):

                    Combinations_all.append(C);
                    Area_all.append(E);

            self.save_to_csv(Combinations_all, Area_all);



