import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from scipy.optimize import curve_fit
import warnings

def pH_log_interpolation1(data_points):
    '''Interpolation of the titration curve for a diprotic acid for ξ ∈ [0, 0.5].
    
    Evaluates the optimal parameters to trace a sigmoid curve of the type ƒ(ξ) = a + b⋅log10(ξ)
    passing through fixed starting and endpoints, by solving a system of equations. Evaluates
    the values of ƒ(ξ) for ξ ∈ [0, 0.5].
    * Requires: numpy
    
    Args:
        data_points (list) : interpolation starting and endpoints
        
    Returns:
        x (array) : contains 10000 points for ξ ∈ [0, 0.5]
        y (array) : contains the corresponding values of ƒ(ξ)'''

    def f(a,b, x):
        return a + b * np.log10(x)

    (x1, y1), (x2, y2) = data_points
    log_x1 = np.log10(x1)
    log_x2 = np.log10(x2)

    A = np.array([[1, log_x1], [1, log_x2]])
    B = np.array([y1, y2])
    a, b = np.linalg.solve(A, B)

    x = np.linspace(min(x1, x2), max(x1, x2), 1000)
    y = f(a, b, x)

    return x, y

def pH_log_interpolation2(data_points):
    '''Interpolation of the titration curve for a diprotic acid for ξ ∈ [0.5, 1].

    Evaluates the optimal parameters to trace a sigmoid curve of the type ƒ(ξ) = a + b⋅log10(1/(0.5 - ξ))
    by fitting ƒ through fixed starting and endpoints. Evaluates the values of ƒ(ξ) for ξ ∈ [0, 0.5].
    * Requires: numpy, scipy

    Args:
        data_points (list) : interpolation starting and endpoints

    Returns:
        x (array) : contains 10000 points for ξ ∈ [0.5, 1]
        y (array) : contains the corresponding values of ƒ(ξ)'''

    warnings.filterwarnings('ignore') # Turns of warning related to covariance

    x_data = np.array([data_points[0][0], data_points[1][0]])
    y_data = np.array([data_points[0][1], data_points[1][1]])

    def f(x, a, b):
        return a + b * np.log10(1 / (0.5 - x))

    params, covariance = curve_fit(f, x_data, y_data)
    a, b = params


    x = np.linspace(min(x_data), max(x_data), 1000)
    y = f(x, a, b)

    return x, y

def pH1(Va, Ctit, Veq, x):
    '''Evaluates the positive log10 contribution for the pH of a strong acid in aqueous solution.

        The positive log10 contribution equals log10(Ca⋅(1-ξ)⋅Da) and can be composed with some
        constants to facilitate the pH calculations.

        Args:
            Va (float):     initial volume of the titrated solution
            Ctit (float) :  concentration of the titrant solution
            Veq (float) :   volume of titrant solution added at equivalence point
            x (float) :     degree of advancement of titration ('variable' to trace the curve)

        Returns:
            np.log10(Ca * (1 - x) * Da) (float) : positive log10 contribution'''

    Ca = (Ctit * Veq) / Va
    Vtit = x * Veq
    Da = Va / (Va + Vtit)

    return np.log10(Ca * (1 - x) * Da)

def pH2(Va, Ctit, Veq, x):
    '''Evaluates the positive log contribution for the pH of a strong base in aqueous solution.

        The positive log10 contribution equals log10(Ctit⋅Dtit) and can be composed with some
        constants to facilitate the pH calculations.

        Args:
            Va (float):     initial volume of the titrated solution
            Ctit (float) :  concentration of the titrant solution
            Veq (float) :   volume of titrant solution added at equivalence point
            x (float) :     degree of advancement of titration ('variable' to trace the curve)

        Returns:
            np.log10(Ca * (1 - x) * Da) (float) : positive log10 contribution'''
    Vtit = x * Veq
    Dtit = (Vtit - Veq) / (Va + Vtit)

    return np.log10(Ctit * Dtit)

def pH3(x):
    '''Evaluates the positive log contribution pH of a buffer solution.

        The positive log10 contribution equals log10(ξ / (1 - ξ))) and can be composed with some
        constants to facilitate the pH calculations.

        Args:
            x (float) :     degree of advancement of titration ('variable' to trace the curve)

        Returns:
            np.log10(x / (1-x)) (float) : positive log10 contribution'''

    return np.log10(x / (1-x))

