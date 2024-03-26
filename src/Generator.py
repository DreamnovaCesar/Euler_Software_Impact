import os
import numpy as np
import multiprocessing

from abc import ABC
from abc import abstractmethod

from typing import Optional

class Generator(ABC):
    """
    An abstract class for generating and saving matrices.

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

    Methods:
    ----------
    create_matrix(Matrix_index)
        Abstract method to create a matrix and save it to a file.

    generate_matrices()
        Abstract method to generate matrices.

    Example:
    ----------
    >>> # Subclass and implement create_matrix and generate_matrices methods.
    >>> matrix_gen = ConcreteMatrixGenerator(Path='/path/to/matrices', Width=10, Height=10, Probabilities=[0.7, 0.3], Num_matrices=50, Num_processes=4)
    >>> matrix_gen.generate_matrices()
    """

    def __init__(self,
                 path: str,
                 width: int,
                 height: int,
                 probabilities: Optional[list] = [0.5, 0.5],
                 PR: Optional[bool] = True,
                 num_matrices: Optional[int] = 100,
                 num_processes: Optional[int] = (multiprocessing.cpu_count() // 2)
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

        self.Num_matrices = num_matrices;
        self.Num_processes = num_processes;

        Total_probability = sum(probabilities);

        self.Probabilities = probabilities;
        self.PR = PR;

        # * Use a small epsilon for floating-point comparisons
        if abs(Total_probability - 1.0) > 1e-10:
            raise ValueError("The sum of probabilities must be equal to 1.0.");

        if not isinstance(self.Num_matrices, int) or not isinstance(self.Num_processes, int):
            raise TypeError(f"Num_matrices {self.Num_matrices} or Num_processes {self.Num_processes} must be integers.");

        if self.Num_processes > multiprocessing.cpu_count() // 2:
            raise ValueError(f"Num_processes cannot be greater than half of the available CPU cores. Number of cores {multiprocessing.cpu_count() // 2}");

        print(f"Number of processors available: {multiprocessing.cpu_count() // 2}, You chose {self.Num_processes} processors");

        os.makedirs(self.Path, exist_ok=True);

    @abstractmethod
    def create_matrix(self, Matrix_index: int) -> tuple[np.ndarray, int]:
        """
        Abstract method to create a matrix and save it to a file.

        Parameters:
        ----------
        Matrix_index : int
            Index of the matrix.

        Returns:
        ----------
        tuple[np.ndarray, int]
            A tuple containing the generated matrix and the matrix index.
        """

    @abstractmethod
    def generate_matrices(self) -> None:
        """
        Abstract method to generate matrices.

        Returns:
        ----------
        None
        """
        pass