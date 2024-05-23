![Project Logo](assets/banner2.png)

![Coverage Status](assets/coverage-badge.svg)

<h1 align="center">
MOSER.py
</h1>

<br>

__MOSER.py__ (for **M**olecular **O**perations and **S**olutions for **E**quilibria and **R**eactions) is a versatile Python package designed for physical chemistry calculations. 

## 🔬 Usage
Unlocking an abundance of analytical tools, __MOSER.py__ serves as an invaluable companion for chemistry students, providing intuitive functionalities for essential calculations and analyses. __MOSER.py__ streamlines complex tasks, empowering students to deepen their understanding of physical chemistry concepts and accelerate their learning journey. Among other features, it enables the users to:

__1. Balance Chemical Equations__ <br>
Easily balance chemical equations with a simple function call. __MOSER.py__ uses advanced algorithms to ensure accurate balancing of equations.

__2. Calculate Molar Mass__ <br>
Determine the molar mass of chemical compounds effortlessly with __MOSER.py__. Input the chemical formula, and __MOSER.py__ will compute the molar mass for you.

__3. Determine the Reactional Quotient__ <br>
Evaluate reaction quotients and kinetics parameters using __MOSER.py__'s intuitive interface.

__4. Evaluate a Solution's Concentration and pH__ <br>
Quickly calculate the concentration of solutions and pH values using __MOSER.py__. Specify the relevant parameters, such as the initial concentration of the solute and the volume of the solution, to obtain accurate results.

__5. Simualte Titration Curves__ <br>
Trace titration curves for acid-base titrations and visualize the pH changes throughout the titration process. Specify the concentrations of the acid and base, as well as the volume of titrant added, to generate detailed titration curves.
```python
from moser import Titration

Select the type of titration you want to perform.
∘ acid titrated by (strong) base --- 1
∘ base titrated by (strong) acid --- 2
Make your choice (1/2): 1

Please enter your data:
∘ chemical formula of titrated acid: HO2CCH(OH)CH(OH)CO2H 
∘ (acid) pKa1 [-] = 3.07
∘ (acid) pKa2 [-] (type '*' if there is none) =  4.34
∘ initial volume of titrated acid: Va [L] = 0.100
∘ chemical formula of titrant base: NaOH
∘ concentration of titrant base: Ctit [molL⁻¹] = 0.010
∘ volume of titrant solution at (first) equivalence point: Veq [L] = 0.010

Find hereafter the corresponding titration curve.
```
<p align="center">
    <img src="assets/Tit1.png" alt="Alt Text" width="500" style="display:block; margin:auto;">
</p>

__5. Investigate Kinetics__ <br>
Analyze reaction rates, rate constants, and other kinetic parameters with ease.

## 💿 Setup 
__1. Set up an environment__ <br>
Create a new environment, you may also give the environment a different name:
```
conda create -n moser python=3.10 
```
```
conda activate moser
(conda_env) $ pip install .
```
__2. Install Dependencies__ <br>
Before installing __MOSER.py__, make sure to install the following dependencies:  <br>
•NumPy <br>
•SciPy <br>
•SymPy <br>
•Matplotlib <br>
•Itertools <br>

__3. Install MOSER.py__ <br>
Once you have installed the dependencies, you can install __MOSER.py__ using pip: <br>
```python
pip install moser
```

__4. Jupyter Lab <br>__
If you need Jupyter Lab, install it:

```
(moser) $ pip install jupyterlab
```

## 🛠️ Development installation

Initialize Git (only for the first time). 

Note: You should have create an empty repository on `https://github.com:philippeloe/moser`.

```
git init
git add * 
git add .*
git commit -m "Initial commit" 
git branch -M main
git remote add origin git@github.com:philippeloe/moser.git 
git push -u origin main
```

Then add and commit changes as usual. 

To install the package, run

```
(moser) $ pip install -e ".[test,doc]"
```

## 🔎 Run tests and coverage

```
(conda_env) $ pip install tox
(conda_env) $ tox
```

## 📖 Licence
Distributed under the MIT License. See ```LICENSE.txt``` for more information.



