from read_file_and_enter_data import manual_or_read
from read_file_and_enter_data import spacing
import matplotlib.pyplot as plt
import numpy as np

def display_graph(times, velocity, ylabel = None, title = None, color = None, label = None):
    """
    Display a graph of velocity versus time.

    Args:
        times (list of float): A list of time values.
        velocity (list of float): A list of corresponding velocity values.
        ylabel (str, optional): Label for the y-axis. If None, default label is 'Velocity (M.s⁻¹)'.
        title (str, optional): Title for the plot. If None, default title is 'Evolution of the velocity of the reaction'.
        color (str, optional): Color of the plot line.
        label (str, optional): Label for the plot legend.

    Returns:
        None
    """
    times_interp = np.linspace(times[0], times[-1], len(velocity))
    plt.plot(times_interp, velocity)
    plt.xlabel('Time (s)')

    if ylabel:
        plt.ylabel(ylabel)
    else:
        plt.ylabel('Velocity (M.s\u207B\u00B9)')

    if title:
        plt.title(title)
    else:
        plt.title('Evolution of the velocity of the reaction')
    plt.show()

def velocity_first(times, concentrations):
    """
    Calculate and display velocity using the first method.

    Args:
        times (list of float): A list of time values.
        concentrations (list of float): A list of corresponding concentration values.

    Returns:
        list of float: A list of calculated velocities.
    """
    velocities = []
    velocities.append(abs((concentrations[1]-concentrations[0]))/times[1])
    for i in range(1, len(concentrations)-1):
        dt = times[i+1] - times[i-1]
        dc = concentrations[i+1] - concentrations[i-1]
        velocity = abs(dc / dt)
        velocities.append(velocity)
    display_graph(times, velocities)
    return velocities

def velocity_second(concentrations, times):
    """
    Calculate and display velocity using the second method.

    Args:
        concentrations (list of float): A list of concentration values.
        times (list of float): A list of corresponding time values.

    Returns:
        None
    """
    # Compute the derivative of the function using the gradient method
    dy_dx = np.gradient(concentrations, times)
    dy_dx = np.abs(dy_dx)
    display_graph(times, dy_dx)

def speed_main():
    """
    Main function to calculate and display reaction speed.

    Prompts the user to choose between two methods to calculate reaction speed:
    1. Using a formula.
    2. Using the Python gradient method.

    Args:
        None

    Returns:
        None
    """
    times, concentrations = manual_or_read()

    print("2 methods are being offered, pick one:\n")
    print("∘Calculation of the speed using the formula v = ([C]1-[C]2)/(t[1]-t[2]) --- 1")
    print("∘Calculation of the speed using the Python gradient method -----------------2\n")

    while True:
        method = input("Enter your choice: (1 ou 2) ")
        spacing()
        if method == '1':
            velocity_first(times, concentrations)
            break
        elif method == '2':
            velocity_second(concentrations, times)
            break
        else:
            print("Error. Choose between 1 and 2.")
            continue