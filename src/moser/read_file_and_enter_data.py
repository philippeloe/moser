def spacing():
    """
    Print a visual spacing separator.

    This function prints a visual separator to create a clear visual distinction in the output.

    Args:
        None

    Returns:
        None
    """
    print()
    print("------------------------")
    print()

def read_file_concentration(name_file):
    """
    Read concentration-time data from a file.

    This function reads concentration-time data from a file with the specified name. The file should 
    have the following format:
    Time (Unit) Concentration (Unit')

    Args:
        name_file (str): The name of the file containing concentration-time data.

    Returns:
        tuple: A tuple containing two lists - one for time values and one for concentration values.
    """
    
    spacing()
    times = []
    concentrations = []

    while True:
        try:
            with open(name_file, 'r') as f:
                # Ignore the first line containing headers
                next(f)
                for line in f:
                    t, c = map(float, line.split())
                    times.append(t)
                    concentrations.append(c)
            break
        except FileNotFoundError:
            print("File not found. Please enter a valid name file (make sure to have it in the same folder as the Python code).")
            name_file = input("Enter the file name again: ")
            spacing()
        
    print("Are your time unit in second?")
    
    while True:
        seconde = input("My units are in second (yes/no): ").lower()
        if seconde == 'yes':
            spacing()
            break

        elif seconde == 'no':
            print()
            while True:
                print("What are your unit? (min/h/days)")
                units = input("Units = ").lower()
                if units == 'min':
                    times = [t * 60 for t in times]
                    spacing()
                    break
                elif units == 'h':
                    times = [t * 3600 for t in times]
                    spacing()
                    break
                elif units == 'days':
                    [t * 86400 for t in times]
                    spacing()
                    break
                else:
                    spacing()
                    print("Error. Pick a given unit (min/h/days).")
                    continue
            break
        else:
            spacing()
            print("Error. Please enter either yes or no.")
            continue
    return times, concentrations

def manually_enter_concentration():
    """
    Manually enter concentration-time data.

    This function prompts the user to manually enter concentration-time data. The user inputs time and
    concentration values until they choose to end the input.

    Returns:
        tuple: A tuple containing two lists - one for time values and one for concentration values.
    """
    times = []
    concentrations = []
    print("Enter the concentrations [M] as a function of time [s]. Enter 'end' to finish.")
    while True:
        entree = input("time [s], Concentration [M]: ").lower()
        if entree == 'end':
            spacing()
            break
        try:
            t, c = map(float, entree.split(','))
            times.append(t)
            concentrations.append(c)
        except ValueError:
            print()
            print("Error: please enter a valid time and conentration.")
    return times, concentrations

def manual_or_read():
    """
    Prompt the user to choose between manual input or reading from a file.

    This function prompts the user to choose between manually entering concentration-time data or 
    reading from a file. It then calls the corresponding function based on the user's choice.

    Returns:
        tuple: A tuple containing two lists - one for time values and one for concentration values.
    """
    print("Do you want to load a file for the concentration values or you'll enter them?\n")
    print("∘Manually enter the values --- A")
    print("∘Open a file ----------------- B\n")
    min_variance_column_idx = 0
    x_fit = 0 
    y_fit = 0
    while True:
            print("Enter your choice (A or B)")
            file_main = input("My choice: ").lower()
            spacing()
            if file_main == "b":
                print("What is the name of the file?")
                name_file = input("The name of the file is: ")
                times, concentrations = read_file_concentration(name_file)
                break
            elif file_main == 'a':
                times, concentrations = manually_enter_concentration()
                pass
                break
            else:
                print("Wrong value. Please choose between A and B.")
                print()
                continue
    return times, concentrations