def pH4(Va, Ctit, Veq, x):
    '''Evaluates the positive log contribution for to pH of a solution of a weak base.

        The positive log10 contribution equals 0.5⋅log10(Ca⋅Da) and can be composed with some
        constants to facilitate the pH calculations.

        Args:
            Va (float):     initial volume of the titrated solution
            Ctit (float) :  concentration of the titrant solution
            Veq (float) :   volume of titrant solution added at equivalence point
            x (float) :     degree of advancement of titration ('variable' to trace the curve)

        Returns:
            1/2 * np.log10(Ca * Da) (float) : positive log10 contribution'''
    Ca = (Ctit * Veq) / Va
    Vtit = x * Veq
    Da = Va / (Va + Vtit)

    return 1/2 * np.log10(Ca * Da)

def Titration_sAsB(acid, Va, base, Ctit, Veq):
    '''Traces the curve corresponding to a titration of a strong acid by a strong base.

        Calls the functions pH1 and pH2, composes them with the right constants to evaluate
        the pH as a function of the titration's degree of advancement to finally trace and
        show the titration curve.
        * Requires: pH1, pH2, numpy, matplotlib

        Args:
            acid (str) :    formula / name ot the titrated acid
            Va (float) :    initial volume of titrated acid
            base (str) :    formula / name ot the titrant base
            Veq (float) :   volume of titrant base added at equivalence point'''

    StrongAcidRed = (211/255, 4/255, 4/255)
    StrongBaseBlue = (4/255, 68/255, 140/255)
    Invisible = (0,0,0,0)

    '''Initialises important parameters'''
    Ctit = round(Ctit, 3)
    Ca = round((Ctit * Veq) / Va, 3)
    pH_eq = 7 #pH at equivalence point

    '''Tracing the graph'''
    x1 = np.linspace(0, 0.9999, 10000)
    x2 = np.linspace(1.0001, 1.9999, 10000)

    y1 = -1 * pH1(Va, Ctit, Veq, x1)
    y2 = 14 + pH2(Va, Ctit, Veq, x2)

    '''Formating the graph'''
    plt.figure(figsize=(8, 6))
    curve1, = plt.plot(x1, y1, color=StrongAcidRed, label="pH of strong acid")
    curve2, = plt.plot(x2, y2, color=StrongBaseBlue, label="pH of strong base")

    variable, = plt.plot(0, 0, color=Invisible, label=r"$\xi = \frac{V_{TIT}}{V_{EQ}}$")
    volume1, = plt.plot(0, 0, color=Invisible, label=f"$V_{{a}}({acid})={Va} mL$")
    concentration1, = plt.plot(0, 0, color=Invisible, label=f"$c_{{a}}({acid})={Ca} M$")
    volume2, = plt.plot(0, 0, color=Invisible, label=f"$V_{{EQ}}({base})={Veq} mL$")
    concentration2, = plt.plot(0, 0, color=Invisible, label=f"$c_{{b}}({base})={Ctit} M$")

    plt.hlines(pH_eq, 0, 1, color="gray", linestyles="dashed")
    plt.vlines(1, 0, 14, color="gray", linestyles="solid")

    title = f"Titration of {Ca} M {acid} with {Ctit} M {base}"
    plt.title(title)
    plt.xlim(0, 2)
    plt.xticks([0,0.5,1,1.5,2], ["0","0.5","1","1.5","2"])
    plt.xlabel('ξ ⟶')
    plt.gca().xaxis.set_minor_locator(AutoMinorLocator(n=5))
    plt.gca().tick_params(axis='x', which='minor', length=4, color='black')
    plt.gca().tick_params(axis='x', which='major', length=8, color='black')
    plt.ylim(0, 14)
    plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
    plt.ylabel('pH')
    plt.gca().yaxis.set_minor_locator(AutoMinorLocator(n=5))
    plt.gca().tick_params(axis='y', which='minor', length=4, color='black')
    plt.gca().tick_params(axis='y', which='major', length=8)

    legend1 = plt.legend(handles=[curve1, curve2, variable], labels=["pH of strong acid", "pH of strong base", r"$\xi = \frac{V_{TIT}}{V_{EQ}}$"], loc="upper left")
    legend2 = plt.legend(handles=[volume1, concentration1, volume2, concentration2], labels=[f"$V_{{A}}({acid})={Va*1000} mL$", f"$c_{{A}}({acid})={Ca} M$", f"$V_{{EQ}}({base})={Veq*1000} mL$", f"$c_{{B}}({base})={Ctit} M$"], loc='lower center', bbox_to_anchor=(0.5, -0.3), ncol=2)
    plt.gca().add_artist(legend1)
    plt.gca().add_artist(legend2)
    plt.subplots_adjust(bottom=0.25)

    plt.savefig(title + ".png", dpi=300)
    plt.show()

