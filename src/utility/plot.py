# If you want to visualize the data series you can use the plot function
# defined here

import matplotlib.pyplot as plt


COLORS = ["r", "g", "b", "m", "c"]
LINE_STYLES = []

FONT_SIZE = 14
LEGEND_SIZE = 14

X_LABEL = "Days"
Y_LABEL = { "price" : "Price (US Dollars)", 
            "volume": "Volume (US Dollars)"}

def plot_data(data_series: dict, dependent_variable: str) -> None:
    """
    This function plots at most 5 data series given in the parameter data_series.
    It is important that you pass to the function the data series associated with the dependent variable.
    For example: if you pass to the function a data series representing the volume but you use
    dependent_variable = \"price\", then you will obtain a plot with the wrong x axis label!
    :data_series: A dict formatted as follows: 
                    {
                            \"crypto_name_1\" : 1.2443, 1.542, 2.5432, ...],
                            \"crypto_name_2\" : 12.2443, 11.542, 10.5432, ...],
                            ... : ...
                    } 
    :dependent_variable: A string that can have two values: \"price\" or \"volume\"
    @return: None
    """

    check_dependent_variable(dependent_variable)

    check_data_series_length(data_series)

    data_series_length = len(list(data_series.values())[0])

    x_values = [day for day in range(1, data_series_length+1)]

    for index, (crypto_name, data) in enumerate(data_series.items()):

        plt.plot(x_values, data, label=crypto_name, color=COLORS[index])

    plt.xlabel(X_LABEL, fontsize=FONT_SIZE)
    plt.ylabel(Y_LABEL[dependent_variable], fontsize=FONT_SIZE)
    plt.yticks(fontsize=FONT_SIZE)
    plt.xticks(fontsize=FONT_SIZE)
    plt.grid(color='black', linestyle='-', linewidth=0.1)
    plt.legend(loc="upper right", fontsize=FONT_SIZE)
    plt.tight_layout()
    plt.show()


def check_dependent_variable(dependent_variable: str) -> bool:
    """
    Check if the dependent variable has one of the value allowed
    :dependet_variable: A string that can have two values: "price" or "volume"
    @return: True if the dependent_variable parameters is ok, otherwise it raises an exception
    """
    if dependent_variable != "price" and dependent_variable != "volume":

        raise Exception(f"check_data_series_length function: Attention, dependent_variable must be equal to \"price\" or \"volume\"!")

def check_data_series_length(data_series: dict) -> bool:
    """
    This function check if the data series have the same length
    :data_series: A dict formatted as follows: 
                        {
                            "crypto_name_1" : 1.2443, 1.542, 2.5432, ...],
                            "crypto_name_2" : 12.2443, 11.542, 10.5432, ...],
                            ... : ...
                        } 
    @return: True, if all the data series have the same length. Otherwise the method raise an exception
    """

    if len(data_series) > 5:

        raise Exception(f"check_data_series_length function: Attention, you cannot plot more than 5 data series!")

    data_series_length = len(list(data_series.values())[0])

    for _, data in data_series.items():

        if len(data) != data_series_length:

            raise Exception(f"check_data_series_length function: Attention, the data series passed to plot_data have different dimensions {data_series_length} and {len(data)}")

    return True



if __name__ == "__main__":

    import random


    test_dict = {
        "bitcoin": [random.randrange(160, 210) for i in range(0, 100)],
        "algorand": [random.randrange(46, 140) for i in range(0, 100)] 
    }

    plot_data(data_series=test_dict, dependent_variable="price")