# Luiss - Management and Computer Science - Algorithm 2022/2023 
# Please fill the empty parts with your solution
from typing import Tuple, List, Dict

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

def crypto_stats(data, crypto_name: str, interval: Tuple[int, int]) -> Tuple[float, float, float]:
    """
    This function calculates the minimum, average, and maximum price values of a crypto
    whose name is passed in input within a specific period of time [a,b] passed
    in input. Notice that [a,b] can be an interval that might exceed the actual monitoring
    time of the crypto given in input.
    
    If any error occurs, return the default value (0.0, 0.0, 0.0)
    
    Parameters:
    :data: The data structure used to calculate the statistics
    :crypto_name: The name of the cryptocurrency to calculate statistics for
    :interval: The time interval consisting of a tuple of two values (a,b)
    
    @return: A tuple that contains the minimum, average, and maximum price values
    """
    # TODO: Implement here your solution
    return (None, None, None)


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
    This function must return the maximum price for a given crypto in
    a specific month.
    
    Parameters:
    
    :data: A data structure containing the information about the cryptos.
    :crypto: The crypto for which to search the maximum value.
    :month: The month in which to search for the maximum value.
    
    Assumption: each month contains 30 days. Notice that the month can be
    a natural number in [1,inf). Example the 13th month represents the first
    month of the second year of monitoring; the 14th month represents the
    second month of the second year of monitoring, and so on.
    
    @return: A tuple containing the day in which the crypto reached the maximum price,
             along with the maximum value for that crypto
    """

    # TODO: Implement here your solution
    return None, None


def search(data, value: float, crypto: str) -> Tuple[int, float]:
    """
    This function searches for a specific price in a given data series and
    returns a tuple with the day and the price for a given cryptocurrency.
    If the searched value is not present in the data, the function returns the
    closest price. It compares two values of the data series, one at position i
    and the other at position j, and returns the price closest to the searched value.
    
    N.B.: If you have more than one possible day whose corresponding price is closest
    to the value in input, return the minimum day.
    
    Parameters:
    :data: A data structure that contains the value of price and volume of all cryptos.
    :value: The price value to be searched in the data.
    :crypto: The crypto name to search the value for.
    
    @return: A tuple containing the day on which the cryptocurrency reached the closest price
             and the closest price.
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
                                interval: Tuple[int,int]) -> Tuple[Dict[str, List[str]], List[str]]:
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
               
    @return: A tuple of key-value pairs where:
        the key is the minimal correlation pathways tree
        the value is a list of cryptocurrencies correlated at the k-th level
    """
    # TODO: Implement here your solution
    
    return (min_correlation_pathways(data, crypto, interval), None)