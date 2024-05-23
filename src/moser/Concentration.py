from MolarMass import *

compound = str()
def ConcentrationA(n, V):
    '''Evaluates the molar concentration of a solution.

        The concentration calculation is done based on the known volume and known number of moles of solute.
        * Requires: MolarMass

        Args:
            n (float) :  number of moles of solute
            V (float) :  volume of the solution

        Returns:
            C (float) :  solution's molar concentration'''

    C = float(n)/float(V)
    return C

def ConcentrationB(compound, m, V):
    '''Evaluates the molar concentration of a solution.

            The concentration calculation is done based on the known volume and known mass of solute.
            * Requires: MolarMass

            Args:
                compound (str) : chemical formula of the solute
                n (float) :      number of moles of solute
                V (float) :      volume of the solution

            Returns:
                C (float) :  solution's molar concentration'''
    C = float(m)/(MolarMass(compound)*float(V))
    return C

def ConcentrationC(Ci, Vi, Vf):
    '''Evaluates the molar concentration of a solution.

            The concentration calculation is done based on dilution of a solution of known molar concentration.

            Args:
                Ci (float) : initial concentration
                Vi (float) : initial volume
                Vf (float) : final volume

            Returns:
                C (float) :  solution's molar concentration'''
    C = float(Vi)/float(Vf)*float(Ci)
    return C

def ConcentrationUI():
    '''Integrates the three concentration calculation methods in a practical user interface.

            Lets the user choice the method how the molar concentration should be evaluated (moles, mass, dilution)
            and accepts only valid inputs.
            * Requires: ConcentrationA, ConcentrationB, ConcentrationC'''

    compound = input("\033[1m" + "\nWhat compound is the solute?" + "\033[0m \nEnter the chemical formula: " )

    while True:
        mode = input(
            "\033[1m" + "\nFrom which data would you like to evaluate the solution's concentration?" + "\033[0m"
            "\n∘ moles [mol] and volume [L] --- 1"
            "\n∘ mass [g] and volume [L] ------ 2"
            "\n∘ dillution -------------------- 3"
            "\nMake your choice (1/2/3): ")

        try:
            if mode == "1":
                print("\033[1m" + "\nPlease enter your data:" + "\033[0m")
                n = input("∘ n [mol] = ")
                V = input("∘ V [L] = ")

                C = round(ConcentrationA(n, V), 3)

                print(f"\033[1m" + "\nThe concentration of this solution equals" + "\033[0m"
                    f"\n➢ c = {C} molL⁻¹")
                break

            if mode == "2":
                print("\033[1m" + "\nPlease enter your data:" + "\033[0m")
                m = input("∘ m [g] = ")
                V = input("∘ V [L] = ")

                C = round(ConcentrationB(compound, m, V), 3)

                print(f"\033[1m" + "\nThe concentration of this solution equals" + "\033[0m"
                      f"\n➢ c = {C} molL⁻¹")
                break

            if mode == "3":
                print("\033[1m" + "\nPlease enter your data:" + "\033[0m")
                Ci = input("∘ ci [molL⁻¹] = ")
                Vi = input("∘ Vi [L] = ")
                Vf = input("∘ Vf [L] = ")

                C = round(ConcentrationC(Ci, Vi, Vf), 3)

                print(f"\033[1m" + "\nThe concentration of this solution equals" + "\033[0m"
                    f"\n➢ c = {C} molL⁻¹")
                break
        except:
            print("\033[1m" + "Enter the pKa" + "\033[0m")

    return C

