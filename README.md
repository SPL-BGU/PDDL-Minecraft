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
2. To generate new maps (to dataset directory) just run:
```
python constructor.py

required options:
  -h, --help      show this help message and exit
  --map_size int  Size of the map (must be >= 6)
  --num_maps int  Number of maps to generate
  --task {0,1}    Task type: 0 for WoodenSword, 1 for PogoStick

You can change the starting item range in the config.json file
```

# Citations

If you find this repository useful or use it in your research, please consider citing the following paper:
```
@inproceedings{benyamin2024crafting,
 title={Crafting a Pogo Stick in Minecraft with Heuristic Search},
 author={Benyamin, Yarin and Mordoch, Argaman and Shperberg, Shahaf and Piotrowski, Wiktor and Stern, Roni},
 booktitle={Proceedings of the International Symposium on Combinatorial Search},
 volume={17},
 pages={261--262},
 year={2024}
}
```
If you are using the basic (“counting”) version of the domain, please also cite:
```
@inproceedings{benyamin2023model,
  title={Model Learning to Solve Minecraft Tasks},
  author={Benyamin, Yarin and Mordoch, Argaman and Shperberg, Shahaf S and Stern, Roni},
  booktitle={PRL Workshop in ICAPS},
  year={2023}
}
```
