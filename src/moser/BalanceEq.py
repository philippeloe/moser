from Decompose import *
from sympy import *

def BalanceEq(l_reactants, l_products):
    '''Calculates the stoichiometric coefficients to balance the chemical reaction.

        Sorts the reactants and products alphabetically and solves the linear system to find the
        minimal stoichiometric coefficients. The output lists respect the alphabetical order.
        * Requires: Decompose, sympy

        Args:
            l_reactants (list) :    contains the reactants
            l_products (list) :  contains the products

        Returns:
            l_coefs_reactants (list) :  contains the stoichiometric coefficients for the reactants only
            l_coefs_products (list) :   contains the stoichiometric coefficients for the products only
            l_coefs (list) :    contains all the stoichiometric coefficients in the correct order'''

    l_dics_elements_reactants = Decompose(sorted(l_reactants))
    l_dics_elements_products = Decompose(sorted(l_products))

    '''Creates list of elements contained in the reactants'''
    l_elements_reactants = []
    for i in range(len(l_dics_elements_reactants)):
        l_keys = list(l_dics_elements_reactants[i].keys())
        for j in range(len(l_keys)):
            l_elements_reactants.append(l_keys[j])
    l_elements_reactants = list(set(l_elements_reactants))

    '''Creates list of elements contained in the products'''
    l_elements_products = []
    for i in range(len(l_dics_elements_products)):
        l_keys = list(l_dics_elements_products[i].keys())
        for j in range(len(l_keys)):
            l_elements_products.append(l_keys[j])
    l_elements_products = list(set(l_elements_products))

    '''Checks if the given reaction is valid (same elements show up in reactants and products)'''
    if l_elements_reactants != l_elements_products:
        return False
    else:
        l_elements = sorted(l_elements_reactants)

        '''Creates reactant coefficient matrix R'''
        RT = []
        for i in range(len(l_dics_elements_reactants)):
            for j in range(len(l_elements)):
                if l_elements[j] not in l_dics_elements_reactants[i].keys():
                    l_dics_elements_reactants[i][l_elements[j]] = 0
            l_dics_elements_reactants[i] = dict(sorted(l_dics_elements_reactants[i].items()))
            RT.append(list(l_dics_elements_reactants[i].values()))
        R = Matrix(RT).T

        '''Creates product coefficient matrix P'''
        PT = []
        for i in range(len(l_dics_elements_products)):
            for j in range(len(l_elements)):
                if l_elements[j] not in l_dics_elements_products[i].keys():
                    l_dics_elements_products[i][l_elements[j]] = 0
            l_dics_elements_products[i] = dict(sorted(l_dics_elements_products[i].items()))
            PT.append(list(l_dics_elements_products[i].values()))
        P = -1*Matrix(PT).T

        '''Creates total coefficient matrix A'''
        A = R.row_join(P)
        A = A.rref()[0]
        AT = A.T
        l_AT = AT.tolist()

        '''Deletes the unit vectors in the matrix'''
        l_unit_vecs = []
        for vec in l_AT:
            if vec.count(1) == 1 and vec.count(0) == len(vec)-1:
                l_unit_vecs.append(vec)

        for unit_vec in l_unit_vecs:
            if unit_vec in l_AT:
                l_AT.remove(unit_vec)
        l_raw_vecs = l_AT

        '''Determines the scalar giving the smallest integer solution'''
        l_scalars = []
        for vec in l_raw_vecs:
            l_temp = []
            for coef in vec:
                if "/" in str(coef):
                    numerator, denominator = str(coef).split('/')
                    l_temp.append(int(denominator))
                else:
                    l_temp.append(1)
            l_scalars.append(int(max(l_temp)))

        '''Extracts the coefficional vectors from the matrix'''
        l_vecs = []
        for i in range(len(l_raw_vecs)):
            for j in range(len(l_dics_elements_reactants)+len(l_dics_elements_products)-len(vec)-1):
                vec.append(0)
            for j in range(len(l_dics_elements_reactants)+len(l_dics_elements_products)-len(vec)):
                vec.append(1)
            l_vecs.append(vec)

        '''Evaluates the stoichiometric coefficients'''
        for i in range(len(l_raw_vecs)):
            scalar = l_scalars[i]
            for j in range(len(l_raw_vecs[i])):
                l_raw_vecs[i][j] = abs(int(l_raw_vecs[i][j]*scalar))
        l_vecs = l_raw_vecs

        '''Creates corresponding lists'''
        l_coefs = [sum(coef) for coef in zip(*l_vecs)]
        l_coefs_reactants = l_coefs[:len(l_dics_elements_reactants)]
        l_coefs_products = l_coefs[-len(l_dics_elements_products):]

    return sorted(l_reactants) , sorted(l_products), l_coefs_reactants, l_coefs_products, l_coefs,

def BalanceEqUI():
    '''User interface to facilitate the usage of the BalanceEq function.

        Calls the functions BalanceEq, rejects invalid parameters and prints the final chemical equation.
        * Requires: BalanceEq'''
    while True:
        print("\033[1m" + "\nPlease enter your chemical reaction." + "\033[0m")
        l_reactants = []
        while True:
            reactant = input("Enter a reactant (type '*' when finished): ")
            if reactant == '*':
                break
            l_reactants.append(reactant)

        l_products = []
        while True:
            product = input("Enter a product (type '*' when finished): ")
            if product == '*':
                break
            l_products.append(product)

        try:
            l_reactants, l_products, l_coefs_reactants, l_coefs_products, l_coefs = BalanceEq(l_reactants, l_products)
            l_reaction1 = [reactant for coef in zip(l_coefs_reactants, l_reactants) for reactant in coef]
            l_reaction2 = [product for coef in zip(l_coefs_products, l_products) for product in coef]

            print("\033[1m" + "\nFind hereafter the balanced chemical equation:" + "\033[0m")

            def format(list):
                formatted_list = []
                for i in range(0, len(list), 2):
                    coef = list[i]
                    molecule = list[i + 1]
                    if coef == 1:
                        formatted_item = molecule
                    else:
                        formatted_item = f"{coef} {molecule}"
                    formatted_list.append(formatted_item)
                return " + ".join(formatted_list)

            coefs_reactants = format(l_reaction1)
            coefs_products = format(l_reaction2)
            chemical_equation = f"{coefs_reactants} → {coefs_products}"
            print(chemical_equation)
            break
        except:
            print(f"\033[1m" + "Invalid chemical reaction!" + "\033[0m")

#print(BalanceEq(["H2", "O2"], ["H2O"]))
#print(BalanceEq(["C2H4", "O2"], ["H2O", "CO2"]))

