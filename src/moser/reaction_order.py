import numpy as np
import itertools
import math

from read_file_and_enter_data import manual_or_read
from read_file_and_enter_data import spacing

from calculate_speed import display_graph
from tabulate import tabulate

def calculate_derivative(times, concentrations):
    """
    Calculate the derivative of concentration with respect to time.

    Args:
        times (list of float): A list containing time values.
        concentrations (list of float): A list containing corresponding concentration values.

    Returns:
        list of float: A list containing the derivative of concentration with respect to time.
    """
    
    # Calculate derivatives and other parameters based on concentration data
    
    derivatives = [(concentrations[i] - concentrations[i-1]) / (times[i] - times[i-1]) for i in range(1, len(times))]
    return derivatives

def calculate_differences(column):
    """
    Calculate the absolute differences between each pair of values in a column.

    Args:
        column (list): A list containing numerical values representing a column of data.

    Returns:
        list: A list containing the absolute differences between each pair of values in the column.

    Raises:
        None
    """
    differences = []
    for a, b in itertools.combinations(column, 2):
        if a is not None and b is not None:
            differences.append(abs(a - b))
    return differences

class TableAnalyzer:
    """
    Analyzes a table and performs statistical calculations on specified columns.

    Attributes:
        column_indices (list): Indices of columns to analyze for statistical properties.
    """
    column_indices = [2, 4, 6]

    def __init__(self, table):
        """
        Initializes a TableAnalyzer instance.

        Args:
            table (list of lists): The table to be analyzed, where each inner list represents a row.

        Returns:
            None

        Raises:
            None
        """
        self.table = table

    def remove_leading_zeros(self, value):
        """
        Removes leading zeros from a numerical value represented as a string.

        Args:
            value (str or None): The numerical value as a string.

        Returns:
            float: The numerical value without leading zeros, or 0 if value is None.

        Raises:
            None
        """
        if value is None:
            return 0
        str_value = str(value)
        str_value = str_value.lstrip('0')
        return float(str_value)

    def calculate_variance(self, column):
        """
        Calculates the coefficient of variation for a given column in the table.

        Args:
            column (list): The column of numerical values to calculate the coefficient of variation for.

        Returns:
            float: The coefficient of variation.

        Raises:
            None
        """
        column = [val for val in column if val is not None]
        if column:
            column = list(map(self.remove_leading_zeros, column))
            mean = sum(column) / len(column)
            variance = sum((val - mean) ** 2 for val in column) / len(column)
            standard_deviation = variance ** 0.5      
            coefficient_of_variation = (standard_deviation / mean) * 100
            return abs(coefficient_of_variation)
        else:
            return float('nan')

    def find_most_constant_column(self, column_indices):
        """
        Finds the column with the least variation based on coefficient of variation.

        Args:
            column_indices (list): Indices of columns to analyze.

        Returns:
            int: Index of the most constant column.

        Raises:
            None
        """
        avg_diffs = {}
        table_transposed = list(zip(*self.table))
        for idx in column_indices:
            if 0 <= idx < len(table_transposed):
                column = list(table_transposed[idx])
                avg_diff = self.calculate_variance(column)
                avg_diffs[idx] = avg_diff
            else:
                print(f"Index {idx} is out of range")
        min_variance_column_idx = min(avg_diffs, key=lambda x: abs(avg_diffs[x]))
        return min_variance_column_idx


def calculate_ln_concentration(concentrations):
    """
    Calculate the natural logarithm of concentrations.

    Args:
        concentrations (list of float): A list containing concentrations of substances.

    Returns:
        list of float: A list containing the natural logarithm of concentrations.
    """
    ln_concentrations = [math.log(concentrations) for concentrations in concentrations] 
    return ln_concentrations

def derivative_ln(concentrations, times):
    """
    Calculate the derivative of the natural logarithm of concentrations with respect to time.

    Args:
        concentrations (list of float): A list containing concentrations of substances.
        times (list of float): A list containing corresponding times.

    Returns:
        list of float: A list containing the derivatives of the natural logarithm of concentrations.
    """
    derivatives_ln = []
    for i in range(len(concentrations) - 1):
        d_concentration = math.log(concentrations[i + 1]) - math.log(concentrations[i])
        dt = times[i + 1] - times[i]
        derivative = d_concentration / dt
        derivatives_ln.append(derivative)
    return derivatives_ln

def calculate_inverse_concentration(concentrations):
    """
    Calculate the inverse of concentrations.

    Args:
        concentrations (list of float): A list containing concentrations of substances.

    Returns:
        list of float: A list containing the inverse of concentrations.
    """
    inverse_concentrations = [1 / concentration for concentration in concentrations]
    return inverse_concentrations

def calculate_derivative_of_inverse_concentration(concentrations, times):
    """
    Calculate the derivative of the inverse of concentrations with respect to time.

    Args:
        concentrations (list of float): A list containing concentrations of substances.
        times (list of float): A list containing corresponding times.

    Returns:
        list of float: A list containing the derivatives of the inverse of concentrations.
    """
    derivatives_inverse = []
    for i in range(len(concentrations) - 1):
        delta_concentration = 1 / concentrations[i + 1] - 1 / concentrations[i]
        dt = times[i + 1] - times[i]
        derivative = delta_concentration / dt
        derivatives_inverse.append(derivative)
    return derivatives_inverse

