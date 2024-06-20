<h1 align="center">PDDL Problem Generator for Minecraft Domain</h2>
<p align="center">
<a href="https://github.com/SPL-BGU/PDDL-Minecraft/blob/main/LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg"></a>
<a href="https://www.python.org/downloads/release/python-3818/"><img alt="Python Version" src="https://img.shields.io/badge/python-3.8-blue"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

# Getting Started
In this project, you will generate PDDL2.1 Minecraft maps. The output includes two versions of the same task - basic (item counts model) and advanced (all blocks model) and you can read more about them in [this link](https://prl-theworkshop.github.io/prl2024-icaps/papers/6.pdf).

## Dependencies
pip install all the requirements for this project:
```
python -m pip install -r requirements.txt
```

# Usage

## How to reproduce the results from the paper
1. The original domain and problem are located in the directory:
```
planning/
```
2. To generate new maps just run:
```
python constructor.py
```
3. Customize changes:
```
Change the map size in line 18
Change the number of maps to generate in line 19
Alter between the two tasks in line 20
Change the starting item range in lines 25 and 29
```

# Citations

If you find our work interesting or the repo useful, please consider citing this paper:
```
Coming Soon
```
