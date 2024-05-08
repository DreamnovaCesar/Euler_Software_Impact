import os
import random
import numpy as np
import pandas as pd
from itertools import combinations

from src.Utils.Config import Config
from typing import Optional, Union, List, Tuple

from skimage import measure

def count_combinations(VIEW_CHUNK : np.ndarray, STORAGELIST_array : List[np.ndarray]) -> np.ndarray:
    """
    Count the number of combinations of elements in VIEW_CHUNK that match each element in STORAGELIST_array.

    Parameters
    ----------
    VIEW_CHUNK : np.ndarray
        6D array representing a chunk of data.
    STORAGELIST_array : List[np.ndarray]
        List of 6D arrays representing different storage lists.

    Returns
    -------
    np.ndarray
        1D array containing the count of combinations of elements in VIEW_CHUNK that match each element in STORAGELIST_array.
    """

    Combinations = len(STORAGELIST_array);
    Combinations_int = np.zeros((Combinations), dtype='int');

    for index in range(len(STORAGELIST_array)):
        Equal_mask = (VIEW_CHUNK == STORAGELIST_array[index]).all(axis=(3, 4, 5));
        Combinations_int[index] += Equal_mask.sum();

    return Combinations_int

def save_time_to_txt(File : str, Descriptor : str, _Class_ : str, Execution_time : int):
    """
    Save information to a log document.

    Parameters
    ----------
    File : str
        File to be saved.
    Descriptor : str
        Descriptor could be Enclosing surface, Contact surface, Volume, Euler.
    _Class_ : str
        Name of the class where the info is extracted.
    Execution_time : int
        The time to be saved.
    Filename : str, optional
        The name of the log document file. Default is 'log.txt'.

    Returns
    -------
    None

    Raises
    ------
    IOError
        If an error occurs while saving the information to the log document.

    Notes
    -----
    This function opens the specified log document file in append mode and writes
    the information in a specific format to the file.
    The information includes the File, Descriptor, Class, and Execution_time separated by spaces,
    followed by a newline character.
    Any errors that occur during the process are caught, and an IOError is raised.

    Examples
    --------
    >>> save_time_to_txt('example_file', 'Enclosing surface', 'ExampleClass', 10, 'mylog.txt')
    Log document successfully.
    """

    Filename = f'{File}_{Descriptor}{_Class_}.xtxt';

    try:
        # * Open the log file in append mode
        with open(Filename, 'a') as file:
            # * Write the float value to the file
            file.write(str(File), str(Descriptor), str(_Class_), str(Execution_time)  + '\n');
        print("Log document successfully.");
    except Exception as e:
        raise IOError("Error occurred while saving float value to log document: " + str(e));

def generate_random_numbers() -> list[int, int]:
    """
    Generate a list of random numbers such that their sum is always 1.0.
    
    This function creates a list of two random numbers between 0 and 1 and normalizes them to ensure their sum is 1.0.
    The generated list can be interpreted as the probabilities of 0 or 1 appearing in a 2D or 3D image.

    Returns:
    ----------
    list[int, int]
        A list of random numbers with a sum of 1.0.
        
    """
    # * Generate random numbers
    Random_numbers = [random.uniform(0, 1) for _ in range(2)];
    
    # * Normalize the numbers to ensure their sum is 1.0
    Total = sum(Random_numbers);
    Random_numbers = [value / Total for value in Random_numbers];
    
    return Random_numbers

def are_arrays_equal(Array1 : np.ndarray, Array2 : np.ndarray) -> tuple[bool, tuple]:
    """
    Check if two NumPy arrays are equal.

    Parameters
    -----------
    Array1 : numpy.ndarray 
        First NumPy array.
    Array2 : numpy.ndarray 
        Second NumPy array.

    Returns:
    ----------
    bool 
        True if arrays are equal, False otherwise.
    tuple 
        Indices where arrays differ if not equal.
    """
    # * Check if arrays are equal
    Equal = np.array_equal(Array1, Array2);

    if(Equal):
        print("Arrays are equal.");
    else:
        # * Find the indices where the arrays differ
        Indices_of_differences = np.where(Array1 != Array2);

        print(f"Arrays are different at the following indices: {Indices_of_differences}");

    return Equal, Indices_of_differences

def is_txt_file(file_path : str) -> bool:
    """
    Check if a file has a .txt extension.

    Parameters
    -----------
    File_path : str
        The path to the file.

    Returns:
    ----------
    bool
        True if the file has a .txt extension, False otherwise.
    """
    _, File_extension = os.path.splitext(file_path);
    print(f"Is the file a .txt format?");

    return File_extension.lower() == '.txt';