def Titration_sBsA(base, Vb, acid, Ctit, Veq):
    '''Traces the curve corresponding to a titration of a strong base by a strong acid.

        Calls the functions pH1 and pH2, composes them with the right constants to evaluate
        the pH as a function of the titration's degree of advancement to finally trace and
        show the titration curve.
        * Requires: pH1, pH2, numpy, matplotlib

        Args:
            base (str) :    formula / name ot the titrant base
            Vb (float) :    initial volume of titrated base
            acid (str) :    formula / name ot the titrant acid
            Veq (float) :   volume of titrant base added at equivalence point'''
    StrongAcidRed = (211/255, 4/255, 4/255)
    StrongBaseBlue = (4/255, 68/255, 140/255)
    Invisible = (0,0,0,0)

    '''Initialises important parameters'''
    Ctit = round(Ctit, 3)
    Cb = round((Ctit * Veq) / Vb, 3)
    pH_eq = 7 #pH at equivalence point

    '''Tracing the graph'''
    x1 = np.linspace(0, 0.9999, 10000)
    x2 = np.linspace(1.0001, 1.9999, 10000)

    y1 = 14 + pH1(Vb, Ctit, Veq, x1)
    y2 = -1*pH2(Vb, Ctit, Veq, x2)

    '''Formating the graph'''
    plt.figure(figsize=(8, 6))
    curve1, = plt.plot(x1, y1, color=StrongBaseBlue, label="pH of strong base")
    curve2, = plt.plot(x2, y2, color=StrongAcidRed, label="pH of strong acid")

    variable, = plt.plot(0, 0, color=Invisible, label=r"$\xi = \frac{V_{TIT}}{V_{EQ}}$")
    volume1, = plt.plot(0, 0, color=Invisible, label=f"$V_{{B}}({base})={Vb} mL$")
    concentration1, = plt.plot(0, 0, color=Invisible, label=f"$c_{{B}}({base})={Cb} M$")
    volume2, = plt.plot(0, 0, color=Invisible, label=f"$V_{{EQ}}({acid})={Veq} mL$")
    concentration2, = plt.plot(0, 0, color=Invisible, label=f"$c_{{A}}({acid})={Ctit} M$")

    plt.hlines(pH_eq, 0, 1, color="gray", linestyles="dashed")
    plt.vlines(1, 0, 14, color="gray", linestyles="solid")

    title = f"Titration of {Cb} M {base} with {Ctit} M {acid}"
    plt.title(title)
    plt.xlim(0, 2)
    plt.xticks([0,0.5,1,1.5,2], ["0","0.5","1","1.5","2"])
    plt.xlabel('ξ ⟶')
    plt.gca().xaxis.set_minor_locator(AutoMinorLocator(n=5))
    plt.gca().tick_params(axis='x', which='minor', length=4, color='black')
    plt.gca().tick_params(axis='x', which='major', length=8, color='black')
    plt.ylim(0, 14)
    plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
    plt.ylabel('pH')
    plt.gca().yaxis.set_minor_locator(AutoMinorLocator(n=5))
    plt.gca().tick_params(axis='y', which='minor', length=4, color='black')
    plt.gca().tick_params(axis='y', which='major', length=8)

    legend1 = plt.legend(handles=[curve1, curve2, variable], labels=["pH of strong base", "pH of strong acid", r"$\xi = \frac{V_{TIT}}{V_{EQ}}$"], loc="upper right")
    legend2 = plt.legend(handles=[volume1, concentration1, volume2, concentration2], labels=[f"$V_{{B}}({base})={Vb*1000} mL$", f"$c_{{B}}({base})={Cb} M$", f"$V_{{EQ}}({acid})={Veq*1000} mL$", f"$c_{{A}}({acid})={Ctit} M$"], loc='lower center', bbox_to_anchor=(0.5, -0.3), ncol=2)
    plt.gca().add_artist(legend1)
    plt.gca().add_artist(legend2)
    plt.subplots_adjust(bottom=0.25)

    plt.savefig(title + ".png", dpi=300)
    plt.show()


