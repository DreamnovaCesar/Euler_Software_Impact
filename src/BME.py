import os
import numpy as np
import pandas as pd

from src.Utils.Config import Config
from src.Utils.DataLoader import DataLoader
from src.Utils.NibbleStorage import NibbleStorage

from src.Decorator.TimerCMD import Timer
from src.Decorator.multiprocessing_info import multiprocessing_info

from src.DM import DM

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
                 connectivity : int = 4
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
    
    def save_to_csv(self, 
                    Combinations_data : np.ndarray, 
                    Euler_data : np.ndarray
                    ) -> None:
        """
        Save the combinations and Euler values to a CSV file.

        Parameters:
        -----------
        Combinations : np.ndarray
            The array of combinations to be saved.

        Euler : np.ndarray
            The array of Euler values.
        """

        _Is_list = False;
    
        if isinstance(Combinations_data, list) and isinstance(Euler_data, list):
            _Is_list = True;       


        Dataframe_completed = pd.DataFrame();

        try:
            
            if(_Is_list):

                for _, (Combination, Euler) in enumerate(zip(Combinations_data, Euler_data)):
                    
                    #print(f"Combinations_data shape: {Combination.shape}")
                    #print(f"Euler_data shape: {Euler.shape}")
                    #print(f"{Combination} ------ {Euler}");

                    print(f"Combinations len {Combination.shape[0]}");
                    
                    Combination = Combination.reshape((1, Combination.shape[0]));

                    print(f"Combinations len reshape {Combination.shape[0]}, {Combination.shape[1]}");
                    print(f"Rows : {Combination.shape[0]} ------ Columns : {Combination.shape[1]}");

                    # * Convert the combinations array to a Pandas DataFrame
                    Dataframe_combination = pd.DataFrame(Combination, columns=[f"BitQuad {i+1}" for i in range(Combination.shape[1])]);

                    # * Add the 'Euler' column to the DataFrame
                    Dataframe_combination['Euler'] = Euler;

                    # * Append the new data to the DataFrame
                    Dataframe_completed = pd.concat([Dataframe_completed, Dataframe_combination], ignore_index=True);
                    
                    print(Dataframe_completed);
                
                # * Check if the folder exists, create it if not
                if not os.path.exists(self.Dest_path):
                    os.makedirs(self.Dest_path);

                Base_name = f"Combinations_And_Euler_{self.Basepath}_{self._C_}.csv";

                print(f"Combinations_And_Euler_{self.Basepath}.csv");

                # * Save the DataFrame to a CSV file
                File_path = os.path.join(self.Dest_path, Base_name);
                Dataframe_completed.to_csv(File_path, index=False);

            else:   
                    Combination = Combinations_data;
                    Euler = Euler_data;

                    #print(f"Combinations_data shape: {Combination.shape}")
                    #print(f"Euler_data shape: {Euler.shape}")
                    #print(f"{Combination} ------ {Euler}");

                    print(f"Combinations len {Combination.shape[0]}");
                    Combination = Combination.reshape((1, Combination.shape[0]));
                    print(f"Combinations len reshape {Combination.shape[0]}, {Combination.shape[1]}");
                    print(f"Rows : {Combination.shape[0]} ------ Columns : {Combination.shape[1]}");

                    # * Convert the combinations array to a Pandas DataFrame
                    Dataframe_combination = pd.DataFrame(Combination, columns=[f"BitQuad {i+1}" for i in range(Combination.shape[1])]);

                    # * Add the 'Euler' column to the DataFrame
                    Dataframe_combination['Euler'] = Euler;

                    print(Dataframe_combination);
                
                    # * Check if the folder exists, create it if not
                    if not os.path.exists(self.Dest_path):
                        os.makedirs(self.Dest_path);

                    Base_name = f"Combinations_And_Euler_{self.Basepath}_{self._C_}.csv";

                    print(f"Combinations_And_Euler_{self.Basepath}.csv");

                    # * Save the DataFrame to a CSV file
                    File_path = os.path.join(self.Path, Base_name);
                    Dataframe_combination.to_csv(File_path, index=False);
                
            print(f"Combinations and Euler values saved to {File_path}");
        
        except Exception as e:
            print(f"An error occurred while saving to CSV: {e} {self.__class__.__name__}")

    @Timer.timer()
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
                
                        Combinations = int(Config.Nibble_binary, 2);
                        
                        # * Create an array to store Combinations_int and initialize it with zeros.
                        Combinations_int = np.zeros((Combinations), dtype='int');

                        self.Arrays = DataLoader.load_data(File_path);
                        
                        # * Reshape the array to a 3D array based on the calculated height.
                        self.Arrays = self.Arrays.reshape(Height, Width);

                        for i in range(self.Arrays.shape[0] - 1):
                            for j in range(self.Arrays.shape[1] - 1):
                                for index in range(len(self.STORAGELIST)):
                                    if np.array_equal(np.array(self.Arrays[i:Config.Bitquads_size + i, 
                                                                           j:Config.Bitquads_size + j]),  

                                                        np.array(self.STORAGELIST[index])):                       
                                            
                                            Combinations_int[index] += 1;

                                            #print(Combinations_int);
                        
                        # * Return the calculated Combinations_int as a numpy array.
                        Combinations = (Combinations_int * self._CONNECTIVITY_);

                        Euler = np.sum(Combinations);
                    
                        #print(f"Combinations = {Combinations}, Euler = {Euler}");
                    
                    Combinations_all.append(Combinations_int);
                    Euler_all.append(Euler);

                self.save_to_csv(Combinations_all, Euler_all)

                return Combinations_all, Euler_all
            
            else:

                if(Height != None and Width != None):

                        print(f"Processing file...");

                        Combinations = int(Config.Nibble_binary, 2);
                        
                        # * Create an array to store Combinations_int and initialize it with zeros.
                        Combinations_int = np.zeros((Combinations), dtype='int');

                        self.Arrays = DataLoader.load_data(self.Path);

                        # * Reshape the array to a 3D array based on the calculated height.
                        self.Arrays = self.Arrays.reshape(Height, Width);

                        for i in range(self.Arrays.shape[0] - 1):
                            for j in range(self.Arrays.shape[1] - 1):
                                    for index in range(len(self.STORAGELIST)):
                                        if np.array_equal(np.array(self.Arrays[i:Config.Bitquads_size + i, 
                                                                               j:Config.Bitquads_size + j]),        

                                                        np.array(self.STORAGELIST[index])):                       
                                            
                                            Combinations_int[index] += 1;

                                            #print(Combinations_int);
                        
                        # * Return the calculated Combinations_int as a numpy array.
                        Combinations = (Combinations_int * self._CONNECTIVITY_);
                    
                        Euler = np.sum(Combinations);

                        #print(f"Combinations = {Combinations_int}, Euler = {Euler}");

                        self.save_to_csv(Combinations_int, Euler)

                        return Combinations, Euler
            
        except Exception as e:
            # * You can also choose to return a default value or handle the exception differently.
            print(f"An error occurred processing {self.__class__.__name__}: {e}")
