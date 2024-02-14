import os
import random
import numpy as np
import pandas as pd
from itertools import combinations

from src.Utils.Config import Config

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
    Random_numbers = [random.uniform(0, 1) for _ in range(2)]
    
    # * Normalize the numbers to ensure their sum is 1.0
    Total = sum(Random_numbers)
    Random_numbers = [value / Total for value in Random_numbers]
    
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
    Equal = np.array_equal(Array1, Array2)

    if(Equal):
        print("Arrays are equal.")
    else:
        # * Find the indices where the arrays differ
        Indices_of_differences = np.where(Array1 != Array2)

        print(f"Arrays are different at the following indices: {Indices_of_differences}")

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

    return File_extension.lower() == '.txt'

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

import numpy as np

def calculate_area(Image: np.ndarray) -> int:
    """
    Count the number of occurrences of '1' in an image stored in a .txt file.

    Parameters
    ----------
    Path : str
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

def calculate_perimeter(Binary_3d_image : np.ndarray) -> int:
    """
    Calculate the perimeter of 1-pixel regions in a 3D binary image.

    Parameters
    ----------
    binary_3d_image : np.ndarray
        3D binary image where 1 represents the region of interest.

    Returns
    -------
    int
        Total perimeter of the 1-pixel regions in the 3D image.
    """
    if Binary_3d_image.ndim != 3:
        raise ValueError("Input should be a 3D binary image.")

    Perimeter = 0

    # * Iterate through each voxel in the image
    for i in range(1, Binary_3d_image.shape[0] - 1):
        for j in range(1, Binary_3d_image.shape[1] - 1):
            for k in range(1, Binary_3d_image.shape[2] - 1):
                if(Binary_3d_image[i, j, k] == 1):
                    
                    Neighbors = [
                        Binary_3d_image[i - 1, j, k],
                        Binary_3d_image[i + 1, j, k],
                        Binary_3d_image[i, j - 1, k],
                        Binary_3d_image[i, j + 1, k],
                        Binary_3d_image[i, j, k - 1],
                        Binary_3d_image[i, j, k + 1]
                    ]

                    # * Count the number of neighboring 0s
                    Perimeter += sum(1 for Neighbor in Neighbors if Neighbor == 0)
    
    print("Perimeter of 1-pixel regions:", Perimeter)

    return Perimeter