def Titration_wAsB(acid, pKa, Va, base, Ctit, Veq):
    '''Traces the curve corresponding to a titration of a weak acid by a strong base.

        Calls the functions pH2 and pH3, composes them with the right constants to evaluate
        the pH as a function of the titration's degree of advancement to finally trace and
        show the titration curve.
        * Requires: pH2, pH3, numpy, matplotlib

        Args:
            acid (str) :    formula / name ot the titrated acid
            pKa (float) :   pKa of the titrated acid
            Va (float) :    initial volume of the titrated acid
            base (str) :    formula / name ot the titrant base
            Ctit (float):   concentration of the the titrant base
            Veq (float) :   volume of titrant base added at equivalence point'''

    WeakAcidRed = (255/255, 138/255, 138/255)
    StrongBaseBlue = (4/255, 68/255, 140/255)
    Invisible = (0,0,0,0)

    '''Initialises important parameters'''
    Ctit = round(Ctit, 3)
    Ca = round((Ctit * Veq) / Va, 3)
    pH_eq = 7 + 1/2 * pKa + pH4(Va, Ctit, Veq, 1) #pH at equivalence point

    '''Tracing the graph'''
    x1 = np.linspace(0.01, 0.9999, 10000)
    x1_stretched = np.linspace(0, 0.9999, 10000)
    x2 = np.linspace(1.0001, 1.9999, 10000)

    y1 = pKa + pH3(x1)
    y2 = 14 + pH2(Va, Ctit, Veq, x2)

    '''Formating the graph'''
    plt.figure(figsize=(8, 6))
    curve1, = plt.plot(x1_stretched, y1, color=WeakAcidRed, label="pH of strong base")
    curve2, = plt.plot(x2, y2, color=StrongBaseBlue, label="pH of strong base")

    variable, = plt.plot(0, 0, color=Invisible, label=r"$\xi = \frac{V_{TIT}}{V_{EQ}}$")
    volume1, = plt.plot(0, 0, color=Invisible, label=f"$V_{{a}}({acid})={Va} mL$")
    concentration1, = plt.plot(0, 0, color=Invisible, label=f"$c_{{a}}({acid})={Ca} M$")
    volume2, = plt.plot(0, 0, color=Invisible, label=f"$V_{{EQ}}({base})={Veq} mL$")
    concentration2, = plt.plot(0, 0, color=Invisible, label=f"$c_{{b}}({base})={Ctit} M$")

    plt.hlines(pH_eq, 0, 1, color="gray", linestyles="dashed")
    plt.vlines(1, 0, 14, color="gray", linestyles="solid")

    title = f"Titration of {Ca} M {acid} with {Ctit} M {base}"
    plt.title(title)
    plt.xlim(0, 2)
    plt.xticks([0,0.5,1,1.5,2], ["0","0.5","1","1.5","2"])
    plt.xlabel('ξ ⟶')
    plt.gca().xaxis.set_minor_locator(AutoMinorLocator(n=5))
    plt.gca().tick_params(axis='x', which='minor', length=4, color='black')
    plt.gca().tick_params(axis='x', which='major', length=8, color='black')
    plt.ylim(0, 14)
    plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
    plt.ylabel('pH')
    plt.gca().yaxis.set_minor_locator(AutoMinorLocator(n=5))
    plt.gca().tick_params(axis='y', which='minor', length=4, color='black')
    plt.gca().tick_params(axis='y', which='major', length=8)

    legend1 = plt.legend(handles=[curve1, curve2, variable], labels=["pH of weak acid", "pH of strong base", r"$\xi = \frac{V_{TIT}}{V_{EQ}}$"], loc="upper left")
    legend2 = plt.legend(handles=[volume1, concentration1, volume2, concentration2], labels=[f"$V_{{A}}({acid})={Va*1000} mL$", f"$c_{{A}}({acid})={Ca} M$", f"$V_{{EQ}}({base})={Veq*1000} mL$", f"$c_{{B}}({base})={Ctit} M$"], loc='lower center', bbox_to_anchor=(0.5, -0.3), ncol=2)
    plt.gca().add_artist(legend1)
    plt.gca().add_artist(legend2)
    plt.subplots_adjust(bottom=0.25)

    plt.savefig(title + ".png", dpi=300)
    plt.show()


