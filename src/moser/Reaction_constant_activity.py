def lign():
    """
    Print a separating line for better readability in the console output.

    This function outputs a line of dashes to the console to separate different sections
    of the output for better readability.

    No parameters or return values.
    """
    print()
    print("--------")
    print()

def get_valid_integer(prompt):
    """
    Prompt the user to enter an integer and validate the input.

    This function repeatedly prompts the user to enter an integer until a valid
    integer is provided.

    Args:
        prompt (str): The input prompt message to display to the user.

    Returns:
        int: The validated integer entered by the user.
    """
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            lign()
            print("Invalid input. Please enter an integer.")

def get_valid_number(prompt):
    """
    Prompt the user to enter a number (float) and validate the input.

    This function repeatedly prompts the user to enter a number until a valid
    number is provided.

    Args:
        prompt (str): The input prompt message to display to the user.

    Returns:
        float: The validated number entered by the user.
    """
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            lign()
            print("Invalid input. Please enter a number.")

def get_reactants_or_products_info(num, type_):
    """
    Collect activities and stoichiometric coefficients for reactants or products.

    This function prompts the user to enter the activity and stoichiometric
    coefficient for each reactant or product.

    Args:
        num (int): Number of reactants or products.
        type_ (str): Type of chemical species ('reactant' or 'product').

    Returns:
        tuple: Two lists, one containing the activities and the other containing
               the stoichiometric coefficients.
    """
    activities = []
    coefficients = []
    for i in range(num):
        activity = get_valid_number(f"Enter the activity of {type_} {i+1}: ")
        coefficient = get_valid_number(f"Enter the stoichiometric coefficient of {type_} {i+1}: ")
        activities.append(activity)
        coefficients.append(coefficient)
        lign()
    return activities, coefficients

def calculate_reaction_quotient(reactant_activities, reactant_coefficients, product_activities, product_coefficients):
    """
    Calculate the reaction quotient from the activities and stoichiometric coefficients.

    This function calculates the reaction quotient using the provided activities
    and stoichiometric coefficients for reactants and products.

    Args:
        reactant_activities (list): List of activities for reactants.
        reactant_coefficients (list): List of stoichiometric coefficients for reactants.
        product_activities (list): List of activities for products.
        product_coefficients (list): List of stoichiometric coefficients for products.

    Returns:
        float: The calculated reaction quotient.
    """
    reactant_term = 1
    for activity, coeff in zip(reactant_activities, reactant_coefficients):
        reactant_term *= activity ** coeff

    product_term = 1
    for activity, coeff in zip(product_activities, product_coefficients):
        product_term *= activity ** coeff

    quotient = product_term / reactant_term
    return quotient

def main_activity():
    """
    Main function to interact with the user for calculating the reaction quotient using activities.

    This function prompts the user to enter the number of reactants and products,
    collects the activities and stoichiometric coefficients, and calculates the
    reaction quotient.

    No parameters or return values.
    """
    num_reactants = get_valid_integer("Enter the amount of reactants: ")
    lign()
    reactant_activities, reactant_coefficients = get_reactants_or_products_info(num_reactants, "reactant")

    num_products = get_valid_integer("Enter the number of products: ")
    product_activities, product_coefficients = get_reactants_or_products_info(num_products, "product")
    
    quotient = calculate_reaction_quotient(reactant_activities, reactant_coefficients, product_activities, product_coefficients)
    
    print(f"The reaction quotient is equal to: {quotient}")
    exit()

def stochio2():
    """
    Prompt the user to enter the stoichiometric coefficient and validate the input.

    This function repeatedly prompts the user to enter a stoichiometric coefficient
    until a valid number is provided.

    Returns:
        float: The validated stoichiometric coefficient entered by the user.
    """
    while True:
        try:
            stochio = float(input("Enter its stoichiometric number: "))
            break  # Exit the loop if input is successfully converted to a float
        except ValueError:
            lign()
            print("Invalid input. Please enter a valid number.")

    return stochio

def reactants_products():
    """
    Prompt the user to enter the number of reactants and products and validate the input.

    This function repeatedly prompts the user to enter the number of reactants and
    products until valid positive integers are provided.

    Returns:
        tuple: A tuple containing the number of reactants (int) and the number of products (int).
    """
    while True:
        try:
            num_reactants = int(input("Enter the number of reactants: "))
            num_products = int(input("Enter the number of products: "))
            
            # Check if both numbers are positive
            if num_reactants > 0 and num_products > 0:
                lign()
                break
            else:
                lign()
                print("Please enter positive integers for the number of reactants and products.")
        except ValueError:
            lign()
            print("Please enter valid integers for the number of reactants and products.\n")

    return num_reactants, num_products

