import time
from functools import wraps
from typing import Callable, Tuple

class Timer(object):
    """
    A class for timing the execution of functions and logging debugging prints.

    Methods:
    --------
    timer() -> Callable:
        Decorator function that measures the execution time of a function.

    """

    @staticmethod
    def timer(log_file: str = "Execution.log") -> Callable:
        """
        Decorator function that measures the execution time of a function and logs debugging prints.

        Parameters:
        -----------
        log_file : str, optional
            File path to save the log, by default "execution.log"

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
                Tuple
                    A tuple containing the return value of the decorated function and its execution time.
                """
                Asterisk = 60;

                with open(log_file, "a") as f:
                    f.write(f"Starting the execution of function {func.__name__}\n");

                Start_time = time.time();
                Result = func(*args, **kwargs);
                End_time = time.time();
                
                Execution_time = End_time - Start_time;

                with open(log_file, "a") as f:
                    f.write("*" * Asterisk + "\n");
                    f.write(f"Function {func.__name__} executed in {Execution_time:.4f} seconds.\n");
                    f.write("*" * Asterisk + "\n");

                return Result

            return wrapper

        return Inner