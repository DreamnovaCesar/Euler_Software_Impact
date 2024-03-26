import numpy as np

from src.Utils.Config import Config
from src.Utils.ConvertionDecimalBinaryByte import ConvertionDecimalBinaryByte

class ByteStorage:
    """
    A class for creating a list of binary arrays and converting it to a NumPy array.

    Methods
    -------
    to_numpy_array() -> np.ndarray:
        Convert a list of binary arrays to a NumPy array.

    Parameters
    ----------
    Convertion_object : ConvertionDecimalBinaryByte
        An object of a class that implements the `convertion_system` method.

    Attributes
    ----------
    Convertion_object : object
        The object implementing the `convertion_system` method used for binary conversion.

    Methods
    -------
    to_numpy_array() -> np.ndarray:
        Convert a list of binary arrays to a NumPy array.

    Notes
    -----
    This class allows you to create and manipulate binary arrays using the provided conversion system.

    """
    BINARYBYTE = ConvertionDecimalBinaryByte;
    
    # * Class description
    @classmethod
    def __str__(cls) -> str:
        """
        Return a string description of the object.

        Returns:
        ----------
        None
        """
        return f'''{cls.__class__.__name__}: A class for creating a list of binary arrays and converting it to a NumPy array.''';

    # * Deleting (Calling destructor)
    @classmethod
    def __del__(cls) -> None:
        """
        Destructor called when the object is deleted.

        Returns:
        ----------
        None
        """
        print(f'Destructor called, {cls.__class__.__name__} class destroyed.');
    
    @classmethod
    def to_numpy_array(cls) -> np.ndarray:
        """
        Convert a list of binary arrays to a NumPy array.

        Returns
        -------
        np.ndarray
            A NumPy array containing the binary arrays.

        Raises
        ------
        ValueError
            If the `Convertion_object` is not an instance of `ConvertionDecimalBinaryByte`.

        """
        try:

            # * Initialize a list to store binary arrays
            Storage_list = [];

            # * Define Byte_binary and Decimal_number
            Decimal_number = int(Config.Byte_binary, 2);

            # * Loop through the range of numbers from 0 to Decimal_number - 1
            for i in range(Decimal_number):
                # * Call the convertion_system method of the Convertion_object
                Binary_array = cls.BINARYBYTE.convertion_system(i);
                
                # * Convert the Binary_array to a list and append to Storage_list
                Binary_array = Binary_array.tolist();
                Storage_list.append(Binary_array);

            # * Convert the list of binary arrays to a NumPy array and return it
            Storage_list = np.array(Storage_list);

            return Storage_list
        except ValueError as e:
            # * Handle the exception by printing an error message or taking appropriate action
            print(f"Error: {e}");
        return None