def Titration_wBsA(base, pKa, Vb, acid, Ctit, Veq):
    '''Traces the curve corresponding to a titration of a weak base by a strong acid.

        Calls the functions pH2 and pH3, composes them with the right constants to evaluate
        the pH as a function of the titration's degree of advancement to finally trace and
        show the titration curve.
        * Requires: pH2, pH3, numpy, matplotlib

        Args:
            base (str) :    formula / name ot the titrated base
            pKa (float) :   pKa of the titrated base
            Vb (float) :    initial volume of the titrated base
            acid (str) :    formula / name ot the titrant acid
            Ctit (float):   concentration of the the titrant acid
            Veq (float) :   volume of titrant acid added at equivalence point'''
    StrongAcidRed = (211/255, 4/255, 4/255)
    WeakBaseBlue = (4/255, 171/255, 211/255)
    Invisible = (0,0,0,0)

    '''Initialises important parameters'''
    Ctit = round(Ctit, 3)
    Cb = round((Ctit * Veq) / Vb, 3)
    pH_eq = 1/2 * pKa - pH4(Vb, Ctit, Veq, 1) #pH at equivalence point

    '''Tracing the graph'''
    x1 = np.linspace(0.01, 0.9999, 10000)
    x1_stretched = np.linspace(0, 0.9999, 10000)
    x2 = np.linspace(1.0001, 1.9999, 10000)

    y1 = pKa - pH3(x1)
    y2 = -1 * pH2(Vb, Ctit, Veq, x2)

    '''Formating the graph'''
    plt.figure(figsize=(8, 6))
    curve1, = plt.plot(x1_stretched, y1, color=WeakBaseBlue, label="pH of weak base")
    curve2, = plt.plot(x2, y2, color=StrongAcidRed, label="pH of strong acid")

    variable, = plt.plot(0, 0, color=Invisible, label=r"$\xi = \frac{V_{TIT}}{V_{EQ}}$")
    volume1, = plt.plot(0, 0, color=Invisible, label=f"$V_{{B}}({base})={Vb} mL$")
    concentration1, = plt.plot(0, 0, color=Invisible, label=f"$c_{{B}}({base})={Cb} M$")
    volume2, = plt.plot(0, 0, color=Invisible, label=f"$V_{{EQ}}({acid})={Veq} mL$")
    concentration2, = plt.plot(0, 0, color=Invisible, label=f"$c_{{A}}({acid})={Ctit} M$")

    plt.hlines(pH_eq, 0, 1, color="gray", linestyles="dashed")
    plt.vlines(1, 0, 14, color="gray", linestyles="solid")

    title = f"Titration of {Cb} M {base} with {Ctit} M {acid}"
    plt.title(title)
    plt.xlim(0, 2)
    plt.xticks([0,0.5,1,1.5,2], ["0","0.5","1","1.5","2"])
    plt.xlabel('ξ ⟶')
    plt.gca().xaxis.set_minor_locator(AutoMinorLocator(n=5))
    plt.gca().tick_params(axis='x', which='minor', length=4, color='black')
    plt.gca().tick_params(axis='x', which='major', length=8, color='black')
    plt.ylim(0, 14)
    plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
    plt.ylabel('pH')
    plt.gca().yaxis.set_minor_locator(AutoMinorLocator(n=5))
    plt.gca().tick_params(axis='y', which='minor', length=4, color='black')
    plt.gca().tick_params(axis='y', which='major', length=8)

    legend1 = plt.legend(handles=[curve1, curve2, variable], labels=["pH of weak base", "pH of strong acid", r"$\xi = \frac{V_{TIT}}{V_{EQ}}$"], loc="upper right")
    legend2 = plt.legend(handles=[volume1, concentration1, volume2, concentration2], labels=[f"$V_{{B}}({base})={Vb*1000} mL$", f"$c_{{B}}({base})={Cb} M$", f"$V_{{EQ}}({acid})={Veq*1000} mL$", f"$c_{{A}}({acid})={Ctit} M$"], loc='lower center', bbox_to_anchor=(0.5, -0.3), ncol=2)
    plt.gca().add_artist(legend1)
    plt.gca().add_artist(legend2)
    plt.subplots_adjust(bottom=0.25)

    plt.savefig(title + ".png", dpi=300)
    plt.show()