def concatenate_csv_files(Files: dict, Descriptor : str) -> None:
    """
    Concatenate and save combinations of CSV files.

    Parameters
    ----------
    files : dict
        A dictionary where keys are bit lengths and values are corresponding CSV file paths.

    Returns
    -------
    None
    """

    # * Read CSV files into a list of DataFrames
    Dataframes = [pd.read_csv(file_path) for file_path in Files.values()];
    Dataframes_names = [str(name) for name in Files.keys()];

    for length in range(2, len(Dataframes) + 1):

        # *Get all combinations of DataFrame pairs
        DF_combinations = list(combinations(Dataframes, length));
        Dataframes_files = list(combinations(Dataframes_names, length));

        # *Concatenate and save the combinations
        for i, (names, combination) in enumerate(zip(Dataframes_files, DF_combinations)):

            Concatenated_df = pd.concat(combination, axis=0);

            Dataframe_name = '_'.join(names) + f"_{Descriptor}_concatenated.csv";
            Dataframe_folder = os.path.join(Config.Folder_data, Dataframe_name);
            
            Concatenated_df.to_csv(Dataframe_folder, index=False);
            print(Dataframe_folder);

def calculate_volume(Image: np.ndarray) -> int:
    """
    Count the number of occurrences of '1' in an image stored in a .txt file.

    Parameters
    ----------
    Image : str
        The file path to the .txt file containing the image data.

    Returns
    -------
    int
        The number of occurrences of '1' in the image.

    Examples
    --------
    >>> file_path = 'path/to/your/file.txt'
    >>> count_ones_in_image(file_path)
    42
    """

    try:
        # * Read image data from the specified file
        #Image = np.loadtxt(Path, delimiter=',');

        # * Count the number of 1s
        Count_ones = np.sum(Image == 1);

        return Count_ones
    
    except Exception as e:
        raise ValueError(f"Error loading image data: {e}") from e

def calculate_enclosing_surface(Image : np.ndarray) -> int:
    """
    Calculate the Enclosing_surface of 1-pixel regions in a 3D Binary image.

    Parameters
    ----------
    Image : np.ndarray
        3D Binary image where 1 represents the region of interest.

    Returns
    -------
    int
        Total Enclosing_surface of the 1-pixel regions in the 3D image.
    """
    if Image.ndim != 3:
        raise ValueError("Input should be a 3D Binary image.")

    Enclosing_surface = 0;

    # * Iterate through each voxel in the image
    for i in range(1, Image.shape[0] - 1):
        for j in range(1, Image.shape[1] - 1):
            for k in range(1, Image.shape[2] - 1):
                if(Image[i, j, k] == 1):
                    
                    Neighbors = [
                        Image[i - 1, j, k],
                        Image[i + 1, j, k],
                        Image[i, j - 1, k],
                        Image[i, j + 1, k],
                        Image[i, j, k - 1],
                        Image[i, j, k + 1]
                    ];

                    # * Count the number of neighboring 0s
                    Enclosing_surface += sum(1 for Neighbor in Neighbors if Neighbor == 0);
    
    #print("Enclosing surface of 1-pixel regions:", Enclosing_surface)

    return Enclosing_surface

def calculate_contact_surface(Image : np.ndarray) -> int:
    """
    Calculate the Enclosing_surface of 1-pixel regions in a 3D Binary image.

    Parameters
    ----------
    Image : np.ndarray
        3D Binary image where 1 represents the region of interest.

    Returns
    -------
    int
        Total Enclosing_surface of the 1-pixel regions in the 3D image.
    """
    if Image.ndim != 3:
        raise ValueError("Input should be a 3D Binary image.")

    Contact_surface = 0;

    # * Iterate through each voxel in the image
    for i in range(1, Image.shape[0] - 1):
        for j in range(1, Image.shape[1] - 1):
            for k in range(1, Image.shape[2] - 1):
                if(Image[i, j, k] == 1):
                    
                    Neighbors = [
                        Image[i - 1, j, k],
                        Image[i + 1, j, k],
                        Image[i, j - 1, k],
                        Image[i, j + 1, k],
                        Image[i, j, k - 1],
                        Image[i, j, k + 1]
                    ];

                    # * Count the number of neighboring 0s
                    Contact_surface += sum(1 for Neighbor in Neighbors if Neighbor == 1);
    
    #print(" Contact surface of 1-pixel regions:", Contact_surface)

    return Contact_surface

def calculate_numbers_objects(Binary_image_3d: np.ndarray) -> int:
    """
    Analyzes a 3D Binary image and calculates the number of objects.

    Attributes:
    -----------
    Binary_image_3d : np.ndarray
        The 3D binary image to be analyzed.

    Returns:
    --------
    int:
        A list containing labels of detected objects.
    """

    # * Label connected components
    Labeled_image = measure.label(Binary_image_3d, connectivity=3);

    # * Analyze labeled components
    Properties = measure.regionprops(Labeled_image);

    # * Extract objects and analyze Properties
    Object_properties = [prop for prop in Properties if prop.label != 0]  # Exclude background label (0)

    for _, obj in enumerate(Object_properties):
      print(f"Objects : {obj.label}");

    # * Extract labels of detected objects
    Objects = obj.label;

    return Objects

