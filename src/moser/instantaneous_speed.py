import matplotlib.pyplot as plt
import numpy as np

from read_file_and_enter_data import manual_or_read
from read_file_and_enter_data import spacing

def instantaneous_main():
    """
    Calculate the instantaneous speed at a specific time based on concentration-time data.

    This function prompts the user to input a time value 't' and calculates the instantaneous speed 
    of the reaction at that time using concentration-time data provided by the user. It then plots
    the curve passing through the two nearest points around time 't' and displays the equation of 
    the line representing the derivative of the curve at time 't'.

    Returns:
        None
    """
    times, concentrations = manual_or_read()
    while True:
        try:
            t = int(input("Give the value at time t in which you want the instantaneous speed (in seconds): "))
            if t < 0:
                spacing()
                print("Please enter a positive time t.\n")
                continue

            if t > times[-1]:
                spacing()
                print("Time t out of range. Please enter a valid time.\n")
                continue
        
            elif t < 0:
                spacing()
                print("Time t out of range please enter a valid time. Please enter a valid time.")
                spacing()
                continue

            elif t == 0:
                spacing()
                slope = (concentrations[1] - concentrations[0]) / (times[1]-times[0])
                break
            
            elif t == times[-1]:
                spacing()
                slope = (concentrations[-1] - concentrations[-2]) / (times[-1]) - (times[-2])
                break

            elif (concentrations[t] > concentrations[t - 1] and concentrations[t] > concentrations[t + 1]) or (concentrations[t] < concentrations[t - 1] and concentrations[t] < concentrations[t + 1]):
                spacing()
                slope = 0
                break

            else:
                # Extract the x and y values for the two points
                x_points = [times[t + 1], times[t - 1]]
                y_points = [concentrations[t + 1], concentrations[t - 1]]
                # Compute the slope between the two points
                slope = (y_points[1] - y_points[0]) / (x_points[1] - x_points[0])
                spacing()
                break

        except ValueError:
            spacing()
            print("Error: please enter a valid number.\n")

    # Compute the y-intercept for the line passing through concentrations[t]
    intercept = concentrations[t] - slope * times[t]

    # Round coefficients to four decimals
    rounded_slope = f"{slope:.3f}"
    rounded_intercept = f"{intercept:.3f}"

    # Generate the polynomial function using the slope and y-intercept
    poly_function = np.poly1d([slope, intercept])

    # Create equation string
    equation = f'y = {rounded_slope}x + {rounded_intercept}'    

    # Generate x values for plotting the curve
    x_values = np.linspace(min(times), max(times), 100)

    # Compute corresponding y values using the polynomial function
    y_values = poly_function(x_values)

    # Plot the original data
    plt.plot(times, concentrations, color='red', label='Concentration as a function of time')

    # Plot the curve passing through the two points
    plt.plot(x_values, y_values, color='blue', label=f'Derivative of the curve at t={t}')
    plt.text(0.5, 0.5, equation, fontsize=12, transform=plt.gca().transAxes, bbox=dict(facecolor='white', alpha=0.5))

    # Add labels and legend
    plt.xlabel('Time (s)')
    plt.ylabel('Concentration (mol.L-1)')   
    plt.title('Instantaneous speed')
    plt.legend()
    plt.show()
    print()
    print(f"The instantaneous speed at t = {t} s is equal to {round(slope, 3)} M.s\u207B\u00B9\n")