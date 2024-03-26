import numpy as np

class ConvertionDecimalBinaryByte:
    
    @staticmethod
    def convertion_system(Value_to_convert: int) -> np.ndarray:
        """
        Convert a decimal value to its binary representation as an 8-bit numpy array.

        Parameters
        ----------
        Value_to_convert : int
            The decimal value to convert to binary. Should be in the range [0, 255].

        Returns
        -------
        numpy.ndarray
            An 8-bit numpy array representing the binary conversion of Value_to_convert.

        Raises
        ------
        ValueError
            If Value_to_convert is not in the range [0, 255].

        """
        try:
            if (Value_to_convert < 0 or Value_to_convert > 255):
                raise ValueError("Value_to_convert should be in the range [0, 255]");

            # * Conversion to int and binary
            Value_to_convert = int(Value_to_convert);
            Binary_value = format(Value_to_convert, '08b');

            Shape = (2,) * 3;
            Binary_array = [int(x) for x in Binary_value];
            Binary_array = np.reshape([Binary_array], Shape);

            return Binary_array;
    
        except ValueError as e:
            # * Handle the exception by printing an error message or taking other actions
            print(f"Error: {e}");
            return None