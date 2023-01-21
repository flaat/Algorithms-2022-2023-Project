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


def sort_data(data) -> list[Tuple[str, float]]:
    """
    This function sorts the cryptocurrencies first in alphabetical order, and,
    then, for each of them, it performs a sort according to the day of monitoring.
    
    It is forbidden to use any kind of libraries such as Pandas, or functions like
    list.sort()!
    
    Parameters:
    :data: A data structure containing all the information about the cryptos
    
    @return: A sorted list of tuples containing (crypto name, price)
    """

    # TODO: Implement here your solution

    return None


def get_max_value(data, crypto: str, period: Tuple[int,int]) -> Tuple[int, float]:
    """
    This function must return the maximum value for a given crypto.
    
    Parameters:
    
    :data: A data structure containing the values for price or volume of a given crypto
    
    @return: A tuple containing the day in which the crypto reached the maximum value,
             along with the maximum value for that crypto
    """

    # TODO: Implement here your solution

    return (None, None)


def search(data, value: float, crypto: str) -> Tuple[int, float]:
    """
    This function searches for a specific value in a given data series and
    returns a tuple with the day and the value for a given cryptocurrency.
    If the searched value is not present in the data, the function returns the
    closest value. It compares two values of the data series, one at position i
    and the other at position j, and returns the value closest to the searched value.
    
    Parameters:
    :data: A data structure that contains the values of price and volume of all cryptos.
    :value: The value to be searched in the data.
    :crypto: The crypto name to search the value for.
    
    @return: A tuple containing the day on which the cryptocurrency reached the closest value
             and the closest value.
    """

    # TODO: Implement here your solution


    return (None, None)
