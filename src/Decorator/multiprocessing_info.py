
import psutil
import platform
import multiprocessing
from functools import wraps

def multiprocessing_info(func):
    """
    Decorator to gather multiprocessing information and append it to the result of a function.

    Parameters:
    -----------
    func : function
        The function to be decorated.

    Returns:
    --------
    function
        The decorated function.

    Example:
    ---------
    @multiprocessing_info
    def my_function():
        # Your function logic here
        return result
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        Wrapper function to gather multiprocessing information and append it to the result.

        Returns:
        --------
        dict
            A dictionary containing the result of the decorated function along with multiprocessing information.
        """

        # * Get multiprocessing information
        Hardware = psutil.cpu_count(logical=False);
        CPU_count = multiprocessing.cpu_count();
        CPU_name = platform.processor();
        Machine = platform.machine();
        System = platform.system();
        Version = platform.version();
        Compiler = platform.python_compiler();

        # * Execute the original function
        Result = func(*args, **kwargs);

        # * Append multiprocessing information to the result
        result_with_info = {
            'hardware': Hardware,
            'CPU count': CPU_count,
            'CPU': CPU_name,
            'machine': Machine,
            'compiler': Compiler,
            'system': System,
            'version': Version
        };

        print(result_with_info);
        
        return Result

    return wrapper