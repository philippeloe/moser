import math
from Concentration import ConcentrationUI
def HConcentration(C, pKa):
    '''Evaluates the concentration of H+ ions in a soltion.

            The H+ concentration is approximated accordingly to each specific case.
            * Requires: Concentration, Concentration.compound, math

            Args:
                C (float) :   concentration of the solute in solution
                pKa (float) : pKa of the solute

            Returns:
                H (float) :  H+ cocentration'''

    Ke = 10**(-14)

    # Acid case
    if pKa < 7:
        Ka = 10**(-pKa)
        Ca = C

        # Strong acid case
        if pKa < -1.74:
            H = 1/2*Ca + math.sqrt(1/4*Ca**2 + Ke)

        # Weak acid case
        else:
            H = -1/2*Ka + math.sqrt(1/4*Ka**2+Ka*Ca)

    # Base case
    if pKa > 7:
        Ka = 10**(-pKa)
        Cb = C

        # Strong base case
        if pKa > 14:
            H = -1/2*Cb + math.sqrt(1/4*Cb**2 + Ke)

        # Weak base case
        else:
            H = 1/2*Ke*1/Cb + math.sqrt(1/4*(Ke*1/Cb)**2 + Ke*Ka*1/Cb)

    return H

def HConcentrationUI():
    '''User interface for the evaluation of the H+ concentration and pH assessment.

            Composes the HConcetration and ConcetrationUI functions to facilitate the input
            and only accepts valid inpute. Prints the H+ concentration as well as the
            pH = -log10([H+]).
            * Requires: ConcentrationUI'''
    C = ConcentrationUI()
    while True:
        try:
            pKa = float(input(f"\033[1m" + "\nEnter the first pKa [-] of the solute: " + "\033[0m"))
            break
        except:
            print(f"\033[1m" + "\nEnter the a valid pKa [-]! " + "\033[0m")
    H = HConcentration(C, pKa)
    pH = -math.log10(H)
    print(f"\033[1m" + "\nThe given solution has the following properties " + "\033[0m"
          f"\n➢ [H+] = {round(H, 3)} molL⁻¹"
          f"\n➢ pH = {round(pH,2 )}")

#print(f"\033[1m" + "\nThe pH of this solution equals" + "\033[0m"
      #f"\n➢ pH = {round(-1*math.log10(HConcentration(Concentration()[0], -6)), 2)}", "Compound =", compound)

