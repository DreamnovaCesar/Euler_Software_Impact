import time
from functools import wraps
from typing import Callable

class Timer(object):
    """
    A class for timing the execution of functions and logging debugging prints.

    Methods:
    --------
    timer() -> Callable:
        Decorator function that measures the execution time of a function.

    """

    @staticmethod
    def timer() -> Callable:
        """
        Decorator function that measures the execution time of a function and logs debugging prints.

        Returns:
        --------
        Callable
            A decorator function that measures the execution time of the input function and logs the results.

        """

        def Inner(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                """
                Wrapper function that detects GPU availability and measures execution time.

                Parameters:
                -----------
                args : tuple
                    Arguments to be passed to the decorated function.
                kwargs : dict
                    Keyword arguments to be passed to the decorated function.

                Returns:
                --------
                Any
                    The return value of the decorated function.
                """
                Asterisk = 60

                print(f"Starting the execution of function {func.__name__}")

                Start_time = time.time()
                Result = func(*args, **kwargs)
                End_time = time.time()

                print("*" * Asterisk)
                print(f"Function {func.__name__} executed in {End_time - Start_time:.4f} seconds.")
                print("*" * Asterisk)

                return Result

            return wrapper

        return Inner