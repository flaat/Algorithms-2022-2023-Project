# Luiss - Management and Computer Science - Algorithm 2022/2023 
# Please fill the empty parts with your solution

import src.solution_evaluation.sorted_datasets as sol_datasets
from typing import Tuple, List, Dict
import pandas as pd

def read_file(file_path: str) -> any:
    """
    This function reads the dataset containg all the information about the 
    cryptocurrecies. The information are stored in a .txt file.
    
    Parameters:
    :file_path: The current path where the file you want to read is located
    
    @return: A data structure contining the information of the crypto
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


def sort_data(data) -> List[Tuple[str, float]]:
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


def get_max_value(data, crypto: str, month: int) -> Tuple[int, float]:
    """
    This function must return the maximum value for a given crypto in
    a specific month.
    
    Parameters:
    
    :data: A data structure containing the values for price or volume
           of a given crypto.
    :crypto: The crypto for which to search the maximum value.
    :month: The month in which to search for the maximum value.
    
    Assumption: each month contains 30 days.
    
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


def min_correlation_pathways(data,
                             crypto: str,
                             interval: Tuple[int,int]) -> Dict[str, List[str]]:
    """
    This function builds a minimal correlation pathways tree on the given
    data structure for a specific cryptocurrency in a designated temporal
    period. For each node x, the sum of the weights in the path from the root
    to x must be minimal.
    
    Parameters:
    :data: A data structure that contains the information of all cryptos.
    :crypto: The crypto name for which to build the tree.
    :interval: The temporal period for which to build the tree.
               It's in the form [x,y] where x is the beginning time and y is the end
               time.
               
    @return: The minimal correlation pathways tree
    """
    # TODO: Implement here your solution
    
    return None


def correlated_cryptos_at_lvl_k(data,
                                crypto: str,
                                level: int,
                                interval: Tuple[int,int]) -> List[str]:
    """
    This function retrieves the cryptocurrencies related to the one given in input
    at a particular level of correlation in a designated temporal period [x,y].
    
    Parameters:
    :data: A data structure that contains the information of all cryptos.
    :crypto: The crypto name to search correlations for.
    :level: The level at which the correlated cryptos should stand at.
    :interval: The temporal period for which to build the correlation tree.
               It's in the form [x,y] where x is the beginning time and y is the end
               time.
               
    @return: A list of cryptocurrencies
    """
    # TODO: Implement here your solution

    
    return None
