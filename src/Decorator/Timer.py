import logging
import time
import os
from functools import wraps

from typing import Optional, Any

class Timer(object):

    # * Define a custom logger for the Timer class.
    logger = logging.getLogger("Timer");
    logger.setLevel(logging.DEBUG);

    """
    A class for timing the execution of functions and logging debugging prints with customizable log file names.

    Examples:
    ---------
    You can use this class to decorate functions and measure their execution time while logging to specific files:

    1. Timing a Function and Logging:
    
    # Decorate a function using the @Timer.timer decorator to measure execution time and log to a file.
    >>> @Timer.timer(folder="/path/to/logs")
    ... def my_func(x, y):
    ...    return np.add(x, y)

    # Call the decorated function.
    >>> my_func(np.array([1, 2, 3]), np.array([4, 5, 6]))
    

    2. Custom Log File Names:
    
    You can provide a custom log folder and class name when using the decorator:

    >>> @Timer.timer(folder="custom_logs", Class_name="MyClass")
    ... def another_func(a, b):
    ...     return a * b

    >>> another_func(10, 20)

    The decorator generates log files with names like "MyClass_another_func_Timer.log" in the "custom_logs" folder.

    Notes:
    -----
    This class decorator uses the `functools.wraps` decorator to preserve the metadata of the original function, such as the function name, docstring, and parameter information.

    Attributes:
    ----------
    None

    Methods:
    ----------
    timer(Folder: Optional[str] = 'Data\logs', Class_name: Optional[str] = None) -> Any
        A decorator function that measures the execution time of a function and logs debugging prints to a specified folder or the current working directory.

    Parameters:
    ----------
    Folder : str, optional, default: 'Data\logs'
        The folder where the log file should be saved.
    
    Class_name : str, optional, default: None
        The class name that is used for log file names. If provided, it is prepended to the function name in the log file names.

    Returns:
    ----------
    wrapper : function
        A function that executes the input function and prints the execution time.
    """
    
    @staticmethod  
    def timer(Folder: Optional[str] = 'Data\logs', Class_name=None) -> Any:
        """
        Decorator function that measures the execution time of a function and logs debugging prints to the specified folder, or to the current working directory if no folder is specified.

        Parameters:
        -----------
        func : function
            The function to be timed.
        folder : str, optional
            The folder where the log file should be saved.

        Returns:
        --------
        wrapper : function
            A function that executes the input function and prints the execution time.
        """
        def Inner(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                """
                Wrapper function that detects GPU availability and measures execution time.

                Parameters
                ----------
                args : tuple
                    Arguments to be passed to the decorated function.
                kwargs : dict
                    Keyword arguments to be passed to the decorated function.

                Returns
                -------
                Any
                    The return value of the decorated function.
                """
                
                Asterisk = 60;

                Log_app_name = f"{Class_name}_{func.__name__}_{__class__.__name__}.log";

                # * Create a logging handler that writes to a file.
                if(Folder is not None):
                    log_file_path = os.path.join(Folder, Log_app_name);

                File_handler = logging.FileHandler(log_file_path);
                File_handler.setLevel(logging.DEBUG);

                # * Configure the logger with a format and set the logging level to DEBUG.
                log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s';
                formatter = logging.Formatter(log_format);
                File_handler.setFormatter(formatter);
                
                # * Add the file handler to the Timer class logger.
                Timer.logger.addHandler(File_handler);

                Timer.logger.debug(f"Starting the execution of function {func.__name__}");
                
                Start_time = time.time();
                Result = func(*args, **kwargs);
                End_time = time.time();

                print("*" * Asterisk);
                print(f"Function {Class_name}_{func.__name__} executed in {End_time - Start_time:.4f} seconds.");
                print("*" * Asterisk);

                Timer.logger.debug(f"Function {func.__name__} executed in {End_time - Start_time:.4f} seconds.");

                # * Close the logging handler.
                File_handler.close();

                return Result
            return wrapper
        return Inner