def calculate_numbers_cavities(Binary_image_3d: np.ndarray) -> int:
    """
    Analyzes a 3D Binary image and calculates the number of cavities.

    Attributes:
    -----------
    Binary_image_3d : np.ndarray
        The 3D Binary image to be analyzed.

    Returns:
    --------
    int:
        A list containing labels of detected Cavities.
    """
    # * Invert Binary image
    Binary_image_3d_inverted = np.logical_not(Binary_image_3d);

    # * Label connected components
    Labeled_image = measure.label(Binary_image_3d_inverted, connectivity=3);

    # * Analyze labeled components
    Properties = measure.regionprops(Labeled_image);

    # * Extract Cavities and analyze Properties
    Cavities_properties = [prop for prop in Properties if prop.label != 0]  # Exclude background label (0)

    for _, obj in enumerate(Cavities_properties):
      print(f"Cavities : {obj.label}");

    # * Extract labels of detected Cavities
    Cavities = obj.label;

    return Cavities

def calculate_numbers_tunnels(Binary_image_3d: np.ndarray, Euler: int) -> int:
    """
    Analyzes a 3D Binary image and calculates the number of tunnels.

    Attributes:
    -----------
    Binary_image_3d : np.ndarray
        The 3D Binary image to be analyzed.
    Euler : int
        Euler characteristic of the binary image.

    Returns:
    --------
    int:
        The number of tunnels detected in the binary image.
    """
    Objects = calculate_numbers_objects(Binary_image_3d);
    Cavities = calculate_numbers_cavities(Binary_image_3d);

    Tunnels = (Objects + Cavities - Euler);

    return Tunnels

def save_to_csv(Main_dest_path : str,
                Folder_read : str,
                Descriptor : str,
                Combinations_data : Union[np.ndarray, list], 
                Descriptor_data : Union[np.ndarray, list]) -> None:
        """
        Save combinations and Descriptor_data values to a CSV file.

        Parameters
        ----------
        Main_Main_dest_path : str
            The destination path where the CSV file will be saved.
        Folder_read : str
            Folder to extract the images to be read
        Descriptor : str
            The descriptor to be added as a column in the CSV file.
        Combinations_data : Union[np.ndarray, list]
            Either a NumPy array or a list containing combinations data.
        Descriptor_data : Union[np.ndarray, list]
            Either a NumPy array or a list containing Descriptor data (Euler, Enclosing Surface, Contact Surface, and Volume).
        """

        Basepath = os.path.basename(Folder_read);

        _Is_list = False;
    
        if isinstance(Combinations_data, list) and isinstance(Descriptor_data, list):
            _Is_list = True;       
        
        Dataframe_completed = pd.DataFrame();

        try:
            
            if(_Is_list):

                for _, (Combination, Descriptor_) in enumerate(zip(Combinations_data, Descriptor_data)):
                    
                    print(f"Combinations len {Combination.shape[0]}");
                    
                    Combination = Combination.reshape((1, Combination.shape[0]));

                    print(f"Combinations len reshape {Combination.shape[0]}, {Combination.shape[1]}");
                    print(f"Rows : {Combination.shape[0]} ------ Columns : {Combination.shape[1]}");

                    # * Convert the combinations array to a Pandas DataFrame
                    Dataframe_combination = pd.DataFrame(Combination, columns=[f"Pattern {i+1}" for i in range(Combination.shape[1])]);

                    # * Add the Descriptor column to the DataFrame
                    Dataframe_combination[Descriptor] = Descriptor_;

                    # * Append the new data to the DataFrame
                    Dataframe_completed = pd.concat([Dataframe_completed, Dataframe_combination], ignore_index=True);
                    
                    print(Dataframe_completed);
                
                # * Check if the folder exists, create it if not
                if not os.path.exists(Main_dest_path):
                    os.makedirs(Main_dest_path);

                Base_name = f"Folder_Combinations_And_{Descriptor}_{Basepath}.csv";
                print(Base_name);

                # * Save the DataFrame to a CSV file
                File_path = os.path.join(Main_dest_path, Base_name);
                Dataframe_completed.to_csv(File_path, index=False);

            else:   
                    Combination = Combinations_data;
                    Descriptor_ = Descriptor_data;

                    print(f"Combinations len {Combination.shape[0]}");
                    Combination = Combination.reshape((1, Combination.shape[0]));
                    print(f"Combinations len reshape {Combination.shape[0]}, {Combination.shape[1]}");
                    print(f"Rows : {Combination.shape[0]} ------ Columns : {Combination.shape[1]}");

                    # * Convert the combinations array to a Pandas DataFrame
                    Dataframe_combination = pd.DataFrame(Combination, columns=[f"Pattern {i+1}" for i in range(Combination.shape[1])]);

                    # * Add the Descriptor column to the DataFrame
                    Dataframe_combination[Descriptor] = Descriptor_;

                    print(Dataframe_combination);
                
                    # * Check if the folder exists, create it if not
                    if not os.path.exists(Main_dest_path):
                        os.makedirs(Main_dest_path);

                    Base_name = f"Combinations_And_{Descriptor}_{Basepath}.csv";
                    print(Base_name);

                    # * Save the DataFrame to a CSV file
                    File_path = os.path.join(Main_dest_path, Base_name);
                    Dataframe_combination.to_csv(File_path, index=False);
                
            print(f"Combinations and {Descriptor} values saved to {File_path}");
        
        except Exception as e:
            print(f"An error occurred while saving to CSV: {e}");