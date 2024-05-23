from Reaction_constant_activity import quotient_reaction
from Reaction_constant_activity import reactants_products
from Reaction_constant_activity import get_valid_number
from Reaction_constant_activity import stochio2
from Reaction_constant_activity import lign

def activities_concentration(num, activities, x):
    """
    Collects activity data for reactants or products based on user input.

    This function prompts the user to enter the type and relevant data for each reactant
    or product (depending on the value of `x`). It calculates the activity based on the type:
    - Solids, liquids, and solvents have an activity of 1.
    - Solutes' activity is based on their concentration.
    - Gases' activity is based on their pressure.

    Args:
        num (int): Number of reactants or products.
        activities (list): List to store the calculated activities.
        x (int): Indicator if the function is processing reactants (0) or products (1).

    Returns:
        list: Updated list of activities.
    """
    if x == 0:
        x = "reagent"
    elif x == 1:
        x = "product"

    for i in range(num):
        while True:
            type = input(f"Enter the type of {x} {i+1} (solid/liquid/solvent/solute/gas): ").lower()
            if type in ['solid', 'liquid', 'solvent']:
                activity = 1
                lign()
                break
            elif type == 'solute':
                stochio = stochio2()
                concentration = get_valid_number("Enter its concentration (in mol/L): ")
                activity = concentration ** stochio
                lign()
                break

            elif type == 'gas':
                stochio = stochio2()
                pressure = get_valid_number("Enter its pressure (in bar): ")
                activity = pressure ** stochio
                lign()
                break

            else:
                lign()
                print("Invalid reactant type. Please enter 'solid', 'liquid', 'solvent', 'solute', or 'gas'.")

        activities.append(activity)

    return activities

def calculate_concentration_constant():
    """
    Calculate the reaction quotient using the concentration and pressure of each compound.

    This function:
    1. Fetches the number of reactants and products.
    2. Collects activities for each reactant and product based on user input.
    3. Calculates the reaction quotient using the collected activities.

    No parameters or return values.
    """
    num_reactants, num_products = reactants_products()

    reactant_activities = []
    product_activities = []

    # Calculate activities for reactants
    reactant_activities = activities_concentration(num_reactants, reactant_activities, 0)

    # Calculate activities for products
    product_activities = activities_concentration(num_products, product_activities, 1)

    quotient_reaction(reactant_activities, product_activities)