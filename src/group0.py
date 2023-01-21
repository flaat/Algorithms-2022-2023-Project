# Luiss - Management and Computer Science - Algorithm 2022/2023 
# Please fill the empty parts with your solution

import src.solutions.sorted_datasets as sol_datasets
from typing import Tuple


def read_file(file_path: str):
    """
    This function reads the dataset containg all the information about the 
    cryptocurrecies. The information are stored in a .txt file.
    
    Parameters:
    :file_path: The current path where the file you want to read is located
    
    @return: A data structure contining the information
    """

    # TODO: Implement here your solution

    return None

def crypto_stats(crypto_name: str, interval: Tuple[int, int]) -> Tuple[float, float, float]:
    """
    This function calculates the minimum, average, and maximum price values of a crypto
    whose name is passed in input within a specific period of time [a,b] passed
    in input.
    
    Parameters:
    :crypto_name: The name of the cryptocurrency to calculate statistics for
    :interval: The time interval consisting of a tuple of two values (a,b)
    
    @return: A tuple that contains the minimum, average, and maximum price values
    """
    
    # TODO: Implement here your solution
    
    return None


def sort_data(data) -> list[str]:
    """
    This function must implement a sorting algorithm among the one you studied during
    the course. It is forbidden to use any kind of libraries such as Pandas, or functions like
    list.sort()!
    
    Parameters:
    :data: A data structure containing all the information about the cryptos
    
    @return: A list of string containing all the dataset entries sorted by name, and by day
    """

    # TODO: Implement here your solution

    return None


def get_minimum_value(data) -> Tuple[int, float]:
    """
    This function must return the minimum value for a given crypto.
    
    Parameters:
    
    :data: A data structure containing the values for price or volume of a given crypto
    
    @return: A tuple containing the day in which the cripto reached the minimum value,
             along with the minimum value for that crypto
    """

    # TODO: Implement here your solution

    return (None, None)


def search(data, value) -> Tuple[int, float]:
    """
    This function takes as input the data series and the value to search and returns a 
    tuple containing the day and the value for a given crypto.
    If the value is not in data, then the function must return the closest value, this means that
    you have to return the value closer to param value, namely:
    if you have  d1 = |value - data[i]|, d2 = |value - data[j]| you have to choose the 
    argmin(d1, d2) (the element in position i if d1 < d2 the element in position d2 otherwise)
    :data: A data structure containing the values for price or volume of a given crypto
    :value: A value to search in data
    @return: A tuple containing the day in which the cripto reached the minimum value,
             along with the minimum value for that crypto
    """

    # TODO: Implement here your solution


    return (None, None)