def Titration_dAsB(acid, pKa1, pKa2, Va, base, Ctit, Veq):
    '''Traces the curve corresponding to a titration of a diprotic (weak) acid by a strong base.

        Calls the functions pH2, pH_log_interpolation1 and pH_log_interpolation1 composes them
        with the right constants to evaluate the pH as a function of the titration's degree of
        advancement to finally trace and show the titration curve.
        * Requires: pH2, pH_log_interpolation1 and pH_log_interpolation1

        Args:
            acid (str) :    formula / name ot the titrated acid
            pKa1 (float) :  1st pKa of the titrated acid
            pKa2 (float) :  2nd pKa of the titrated acid
            Va (float) :    initial volume of the titrated acid
            base (str) :    formula / name ot the titrant base
            Ctit (float):   concentration of the the titrant base
            Veq (float) :   volume of titrant base added at equivalence point'''
    WeakAcidRed = (255/255, 138/255, 138/255)
    StrongBaseBlue = (4/255, 68/255, 140/255)
    Invisible = (0,0,0,0)

    '''Initialises important parameters'''
    Ctit = round(Ctit, 3)
    Ca = round((Ctit * Veq) / Va, 3)

    pH_a = 1/2 * pKa1 - 1/2 * np.log10(Ca)
    pH_b = pKa1
    pH_c = 1/2 * pKa1 + 1/2 * pKa2
    pH_d = pKa2
    pH_e = 7 + 1/2 * pKa2 + pH2(Va, Ctit, Veq, 2)

    pH_data1 = [(0.0001, pH_a), (0.5, pH_b)]
    pH_data2 = [(0, pH_b), (0.4999, pH_c)]
    pH_data3 = [(0.0001, pH_c), (0.5, pH_d)]
    pH_data4 = [(0, pH_d), (0.4999, pH_e)]

    pH_eq1 = pH_c # pH at 1st equivalence point
    pH_eq2 = pH_e # pH at 2nd equivalence point

    '''Tracing the graph'''
    x1 = pH_log_interpolation1(pH_data1)[0]
    x2 = pH_log_interpolation2(pH_data2)[0] + 0.5
    x3 = pH_log_interpolation1(pH_data3)[0] + 1
    x4 = pH_log_interpolation2(pH_data4)[0] + 1.5
    x5 = np.linspace(2.0001, 3, 10000)

    y1 = pH_log_interpolation1(pH_data1)[1]
    y2 = pH_log_interpolation2(pH_data2)[1]
    y3 = pH_log_interpolation1(pH_data3)[1]
    y4 = pH_log_interpolation2(pH_data4)[1]
    y5 = 14 + pH2(Va, Ctit, Veq, x5-1)

    '''Formating the graph'''
    plt.figure(figsize=(8, 6))
    curve1A, = plt.plot(x1, y1, color=WeakAcidRed)
    curve1B, = plt.plot(x2, y2, color=WeakAcidRed)
    curve2A, = plt.plot(x3, y3, color="green")
    curve2B, = plt.plot(x4, y4, color="green")
    curve3, = plt.plot(x5, y5, color=StrongBaseBlue)

    variable, = plt.plot(0, 0, color=Invisible, label=r"$\xi = \frac{V_{TIT}}{V_{EQ}}$")
    volume1, = plt.plot(0, 0, color=Invisible, label=f"$V_{{A}}({acid})={Va} mL$")
    concentration1, = plt.plot(0, 0, color=Invisible, label=f"$c_{{A}}({acid})={Ca} M$")
    volume2, = plt.plot(0, 0, color=Invisible, label=f"$V_{{EQ1}}({base})={Veq} mL$")
    concentration2, = plt.plot(0, 0, color=Invisible, label=f"$c_{{B}}({base})={Ctit} M$")

    plt.hlines(pH_eq1, 0, 1, color="gray", linestyles="dashed")
    plt.vlines(1, 0, 14, color="gray", linestyles="solid")
    plt.hlines(pH_eq2, 0, 2, color="gray", linestyles="dashed")
    plt.vlines(2, 0, 14, color="gray", linestyles="solid")

    title = f"Titration of {Ca} M {acid} with {Ctit} M {base}"
    plt.title(title)
    plt.xlim(0, 2)
    plt.xticks([0,0.5,1,1.5,2, 2.5, 3], ["0","0.5","1","1.5","2", "2.5", "3"])
    plt.xlabel('ξ ⟶')
    plt.gca().xaxis.set_minor_locator(AutoMinorLocator(n=5))
    plt.gca().tick_params(axis='x', which='minor', length=4, color='black')
    plt.gca().tick_params(axis='x', which='major', length=8, color='black')
    plt.ylim(0, 14)
    plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
    plt.ylabel('pH')
    plt.gca().yaxis.set_minor_locator(AutoMinorLocator(n=5))
    plt.gca().tick_params(axis='y', which='minor', length=4, color='black')
    plt.gca().tick_params(axis='y', which='major', length=8)

    legend1 = plt.legend(handles=[curve1A, curve2A, curve3, variable], labels=["pH of weak acid", "intermediate pH", "pH of strong base", r"$\xi = \frac{V_{TIT}}{V_{EQ}}$"], loc="lower right")
    legend2 = plt.legend(handles=[volume1, concentration1, volume2, concentration2], labels=[f"$V_{{A}}({acid})={Va*1000} mL$", f"$c_{{A}}({acid})={Ca} M$", f"$V_{{EQ}}({base})={Veq*1000} mL$", f"$c_{{B}}({base})={Ctit} M$"], loc='lower center', bbox_to_anchor=(0.5, -0.3), ncol=2)
    plt.gca().add_artist(legend1)
    plt.gca().add_artist(legend2)
    plt.subplots_adjust(bottom=0.25)

    plt.savefig(title + ".png", dpi=300)
    plt.show()


