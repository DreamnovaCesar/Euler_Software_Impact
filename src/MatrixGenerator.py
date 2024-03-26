import os
import numpy as np
import multiprocessing

from src.Decorator.TimerCMD import Timer
from src.Decorator.multiprocessing_info import multiprocessing_info

from src.Utils.Utils import generate_random_numbers

from typing import Optional

from src.Generator import Generator

class MatrixGenerator(Generator):
    """
    A class for generating and saving matrices.

    Attributes:
    ----------
    Path : str
        The folder where generated matrices will be saved.
    Width : int
        The width of the 2D matrices.
    Height : int
        The height of the 2D matrices.
    Probabilities : list, optional
        A list of two probabilities [p0, p1], where p0 is the probability of 0 and p1 is the probability of 1.
    Num_matrices : int, optional
        The number of matrices to generate.
    Num_processes : int, optional
        The number of worker processes to use for matrix generation.
    Matrix_generator_folder : str
        The folder where generated matrices will be saved.
    Matrix_generator_file : str
        The file path for saving the current matrix.

    Parameters:
    ----------
    path : str
        The folder where generated matrices will be saved.
    width : int
        The width of the 2D matrices.
    height : int
        The height of the 2D matrices.
    probabilities : list, optional
        A list of two probabilities [p0, p1], where p0 is the probability of 0 and p1 is the probability of 1.
    PR : bool
        Bool value to generate a list of random numbers such that their sum is always 1.0.
    num_matrices : int, optional
        The number of matrices to generate.
    num_processes : int, optional
        The number of worker processes to use for matrix generation.

    Methods:
    ----------
    create_matrix(Matrix_index)
        Create a matrix and save it to a file.

    generate_matrices()
        Generate matrices in parallel using multiprocessing.

    Example:
    ----------
    >>> matrix_gen = MatrixGenerator(Path='/path/to/matrices', Width=10, Height=10, Probabilities=[0.7, 0.3], Num_matrices=50, Num_processes=4)
    >>> matrix_gen.generate_matrices()
    """

    def __init__(self, 
                 path : str, 
                 width : int,
                 height : int,
                 probabilities : Optional[list] = [0.5, 0.5],
                 PR : Optional[bool] = True,
                 num_matrices : Optional[int] = 100, 
                 num_processes : Optional[int] = (multiprocessing.cpu_count() // 2)
                 ) -> None:
        """
        Initialize the MatrixGenerator.

        Parameters:
        ----------
        path : str
            The folder where generated matrices will be saved.
        width : int
            The width of the 2D matrices.
        height : int
            The height of the 2D matrices.
        depth : int
            The depth of the 2D matrices.
        probabilities : list, optional
            A list of two probabilities [p0, p1], where p0 is the probability of 0 and p1 is the probability of 1.
        PR : bool
            Bool value to generate a list of random numbers such that their sum is always 1.0.
        num_matrices : int, optional
            The number of matrices to generate.
        num_processes : int, optional
            The number of worker processes to use for matrix generation.
        """
        
        super().__init__(path, width, height, probabilities, PR, num_matrices, num_processes);
    
    # * Class description
    def __str__(self) -> str:
        """
        Return a string description of the object.

        Returns:
        ----------
        None
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

    @Timer.timer()
    def create_matrix(self, Matrix_index: int) -> tuple[np.ndarray, int]:
        """
        Create a matrix and save it to a file.

        Parameters:
        ----------
        Matrix_index : int
            The index of the matrix.

        Returns:
        ----------
        Images_2D_edges : numpy.ndarray
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

            # * Generate a random matrix of 0s and 1s based on probabilities
            Images_2D = np.random.choice([0, 1], size=(self.Width, self.Height), p=Probabilities).astype(np.uint8);
            
            # * Create a matrix with an extra border of zeros
            Images_2D_edges = np.zeros((Images_2D.shape[0] + 2, Images_2D.shape[1] + 2));
            Images_2D_edges[1:-1, 1:-1] = Images_2D;

            try:
                # * Construct the file name and path
                File_name = f"Matrix_{Matrix_index}.txt";
                self.Matrix_generator_file = os.path.join(self.Path, File_name);

                # * Save the matrix to a text file
                with open(self.Matrix_generator_file, 'w') as file:
                    np.savetxt(file, Images_2D_edges, fmt='%0.0f', delimiter=',');

            except Exception as e:
                # * Handle file saving error
                print(f"Error saving matrix {self.Matrix_generator_file}: {e}");

            # * Return the generated matrix and its index
            return Images_2D_edges, Matrix_index

        except Exception as e:
            # * Handle matrix creation error
            print(f"Error creating matrix {Matrix_index}: {e}")
            return None, Matrix_index
        
    @Timer.timer()
    @multiprocessing_info
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
