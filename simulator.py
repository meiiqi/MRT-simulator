# -*- coding: utf-8 -*-
"""
McGill Rocket Team Flight Simulator
Authors: Matt Saathoff, Mei Qi Tang

The simulator class configures the simulations. After reading input configuration instructions, it will call the
simulation class to execute simulations according to the configs. Possible configurable variables could be the number
of simulations to run (eg. 100), the specific modules active in each simulation (eg. atmospheric model), the type of simulation
to run (eg. vertical fire test), etc.
"""

# import numpy as np
# import matplotlib.pyplot as plt
# import IPython.display as IPy
# from math import factorial
# import helper

#STEP 1: read, validate, and store values from input JSON config file

#STEP 2: run (instantiate) simulations according to the configs