def type(number, R_or_P, x):
    """
    Collect information about the type and relevant properties of reactants or products.

    This function prompts the user to enter the type and relevant properties for each
    reactant or product. It calculates and returns the product of the properties based
    on the type.

    Args:
        number (int): Number of reactants or products.
        R_or_P (list): List to store the information about each reactant or product.
        x (int): Indicator if the function is processing reactants (1) or products (0).

    Returns:
        float: The calculated product of properties for the reactants or products.
    """
    nb = x

    if nb == 0:
        nb = "product"

    elif nb == 1:
        nb = "reactant"

    for i in range(number):
        while True:  # Loop until a valid input is provided
            compound_type = input(f"Enter the type of {nb} {i+1} (gas/solute/solid/liquid/other): ").lower()
            
            if compound_type == 'gas':
                while True:
                    try:
                        pressure = float(input("Enter its pressure in bar: "))
                        break  # Exit the loop if input is successfully converted to a float
                    except ValueError:
                        lign()
                        print("Invalid input. Please enter a valid number.")
            
                stochio = stochio2()
                R_or_P.append({'type': 'gas', 'pressure': pressure**stochio})
                lign()
                break  # Break out of the loop after valid input
            
            elif compound_type == 'solute':
                while True:
                    try:
                        concentration = float(input("Enter the concentration of the solute (in mol/L): "))
                        break  # Exit the loop if input is successfully converted to a float
                    except ValueError:
                        lign()
                        print("Invalid input. Please enter a valid number.")

                stochio = stochio2()
                R_or_P.append({'type': 'solute', 'concentration': concentration**stochio})
                lign()
                break  # Break out of the loop after valid input
            
            elif compound_type == 'other':
                while True:
                    try:
                        concentration = float(input("Enter the concentration of the compound (in mol/L): "))
                        break  # Exit the loop if input is successfully converted to a float
                    except ValueError:
                        lign()
                        print("Invalid input. Please enter a valid number.")

                while True:
                    try:
                        activity_coefficient = float(input("Enter the activity coefficient (γ): "))
                        break  # Exit the loop if input is successfully converted to a float
                    except ValueError:
                        lign()
                        print("Invalid input. Please enter a valid number.")

                stochio = stochio2()
                R_or_P.append({'type': 'other', 'concentration': concentration, 'activity_coefficient': activity_coefficient, 'stochio': stochio})
                lign()
                break  # Break out of the loop after valid input
            
            elif compound_type == 'solid' or compound_type == 'liquid':
                R_or_P.append({'type': 'solid/liquid', 'activity': 1})
                lign()
                break  # Break out of the loop after valid input
            
            else:
                lign()
                print("Please, choose between the offered nature")
            
    N_or_D = 1
    for reactant in R_or_P:
        if reactant['type'] == 'gas':
            N_or_D *= reactant['pressure']
        elif reactant['type'] == 'solute':
            N_or_D *= reactant['concentration']
        elif reactant['type'] == 'other':
            N_or_D *= (reactant['concentration'] * reactant['activity_coefficient'])**reactant['stochio']

    return N_or_D

def quotient_reaction(reagents, products):
    """
    Calculate and print the equilibrium constant for a reaction.

    This function calculates the equilibrium constant using the provided activities
    of reactants and products and prints the result.

    Args:
        reagents (list): List of activities for reactants.
        products (list): List of activities for products.

    No return values.
    """
    denominator = 1
    for activity in reagents:
        denominator *= activity

    numerator = 1
    for activity in products:
        numerator *= activity
    
    equilibrium_constant = numerator / denominator
    print(f"The equilibrium constant for the reaction is: {round(equilibrium_constant, 3)}")
   
    exit()

def calculate_activity_constant():
    """
    Calculate the equilibrium constant using the activities of reactants and products.

    This function prompts the user to enter whether they know the activities of reactants
    and products. If yes, it uses the activities directly. If no, it collects the required
    data to calculate the equilibrium constant.

    No parameters or return values.
    """
    num_reactants = 0
    num_products = 0

    while True:
        print("Do you know the activities of the reactants and products?\n")

        know_activities = input("Your response (yes/no): ").lower()

        if know_activities == 'yes':
            main_activity()
        elif know_activities == 'no':
            num_reactants, num_products = reactants_products()
                
            reactants = []
            products = []
            
            equilibrium_constant = type(num_products, products, 0) / type(num_reactants, reactants, 1)
            print(f"The equilibrium constant for the reaction is: {equilibrium_constant}")
            break
        else:
            lign()
            print("Invalid input. Please enter 'yes' or 'no'.")
            continue