def main_rate():
    """
    Perform calculations and analysis based on user concentrations and times input.

    This function collects user data, performs calculations, analyzes the data, and provides results
    and visualizations based on the user's choices.

    A table showing the various values (with derivatives) is shown. The order is determined and 
    plotting the concentrations as a function of time is offered.
    """
    times, concentrations = manual_or_read()
    derivatives = [None] + calculate_derivative(times, concentrations) 
    ln_concentrations = calculate_ln_concentration(concentrations)
    derivative_ln2 = [None] + derivative_ln(concentrations, times)
    inverse_concentration = calculate_inverse_concentration(concentrations)
    inverse_derivative = [None] + calculate_derivative_of_inverse_concentration(concentrations, times)
    
    # List of lists to round
    lists_to_round = [times, concentrations, derivatives, ln_concentrations, derivative_ln2, inverse_concentration, inverse_derivative]
    
    # Round each list in the lists_to_round list
    rounded_lists = [list(map(lambda x: round(x, 4) if x is not None else None, lst)) for lst in lists_to_round]

    table = zip(*rounded_lists)
    headers = ["Time", "Concentration", "Derivatives", "ln(Concentrations)", "derivative_ln", "Inverse", "Inverse derivative"]
    print(tabulate(table, headers=headers))

    # Example 
    # Define the indices of the columns you want to consider
    column_indices = [0, 1, 2]

    # Combine the data into a table
    table = zip(derivatives, derivative_ln2, inverse_derivative)
    
    # Create an instance of the TableAnalyzer class
    analyzer = TableAnalyzer(table)

    # Find the index of the column with the lowest average difference
    most_constant_column_idx = analyzer.find_most_constant_column(column_indices)   

    while True:

        if most_constant_column_idx == 0:
           print()
           print("The speed law is zero order.\nThe derivatives column exhibits the least variation (according to the coefficient of variation).")
           spacing()
           break

        elif most_constant_column_idx == 1:
            print()
            print("The speed law is first order.\nThe derivative_ln column exhibits the least variation (according to the coefficient of variation).")
            spacing()
            break

        elif most_constant_column_idx == 2:
            print()
            print("The speed law is second order.\nThe inverse derivative column exhibits the least variation (according to the coefficient of variation).")
            spacing()
            break

        else:
            continue

    while True:
        print("Do you want to plot the graph showing the evolution of the concentration as a function of time?")
        yes_or_no = input("Your response (yes/no): ").lower()
        if yes_or_no == 'yes':
            display_graph(times, concentrations, ylabel ='Concentration [M]', title = 'Evolution of the concentration as a function of time')
            break

        elif yes_or_no == 'no':
            break

        else:
            spacing()
            print("Error. Enter yes or no")
            continue

    spacing()

    while True:
        print("Would you like to get the rate constant?")
        rate_constant = input("Your response (yes/no): ")
        if rate_constant == 'yes':
            print()
            if most_constant_column_idx == 0:
                # Fit a linear function (y = mx + b) to the data
                x, y = np.polyfit(times, concentrations, 1)
                # Generate points for the linear function
                x_fit = np.linspace(min(times), max(times), 100)
                y_fit = x * x_fit + y
                print(f"The rate constant k is {round(-x,3)} M.s\u207B\u00B9")
                exit()

            elif most_constant_column_idx == 1:
                # Fit a function to the data
                x, y = np.polyfit(times, np.log(concentrations), 1)
                x = np.exp(x)
                # Generate points for the linear function
                x_fit = np.linspace(min(times), max(times), 100)
                y_fit = x * np.exp(y * x_fit)
                print(f"The rate constant k is {round(-y,3)} s\u207B\u00B9")
                spacing()
                print("Would you like to have the half reaction time?")    
                while True:
                    half_reaction = input("Your response (yes/no): ").lower()
                    if half_reaction == 'yes':
                        print()
                        print(f"The half reaction time is {round(math.log(2)/abs(x),3)} s.\n")
                        break
                    elif half_reaction == 'no':
                        break
                    else:
                        print("Please enter either yes or no.\n")
                        continue   
                exit()

            elif most_constant_column_idx == 2:
                # Fit a function of the type 1/x(t) = 1/x0 + kt to the data
                x = np.array(times)
                y = np.array(concentrations)
                y0 = y[0]  # Initial value of y
                k, _ = np.polyfit(x, 1/y, 1)

                # Generate points for the fitted curve
                x_fit = np.linspace(min(x), max(x), 100)
                y_fit = 1 / (1/y0 + k * x_fit)
                print(f"The rate constant k is {round(k,3)} M\u207B\u00B9s\u207B\u00B9")
                exit()

        elif rate_constant == 'no':
            exit()
        else:
            spacing()
            print("Please, provide one of the provided answers.")
            continue