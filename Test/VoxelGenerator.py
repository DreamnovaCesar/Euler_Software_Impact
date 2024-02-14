import os
import numpy as np
import multiprocessing

from src.Decorator.TimerCMD import Timer
from src.Utils.Utils import  generate_random_numbers

from typing import Optional

class VoxelGenerator:
    """
    A class for generating and saving 3D matrices.

    Attributes:
    ----------
    Path : str
        The folder where generated matrices will be saved.
    Width : int
        The width of the 3D matrices.
    Height : int
        The height of the 3D matrices.
    Depth : int
        The depth of the 3D matrices.
    Probabilities : list, optional
        A list of two probabilities [p0, p1], where p0 is the probability of 0 and p1 is the probability of 1.
    PR : bool
        Bool value to generate a list of random numbers such that their sum is always 1.0.
    Num_matrices : int, optional
        The number of matrices to generate.
    Num_processes : int, optional
        The number of worker processes to use for matrix generation.

    Parameters:
    ----------
    Path : str
        The folder where generated matrices will be saved.
    Width : int
        The width of the 3D matrices.
    Height : int
        The height of the 3D matrices.
    Depth : int
        The depth of the 3D matrices.
    Probabilities : list, optional
        A list of two probabilities [p0, p1], where p0 is the probability of 0 and p1 is the probability of 1.
    Num_matrices : int, optional
        The number of matrices to generate.
    Num_processes : int, optional
        The number of worker processes to use for matrix generation.

    Methods:
    ----------
    create_matrix(Matrix_index)
        Create a matrix and save it to a file.

    generate_matrices()
        Generate matrices in parallel using multiprocessing.
    
    >>> matrix_gen = VoxelGenerator(Path='/path/to/matrices', Depth=10, Width=10, Height=10, Probabilities=[0.7, 0.3], Num_matrices=50, Num_processes=4)
    >>> matrix_gen.generate_matrices()
    """

    def __init__(self, 
                 path : str, 
                 width : int,
                 height : int,
                 depth : int,
                 probabilities : Optional[list] = [0.5, 0.5],
                 PR : Optional[bool] = True,
                 num_matrices : Optional[int] = 100, 
                 num_processes : Optional[int] = (multiprocessing.cpu_count() // 2)
                 ) -> None:
        """
        Initialize the VoxelGenerator.

        Parameters:
        ----------
        path : str
            The folder where generated matrices will be saved.
        width : int
            The width of the 3D matrices.
        height : int
            The height of the 3D matrices.
        depth : int
            The depth of the 3D matrices.
        probabilities : list, optional
            A list of two probabilities [p0, p1], where p0 is the probability of 0 and p1 is the probability of 1.
        PR : bool
            Bool value to generate a list of random numbers such that their sum is always 1.0.
        num_matrices : int, optional
            The number of matrices to generate.
        num_processes : int, optional
            The number of worker processes to use for matrix generation.
        """

        self.Path = path;
        self.Width = width;
        self.Height = height;
        self.Depth = depth;
        
        self.Num_matrices = num_matrices;
        self.Num_processes = num_processes;

        Total_probability = sum(probabilities);
        
        self.Probabilities = probabilities;
        self.PR = PR;

        if abs(Total_probability - 1.0) > 1e-10:  # Use a small epsilon for floating-point comparisons
            raise ValueError("The sum of probabilities must be equal to 1.0.");

        if not isinstance(self.Num_matrices, int) or not isinstance(self.Num_processes, int):
            raise TypeError(f"Num_matrices {self.Num_matrices} or Num_processes {self.Num_processes} must be integers.")

        if(self.Num_processes > multiprocessing.cpu_count() // 2):
            raise ValueError(f"Num_processes cannot be greater than half of the available CPU cores. Number of cores {multiprocessing.cpu_count() // 2}")

        print(f"Number of processors available : {multiprocessing.cpu_count() // 2}, You chosen {self.Num_processes} processors");

        os.makedirs(self.Path, exist_ok=True);
    
    # * Class description
    def __str__(self) -> str:
        """
        Return a string description of the object.

        Returns:
        ----------
        str
            String description of the object.
        """
        return f'''{self.__class__.__name__}: A class for generating and saving matrices.''';

    # * Deleting (Calling destructor)
    def __del__(self) -> None:
        """
        Destructor called when the object is deleted.

        Returns:
        ----------
        None
        """
        print(f'Destructor called, {self.__class__.__name__} class destroyed.');

    #@Timer.timer(Config.Folder_logs, Config.Matrix_generator_name)
    def create_matrix(self, Matrix_index: int) -> tuple[np.ndarray, int]:
        """
        Create a 3D matrix and save it to a file.

        Parameters:
        ----------
        Matrix_index : int
            The index of the matrix.

        Returns:
        ----------
        Images_3D_edges : numpy.ndarray
            The generated matrix.
        Matrix_index : int
            The index of the matrix.
        """
        try:
            # * Check if PR is True, then use generated random numbers
            if self.PR:
                Probabilities = generate_random_numbers();
            else:
                Probabilities = self.Probabilities;

            # * Generate a 3D matrix of 0s and 1s based on probabilities
            Images_3D = np.random.choice([0, 1], size=(self.Width, self.Height, self.Depth), p=Probabilities).astype(np.uint8);

            # * Create a 3D matrix with an extra border of zeros
            Images_3D_edges = np.zeros((Images_3D.shape[0] + 2, Images_3D.shape[1] + 2, Images_3D.shape[2] + 2));
            Images_3D_edges[1:-1, 1:-1, 1:-1] = Images_3D;

            try:
                # * Construct the file name and path
                File_name = f"Matrix_voxels_{Matrix_index}.txt";
                self.Matrix_generator_file = os.path.join(self.Path, File_name);

                # * Flatten the 3D matrix and save it to a text file
                Flattened_array = Images_3D_edges.reshape((Images_3D_edges.shape[0] * Images_3D_edges.shape[1], Images_3D_edges.shape[2]));
                np.savetxt(self.Matrix_generator_file, Flattened_array, fmt='%0.0f', delimiter=',');

            except Exception as e:
                print(f"Error saving matrix {self.Matrix_generator_file}: {e}");

            # * Return the generated 3D matrix and its index
            return Images_3D_edges, Matrix_index

        except Exception as e:
            # Handle matrix creation error
            print(f"Error creating matrix {Matrix_index}: {e}");
            return None, Matrix_index
        
    def generate_matrices(self) -> None:
        """
        Generate matrices in parallel using multiprocessing.

        """
        try:

            Pool = multiprocessing.Pool(processes=self.Num_processes);
            Results = Pool.map(self.create_matrix, range(self.Num_matrices));
            Pool.close();
            Pool.join();
        except Exception as e:
            print(f"Error generating matrices: {e}")