def Titration():
    '''User interface to facilitate the usage of the different titration functions.

        Integrates all the titration modes into one single callable function that decides which case is applicable,
        then traces the corresponding titration curve. Invalid parameters will be rejected.
        * Requires: Titration_sAsB(), Titration_sBsA(), Titration_wAsB(), Titration_wBsA(), Titration_dAsB()'''
    while True:
        try:
            mode = int(input("\033[1m" + "\nSelect the type of titration you want to perform." + "\033[0m"
                         "\n∘ acid titrated by (strong) base --- 1"
                         "\n∘ base titrated by (strong) acid --- 2"
                         "\n\033[1m" + "Make your choice (1/2): " + "\033[0m"))

            if mode == 1:
                print("\033[1m" + "\nPlease enter your data:" + "\033[0m")
                acid = input("∘ chemical formula of titrated acid: ")
                while True:
                    try:
                        pKa1 = float(input("∘ (acid) pKa1 [-] = "))
                        break
                    except:
                        print("\033[1m" + "Enter a valid pKa1 [-]!" + "\033[0m")

                while True:
                    try:
                        pKa2 = input("∘ (acid) pKa2 [-] (type '*' if there is none) =  ")
                        if pKa2 == float(pKa2):
                            pKa2 = float(pKa2)
                        if pKa2 == "*":
                            pKa2 = "*"
                        break
                    except:
                        print("\033[1m" + "Enter a valid pKa2 [-]!" + "\033[0m")

                while True:
                    try:
                        Va = float(input("∘ initial volume of titrated acid: Va [L] = "))
                        break
                    except:
                        print("\033[1m" + "Enter a valid volume [L]!" + "\033[0m")

                base = input("∘ chemical formula of titrant base: ")

                while True:
                    try:
                        Ctit = float(input("∘ concentration of titrant base: Ctit [molL⁻¹] = "))
                        break
                    except:
                        print("\033[1m" + "Enter a valid concentration [molL⁻¹]!" + "\033[0m")

                while True:
                    try:
                        Veq = float(input("∘ volume of titrant solution at (first) equivalence point: Veq [L] = "))
                        break
                    except:
                        print("\033[1m" + "Enter a valid volume [L]!" + "\033[0m")

                l_pKa = []
                for pKa in pKa1, pKa2:
                    if pKa != "*":
                        l_pKa.append(pKa)

                if len(l_pKa) == 1:
                    pKa = l_pKa[0]

                    if pKa < -1.74:  # Strong acid case
                        print("\033[1m" + "\nFind hereafter the corresponding titration curve." + "\033[0m")
                        Titration_sAsB(acid, Va, base, Ctit, Veq)
                    else:  # Weak acid case
                        print("\033[1m" + "\nFind hereafter the corresponding titration curve." + "\033[0m")
                        Titration_wAsB(acid, pKa, Va, base, Ctit, Veq)

                else:
                    pKa1 = l_pKa[0]
                    pKa2 = float(l_pKa[1])

                    Delta_pKa = pKa2 - pKa1
                    if Delta_pKa > 4.5:  # Second acid dissociation negligible
                        print(
                            "\033[1m" + "\nThe second acid dissociation will be neglected, as pKa1 << pKa2." + "\033[0m")
                        pKa = pKa1

                        if pKa < -1.74:  # Strong acid case
                            print("\033[1m" + "Find hereafter the corresponding titration curve." + "\033[0m")
                            Titration_sAsB(acid, Va, base, Ctit, Veq)
                        else:  # Weak acid case
                            print("\033[1m" + "Find hereafter the corresponding titration curve." + "\033[0m")
                            Titration_wAsB(acid, pKa, Va, base, Ctit, Veq)


                    else:  # Diprotic acid case
                        print("\033[1m" + "\nFind hereafter the corresponding titration curve." + "\033[0m")
                        Titration_dAsB(acid, pKa1, pKa2, Va, base, Ctit, Veq)
                break

            if mode == 2:
                print("\033[1m" + "\nPlease enter your data:" + "\033[0m")
                base = input("∘ chemical formula of titrated base: ")
                while True:
                    try:
                        pKb = float(input("∘ (base) pKb [-] = "))
                        break
                    except:
                        print("\033[1m" + "Enter a valid pKb [-]!" + "\033[0m")

                while True:
                    try:
                        Vb = float(input("∘ initial volume of titrated base: Vb [L] = "))
                        break
                    except:
                        print("\033[1m" + "Enter a valid volume [L]!" + "\033[0m")

                acid = input("∘ chemical formula of titrant acid: ")

                while True:
                    try:
                        Ctit = float(input("∘ concentration of titrant acid: Ctit [molL⁻¹] = "))
                        break
                    except:
                        print("\033[1m" + "Enter a valid concentration [molL⁻¹]!" + "\033[0m")

                while True:
                    try:
                        Veq = float(input("∘ volume of titrant solution at (first) equivalence point: Veq [L] = "))
                        break
                    except:
                        print("\033[1m" + "Enter a valid volume [L]!" + "\033[0m")

                pKa = 14 - pKb

                if pKa > 10.2:  # Strong base case
                    print("\033[1m" + "\nFind hereafter the corresponding titration curve." + "\033[0m")
                    Titration_sBsA(base, Vb, acid, Ctit, Veq)

                else:  # Weak base case
                    print("\033[1m" + "\nFind hereafter the corresponding titration curve." + "\033[0m")
                    Titration_wBsA(base, pKa, Vb, acid, Ctit, Veq)
                break
        except:
            print("\033[1m" + "Make a valid choice (1/2)!" + "\033[0m")

#Titration_sAsB("HCl", 0.25, "NaOH", 1, 0.2)
#Titration_sBsA("NaOH", 0.2, "HCl", 0.1, 0.1)
#Titration_wAsB("CH3COOH", 4.756, 0.250, "NaOH", 0.1, 0.10)
#Titration_wBsA("NH3", 9.249, 0.125, "HCl", 0.1, 0.05)
#Titration_dAsB("H2CO3", 6.36, 10.25, 0.1, "NaOH", 0.4, 0.050)

