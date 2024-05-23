from instantaneous_speed import instantaneous_main
from read_file_and_enter_data import spacing
from calculate_speed import speed_main 
from reaction_order import main_rate

from Reaction_constant_concentration import calculate_concentration_constant
from Reaction_constant_activity import calculate_activity_constant

from BalanceEq import *
from Concentration import *
from Decompose import *
from HConcentration import *
from MolarMass import *
from Titration import *

def print_menu():
    """
    Print the menu options for the user.
    """
    print("\033[1m" + "\nWhat would you like to calculate ?\n")

    print(f"\033[1mKinetics\033[0m")
    print("∘The instantaneous velocity at a certain time t ------ A")
    print("∘To determine the reaction order (0,1 or 2) ---------- B")
    print("∘The velocity as a function of time ------------------ C\n")

    print("\033[1m" + "Calculating the reaction quotient" + "\033[0m")
    print("By using the concentration and pressure -------------- D")
    print("By using the activity -------------------------------- E\n")

    print("\033[1m" + "Chemical equations" + "\033[0m")
    print("∘Balance a chemical equation ------------------------- F\n")

    print("\033[1m" + "Molar mass" + "\033[0m")
    print("∘Calculate a compound's molar mass ------------------- G\n")

    print("\033[1m" + "Concentration & pH" + "\033[0m")
    print("∘Evaluate the concentration of solute ---------------- H")
    print("∘Evaluate the pH of a solution ----------------------- I\n")

    print("\033[1m" + "Titrations" + "\033[0m")
    print("∘Trace specific titration curves --------------------- J\n")


def main():
    """
    Presents a menu for the user to choose between three options.

    This function repeatedly displays a menu of options to the user and prompts for their choice.
    The available options are:
    - A: Calculate the velocity as a function of the time.
    - B: Determine the instantaneous velocity at a specific time.
    - C: Determine the reaction order (0, 1, or 2).
    - 'exit': Quit the program.

    Args:
        None

    Returns:
        None

    User's Choice (str): The user's input representing their choice of action, which can be 'A', 'B', 'C', or 'exit'.
    """
    while True:
        print_menu()
        choice = input("Enter your choice: ").lower()
        spacing()

        if choice == "a":
            instantaneous_main()
            break

        elif choice == "b":
            main_rate()
            break
    
        elif choice == "c":
            speed_main()
            break

        elif choice == 'd':
            calculate_concentration_constant()
            break

        elif choice == 'e':
            calculate_activity_constant()
            break

        elif choice == "f":
            BalanceEqUI()
            break

        elif choice == "g":
            MolarMassUI()
            break

        elif choice == "h":
            ConcentrationUI()
            break

        elif choice == "i":
            HConcentrationUI()
            break

        elif choice == "j":
            Titration()
            break

        elif choice == 'exit':
            exit()

        else:
            print("Invalid choice. Please enter a given letter or 'exit' to quit the program.\n")
            continue

if __name__ == "__main__":
    """
    This block of code is executed when the script is run directly by the Python interpreter,
    rather than being imported as a module into another script. It ensures that the `main()` function
    is called to start the program's execution.
    """
    main()