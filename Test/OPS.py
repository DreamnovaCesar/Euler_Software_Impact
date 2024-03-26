import os
import numpy as np
import pandas as pd

from src.Utils.Config import Config
from src.Utils.DataLoader import DataLoader
from src.Utils.ByteStorage import ByteStorage
from src.Utils.Utils import is_txt_file

from src.Decorator.TimerCMD import Timer
from src.Decorator.multiprocessing_info import multiprocessing_info

from typing import Optional, Union

from src.Utils.Utils import calculate_enclosing_surface

class OESS:
    """
    Q_values denote the spatial extent of each identified pattern within the 3D image.
    Octo-Voxel Enclosing Surface Simplified (OVS) - A class for handling Octo-Voxels and obtaining Q_values based on the given ByteStorage. 

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
    __str__() -> str:
        Return a string description of the object.

    get_array(Depth: int, Height: int, Width: int) -> Union[np.ndarray, list]:
        Calculate Combinations_int based on the given STORAGELIST and return them as a numpy array.

    save_to_csv_Enclosing_surface(Combinations_data: Union[np.ndarray, list], Enclosing_surface_data: Union[np.ndarray, list]) -> None:
        Save the combinations and Enclosing_surface values to a CSV file.

    Notes:
    ------
    This class provides methods for processing octovoxel data and calculating Combinations_int based on a given STORAGELIST.

    Examples:
    ---------
    >>> File_path = "data.csv"
    >>> Handler = OESS(File_path)
    >>> Result_combinations, Result_Enclosing_surface = Handler.get_array(Depth=3, Height=3, Width=3)
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

        self.Path = path;
        self.Basepath = os.path.basename(path);
        self.Folder = True;

        self.SLC = ByteStorage;
        self.STORAGELIST = self.SLC.to_numpy_array();

        # * Check if Path is a directory
        if os.path.isdir(self.Path):
            print(f"Is a Directory");
        # * Check if Path is a file
        elif is_txt_file(self.Path):
            print(f"Is a File txt");
            # *Load the array from the file
            self.Arrays = DataLoader.load_data(self.Path);
            self.Folder = False;
        else:
            print(f"Neither");
    
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
    
    def save_to_csv_Enclosing_surface(self, 
                              Combinations_data : Union[np.ndarray, list], 
                              Enclosing_surface_data : Union[np.ndarray, list]
                              ) -> None:
        """
        Save the combinations and Enclosing_surface values to a CSV file.

        Parameters:
        -----------
        Combinations : np.ndarray
            The array of combinations to be saved.

        Enclosing_surface : np.ndarray
            The array of Enclosing_surface values.
        """

        _Is_list = False;
    
        if isinstance(Combinations_data, list) and isinstance(Enclosing_surface_data, list):
            _Is_list = True;       

        # * Store the data (Combination and Enclosing_surface)
        Dataframe_completed = pd.DataFrame();

        try:
            
            if(_Is_list):

                for _, (Combination, Enclosing_surface) in enumerate(zip(Combinations_data, Enclosing_surface_data)):
                    
                    #print(f"Combinations_data shape: {Combination.shape}")
                    #print(f"Enclosing_surface_data shape: {Enclosing_surface.shape}")
                    #print(f"{Combination} ------ {Enclosing_surface}");

                    print(f"Combinations len {Combination.shape[0]}");
                    Combination = Combination.reshape((1, Combination.shape[0]));
                    print(f"Combinations len reshape {Combination.shape[0]}, {Combination.shape[1]}");
                    print(f"Rows : {Combination.shape[0]} ------ Columns : {Combination.shape[1]}");

                    # * Convert the combinations array to a Pandas DataFrame
                    Dataframe_combination = pd.DataFrame(Combination, columns=[f"Voxel {i+1}" for i in range(Combination.shape[1])]);

                    # * Add the 'Enclosing_surface' column to the DataFrame
                    Dataframe_combination['Enclosing_surface'] = Enclosing_surface;

                    # * Append the new data to the DataFrame
                    Dataframe_completed = pd.concat([Dataframe_completed, Dataframe_combination], ignore_index=True);
                    
                    print(Dataframe_completed);
                
                # * Check if the folder exists, create it if not
                if not os.path.exists(Config.Folder_data):
                    os.makedirs(Config.Folder_data);

                Base_name = f"Combinations_And_Enclosing_surface_{self.Basepath}.csv";

                print(f"Combinations_And_Enclosing_surface_{self.Basepath}.csv");

                # * Save the DataFrame to a CSV file
                File_path = os.path.join(Config.Folder_data, Base_name);
                Dataframe_completed.to_csv(File_path, index=False);

            else:   
                    Combination = Combinations_data;
                    Enclosing_surface = Enclosing_surface_data;

                    #print(f"Combinations_data shape: {Combination.shape}")
                    #print(f"Enclosing_surface_data shape: {Enclosing_surface.shape}")
                    #print(f"{Combination} ------ {Enclosing_surface}");

                    print(f"Combinations len {Combination.shape[0]}");
                    Combination = Combination.reshape((1, Combination.shape[0]));
                    print(f"Combinations len reshape {Combination.shape[0]}, {Combination.shape[1]}");
                    print(f"Rows : {Combination.shape[0]} ------ Columns : {Combination.shape[1]}");

                    # * Convert the combinations array to a Pandas DataFrame
                    Dataframe_combination = pd.DataFrame(Combination, columns=[f"Voxel {i+1}" for i in range(Combination.shape[1])]);

                    # * Add the 'Enclosing_surface' column to the DataFrame
                    Dataframe_combination['Enclosing_surface'] = Enclosing_surface;

                    print(Dataframe_combination);
                
                    # * Check if the folder exists, create it if not
                    if not os.path.exists(Config.Folder_data):
                        os.makedirs(Config.Folder_data);

                    Base_name = f"Combinations_And_Enclosing_surface_{self.Basepath}.csv";

                    print(f"Combinations_And_Enclosing_surface_{self.Basepath}.csv");

                    # * Save the DataFrame to a CSV file
                    File_path = os.path.join(Config.Folder_data, Base_name);
                    Dataframe_combination.to_csv(File_path, index=False);
                
            print(f"Combinations and Enclosing_surface values saved to {File_path}");
        
        except Exception as e:
            print(f"An error occurred while saving to CSV: {e}")

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
                Enclosing_surface_all = [];

                # * Filter the list to include only .txt files
                Files = os.listdir(self.Path);
                
                print(f"Processing file... Total : {Files}");

                for i, File in enumerate(Files):
                    
                    File_path = os.path.join(self.Path, File);
                    print(f"{i} ---- {File_path}");

                    if(Depth != None and Height != None and Width != None):
                
                        Combinations = int(Config.Byte_binary, 2);
                        
                        # * Create an array to store Combinations_int and initialize it with zeros.
                        Combinations_int = np.zeros((Combinations), dtype='int');

                        self.Arrays = DataLoader.load_data(File_path);

                        Enclosing_surface = calculate_enclosing_surface(self.Arrays);

                        # * Reshape the array to a 3D array based on the calculated height.
                        self.Arrays = self.Arrays.reshape(Depth, Height, Width);

                        for i in range(self.Arrays.shape[0] - 1):
                            for j in range(self.Arrays.shape[1] - 1):
                                for k in range(self.Arrays.shape[2] - 1):
                                    for index in range(len(self.STORAGELIST)):
                                        if np.array_equal(np.array(self.Arrays[i:Config.Octovoxel_size + i, 
                                                                            j:Config.Octovoxel_size + j, 
                                                                            k:Config.Octovoxel_size + k]),               
                                                        np.array(self.STORAGELIST[index])):                       
                                            
                                            Combinations_int[index] += 1;

                                            #print(Combinations_int);
                        
                        # * Return the calculated Combinations_int as a numpy array.
                        #Combinations = (Combinations_int * Config._OUTPUT_3D_);

                        #Euler = np.sum(Combinations);
                    
                        #print(f"Combinations = {Combinations}, Euler = {Euler}");
                    
                    Combinations_all.append(Combinations_int);
                    Enclosing_surface_all.append(Enclosing_surface);

                self.save_to_csv_Enclosing_surface(Combinations_all, Enclosing_surface_all)

                return Combinations_all, Enclosing_surface_all
            
            else:

                if(Depth != None and Height != None and Width != None):

                        print(f"Processing file...");

                        Combinations = int(Config.Byte_binary, 2);
                        
                        # * Create an array to store Combinations_int and initialize it with zeros.
                        Combinations_int = np.zeros((Combinations), dtype='int');

                        # * Reshape the array to a 3D array based on the calculated height.
                        self.Arrays = self.Arrays.reshape(Depth, Height, Width);

                        Enclosing_surface = calculate_enclosing_surface(self.Arrays);

                        for i in range(self.Arrays.shape[0] - 1):
                            for j in range(self.Arrays.shape[1] - 1):
                                for k in range(self.Arrays.shape[2] - 1):
                                    for index in range(len(self.STORAGELIST)):
                                        if np.array_equal(np.array(self.Arrays[i:Config.Octovoxel_size + i, 
                                                                            j:Config.Octovoxel_size + j, 
                                                                            k:Config.Octovoxel_size + k]),               
                                                        np.array(self.STORAGELIST[index])):                       
                                            
                                            Combinations_int[index] += 1;

                                            #print(Combinations_int);
                        
                        # * Return the calculated Combinations_int as a numpy array.
                        #Combinations = (Combinations_int * Config._OUTPUT_3D_);
                        #Euler = np.sum(Combinations);

                        #print(f"Combinations = {Combinations_int}, Euler = {Euler}");

                        self.save_to_csv_Enclosing_surface(Combinations_int, Enclosing_surface)

                        return Combinations_int, Enclosing_surface
            
        except Exception as e:
            # * You can also choose to return a default value or handle the exception differently.
            print(f"An error occurred processing Octovoxel: {e}")
