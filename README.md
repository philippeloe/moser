![Project Logo](assets/banner2.png)

![Coverage Status](assets/coverage-badge.svg)

<h1 align="center">
MOSER.py
</h1>

<br>

MOSER.py (for Molecular Operations and Solutions for Equilibria and Reactions) is a versatile Python package designed for physical chemistry calculations. It enables users to balance chemical equations, trace titration curves, calculate solutions' concentrations and pH, determine molar masses, evaluate reactional quotients, and analyze reaction kinetics efficiently and accurately.

## 🔬 Usage

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
![Titration example](assets/Tit1.png)
<img src="assets/Tit1.png" alt="Titration example" width="300" height="200">

This usage example shows how to quickly leverage the package's main functionality with just one line of code (or a few lines of code). 
After importing the `main_func` (to be renamed by you), you simply pass in your `data` and get the `result` (this is just an example, your package might have other inputs and outputs). 
Short and sweet, but the real power lies in the detailed documentation.

## 👩‍💻 Installation

Create a new environment, you may also give the environment a different name. 

```
conda create -n moser python=3.10 
```

```
conda activate moser
(conda_env) $ pip install .
```

If you need jupyter lab, install it 

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

### Run tests and coverage

```
(conda_env) $ pip install tox
(conda_env) $ tox
```



