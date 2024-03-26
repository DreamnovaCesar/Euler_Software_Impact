import os
import numpy as np
import pandas as pd

from src.Utils.Config import Config
from src.Utils.DataLoader import DataLoader
from src.Utils.ByteStorage import ByteStorage
from src.Utils.Utils import is_txt_file

from src.Decorator.TimerCMD import Timer
from src.Decorator.multiprocessing_info import multiprocessing_info
from src.CHUNKS import image_into_chunks

from typing import Optional, Union, List, Tuple

from src.Utils.Utils import calculate_enclosing_surface

import multiprocessing

class OESC:
    """
    Q_values denote the spatial extent of each identified pattern within the 3D image.
    Octo-Voxel Enclosing Surface Chunks (OESC) - A class for handling Octo-Voxels and obtaining Q_values based on the given ByteStorage.
    Utilizes multiprocessing and asynchronous techniques for significant performance enhancements.
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

    CHUNK_divided_3d(Image: str, Depth: int, Height: int, Width: int) -> list[np.ndarray]:
        Divide a 3D image into chunks and return a list of sub-volumes.

    save_to_csv_Enclosing_surface(Combinations_data: Union[np.ndarray, list], Enclosing_surface_data: Union[np.ndarray, list]) -> None:
        Save the combinations and Enclosing_surface values to a CSV file.

    process_octovoxel(CHUNK: np.ndarray, STORAGELIST: np.ndarray) -> Tuple[np.ndarray, int]:
        Process a sub-volume of octovoxel and return combinations and Enclosing_surface value.

    get_array_multiprocessing(Depth: int, Height: int, Width: int) -> np.ndarray:
        Calculate Combinations_int based on the given Storage_list using multiprocessing.
    """

    def __init__(self,
                 path: str,
                 num_processes: Optional[int] = (multiprocessing.cpu_count() // 2)) -> None:
        """
        Initialize OESC.

        Parameters:
        ----------
        path : str
            The file path for data and convert it into an array.
        num_processes : Optional[int]
            Number of parallel processes (default: half of available CPU cores).
        """

        self.Path = path;
        self.Basepath = os.path.basename(path);
        self.Folder = False;
        self.Num_processes = num_processes;

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
    
    '''# *Load the array from the file
    @staticmethod
    def CHUNK_divided_3d(Image : str, Depth : int, Height : int, Width : int) -> list[np.ndarray]:
        """
        Divide a 3D image into chunks and return a list of sub-volumes.

        This code is creating several "chunks" or slices of a 3D image array, each with a different orientation. 
        These chunks are extracted from the original image to provide access to sub-volumes of the image. 
        The purpose of obtaining these sub-volumes is to facilitate the processing of Octo-Voxels in a more structured manner, 
        likely to perform some analysis or computation on specific regions of the 3D image.

        A brief explanation of each CHUNK:

        CHUNK_width: Extracts a 2D slice along the width of the 3D image at the central depth. It includes two columns, 
        centered around the middle column of the width.

        CHUNK_height_1: Extracts a 2D slice along the height of the 3D image at the central width. It includes two rows, 
        centered around the middle row of the height, and spans from the beginning to the middle of the width.

        CHUNK_height_2: Similar to CHUNK_height_1 but spans from the middle to the end of the width.

        CHUNK_depth_1: Extracts a 2D slice along the depth of the 3D image at the central height. It includes two slices, 
        centered around the middle slice of the depth, and spans from the beginning to the middle of the height.

        CHUNK_depth_2: Similar to CHUNK_depth_1 but spans from the middle to the end of the height.

        CHUNK_depth_3: Extracts a 2D slice along the depth of the 3D image at the central height. It includes two slices, 
        centered around the middle slice of the depth, and spans from the beginning to the middle of the width.

        CHUNK_depth_4: Similar to CHUNK_depth_3 but spans from the middle to the end of the width.
        
        Parameters:
        -----------
        Image : str
            The file path for loading an array of numbers.
        Depth : int
            Depth dimension of the 3D image.
        Height : int
            Height dimension of the 3D image.
        Width : int
            Width dimension of the 3D image.

        Returns:
        -------
        list[np.ndarray]
            List of sub-volumes.
        """

        CHUNKS = 2;

        Image = DataLoader.load_data(Image);
        
        # * Get the dimensions of the original image
        #Depth, Height, Width = Image.shape;

        # * Reshape the array to a 3D array based on the calculated height.
        Image = Image.reshape(Depth, Height, Width);

        #print(f"Completes image = {Image}")
        #print(f"Depth : {Depth}, Height : {Height}, Width: {Width}" );
        
        if(Depth % 2 == 1):
            # * Add a new column of zeros to each slice along the depth dimension
            Image = np.pad(Image, ((0, 1), (0, 0), (0, 0)), mode='constant', constant_values=0)

        if(Height % 2 == 1):
            # * Add a new column of zeros to each slice along the height dimension
            Image = np.pad(Image, ((0, 0), (0, 1), (0, 0)), mode='constant', constant_values=0)

        if(Width % 2 == 1):
            # * Add a new column of zeros to each slice along the width dimension
            Image = np.pad(Image, ((0, 0), (0, 0), (0, 1)), mode='constant', constant_values=0)
        
        print(f"Image complete. Depth : {Image.shape[0]}, Height : {Image.shape[1]}, Width: {Image.shape[2]}" )
            
        # * Calculate the size of each sub-volume
        Sub_depth = (Image.shape[0] // 2);
        Sub_height = (Image.shape[1] // 2);
        Sub_width = (Image.shape[2] // 2);

        Depth = Image.shape[0];
        Height = Image.shape[1];
        Width = Image.shape[2];
        
        #print(f"image is Even. Depth : {Sub_depth}, Height : {Sub_height}, Width: {Sub_width}" );

        # * Initialize a list to store the sub-volumes and their coordinates
        #Sub_volumes_with_coordinates = [];
        Sub_volumes_CHUNKS = [];

        # * Iterate through each sub-volume
        for i in range(CHUNKS):
            for j in range(CHUNKS):
                for k in range(CHUNKS):

                    # * Extract the sub-volume from the original image
                    Sub_volume = Image[i * Sub_depth:(i + 1) * Sub_depth,
                                    j * Sub_height:(j + 1) * Sub_height,
                                    k * Sub_width:(k + 1) * Sub_width];

                    #print(f"{Sub_volume.shape[0]} ------ Sub_volume Images {Sub_volume}");
                    
                    """# * Get the coordinates of the sub-volume
                    sub_volume_coordinates = (i * Sub_depth, j * Sub_height, k * Sub_width);
                    
                    # * Sum the two tuples element-wise
                    Sum_result = ((i * Sub_depth + Sub_volume.shape[0]), 
                                (j * Sub_height + Sub_volume.shape[1]), 
                                (k * Sub_width + Sub_volume.shape[2]));

                    # * Add the sub-volume and its coordinates to the list
                    Sub_volumes_with_coordinates.append((Sub_volume, sub_volume_coordinates, Sum_result));"""
                    Sub_volumes_CHUNKS.append(Sub_volume);


        CHUNK_width = Image[:, :, ((Width // 2) - 1):((Width // 2) + 1)];

        CHUNK_height_1 = Image[:, ((Height // 2) - 1):((Height // 2) + 1), :((Width // 2))];
        CHUNK_height_2 = Image[:, ((Height // 2) - 1):((Height // 2) + 1), ((Width // 2)):Width];

        CHUNK_depth_1 = Image[((Depth // 2) - 1):((Depth // 2) + 1), :((Height // 2)), :((Width // 2))];
        CHUNK_depth_2 = Image[((Depth // 2) - 1):((Depth // 2) + 1), ((Height // 2)):Height, :((Width // 2))];
        CHUNK_depth_3 = Image[((Depth // 2) - 1):((Depth // 2) + 1), :((Height // 2)), ((Width // 2)):Width];
        CHUNK_depth_4 = Image[((Depth // 2) - 1):((Depth // 2) + 1), ((Height // 2)):Height, ((Width // 2)):Width];

        #CHUNK_depth = Image[((Depth // 2) - 1):((Depth // 2) + 1), :, :];
        #CHUNK_height = Image[:, ((Height // 2) - 1):((Height // 2) + 1), np.r_[:((Width // 2) - 1), ((Width // 2) + 1):Width]];
        #CHUNK_depth = Image[((Depth // 2) - 1):((Depth // 2) + 1), np.r_[:((Height // 2) - 1), ((Height // 2) + 1):Height], np.r_[:((Width // 2) - 1), ((Width // 2) + 1):Width]];
        
        #print(f"Chunks between Width = {CHUNK_width}: Cut : {((Width // 2) - 1)}, {((Width // 2) + 1)}");
        #print(f"Chunks between Height 1 = {CHUNK_height_1}");
        #print(f"Chunks between Height 2 = {CHUNK_height_2}");

        #print(f"Chunks between depth 1 = {CHUNK_depth_1}");
        #print(f"Chunks between depth 2 = {CHUNK_depth_2}");
        #print(f"Chunks between depth 3 = {CHUNK_depth_1}");
        #print(f"Chunks between depth 4 = {CHUNK_depth_2}");

        Sub_volumes_CHUNKS.append(CHUNK_width);

        Sub_volumes_CHUNKS.append(CHUNK_height_1);
        Sub_volumes_CHUNKS.append(CHUNK_height_2);

        Sub_volumes_CHUNKS.append(CHUNK_depth_1);
        Sub_volumes_CHUNKS.append(CHUNK_depth_2);
        Sub_volumes_CHUNKS.append(CHUNK_depth_3);
        Sub_volumes_CHUNKS.append(CHUNK_depth_4);

        return Sub_volumes_CHUNKS'''

    def save_to_csv_Enclosing_surface(self, 
                              Combinations_data : Union[np.ndarray, list], 
                              Enclosing_surface_data : Union[np.ndarray, list]
                              ) -> None:
        """
        Save the combinations and Enclosing_surface values to a CSV file.

        Parameters:
        -----------
        Combinations_data : Union[np.ndarray, list]
            The array or list of combinations to be saved.
        Enclosing_surface_data : Union[np.ndarray, list]
            The array or list of Enclosing_surface values.
        """

        _Is_list = False;
    
        if isinstance(Combinations_data, list) and isinstance(Enclosing_surface_data, list):
            _Is_list = True;       
        
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

                    Base_name = f"Combinations_And_Enclosing_surface_{self.Basepath}_async.csv";

                    print(f"Combinations_And_Enclosing_surface_{self.Basepath}_async.csv");

                    # * Save the DataFrame to a CSV file
                    File_path = os.path.join(Config.Folder_data, Base_name);
                    Dataframe_combination.to_csv(File_path, index=False);
                
            print(f"Combinations and Enclosing_surface values saved to {File_path}");
        
        except Exception as e:
            print(f"An error occurred while saving to CSV: {e}")

    #@Timer.timer(Config.Folder_logs, Config.OH_name)
    def process_octovoxel(self, 
                          CHUNK : np.ndarray, 
                          STORAGELIST : List[np.ndarray]):
        """
        Process a sub-volume of octovoxel and return combinations and Enclosing_surface value.

        Parameters:
        -----------
        CHUNK : np.ndarray
            Sub-volume of octovoxel.
        STORAGELIST : np.ndarray
            Numpy array representation of the binary storage list.

        Returns:
        -------
        Tuple[np.ndarray, int]
            Combinations array and Enclosing_surface value.
        """
        
        # * Reshape the array to a 3D array based on the calculated height.

        Combinations = int(Config.Byte_binary, 2);
        
        # * Create an array to store Combinations_int and initialize it with zeros.
        Combinations_int = np.zeros((Combinations), dtype='int');
        
        for i in range(CHUNK.shape[0] - 1):
            for j in range(CHUNK.shape[1] - 1):
                for k in range(CHUNK.shape[2] - 1):
                    for index in range(len(STORAGELIST)):
                        if np.array_equal(np.array(CHUNK[i:Config.Octovoxel_size + i, 
                                                         j:Config.Octovoxel_size + j, 
                                                         k:Config.Octovoxel_size + k]), 

                                        np.array(STORAGELIST[index])):                       
                            
                            Combinations_int[index] += 1;

                            #print(Combinations_int)

        return Combinations_int
    
    @Timer.timer()
    @multiprocessing_info 
    def get_array_multiprocessing(self, Depth : int, Height : int, Width : int):
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
                Enclosing_surface_all = [];
            
                # * Filter the list to include only .txt files
                Files = os.listdir(self.Path);
                
                print(f"Processing file... Total : {len(Files)}");

                for i, File in enumerate(Files):

                    File_path = os.path.join(self.Path, File);
                    Arrays = DataLoader.load_data(File_path);
                    Arrays = Arrays.reshape(Depth, Height, Width);
                    Enclosing_surface = calculate_enclosing_surface(Arrays);

                    print(f"{i} ---- {File_path}");

                    CHUNKS = image_into_chunks(File_path, Depth, Height, Width);

                    with multiprocessing.Pool(processes=self.Num_processes) as pool:
                        # * Use starmap to pass both CHUNKS and STORAGELIST to process_octovoxel
                        Results = pool.starmap_async(self.process_octovoxel, [(CHUNK, self.STORAGELIST) for CHUNK in CHUNKS]);
                        
                        Data = Results.get();

                        # * Extract Results and Enclosing_surface from the list of results
                        Combination = zip(*Data);

                        #print(Combination);

                    Result_combination = np.sum(Combination, axis=0);

                    Combinations_all.append(Result_combination);
                    Enclosing_surface_all.append(Enclosing_surface);
                    
                self.save_to_csv_Enclosing_surface(Result_combination, Enclosing_surface);

                return Result_combination, Enclosing_surface

            else:
                
                Arrays = DataLoader.load_data(self.Path);
                Arrays = Arrays.reshape(Depth, Height, Width);
                Enclosing_surface = calculate_enclosing_surface(Arrays);
                
                CHUNKS = image_into_chunks(self.Path, Depth, Height, Width);

                with multiprocessing.Pool(processes=self.Num_processes) as pool:
                    # * Use starmap to pass both CHUNKS and STORAGELIST to process_octovoxel
                    Results = pool.starmap_async(self.process_octovoxel, [(CHUNK, self.STORAGELIST) for CHUNK in CHUNKS]);
                    
                    Data = Results.get();

                    # * Extract Results and Enclosing_surface from the list of results
                    Combination = zip(*Data);

                    #print(Combination);

                Result_combination = np.sum(Combination, axis=0);

                self.save_to_csv_Enclosing_surface(Result_combination, Enclosing_surface);

                return Result_combination, Enclosing_surface        

        except Exception as e:
            print(f"Error on the multiprocessing function: {e}")
