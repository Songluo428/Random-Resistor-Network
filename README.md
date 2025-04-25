# Random-Resistor-Network
This project aims to store the source code of the Random resistor network model used in the electrical anisotropy calculation for the continental crust.

This repository contains 1 distribution function data, 3 source code, and the simulation results:

Distribution function.zip: the electrical anisotropy of single crystal is calculated by transforming the orientation matrix to Euler angles. This file is composed of the electrical anisotropy of each single crystal in the reference coordinate system and corresponding distribution functions.

Random.py: The code can be run once to generate two text files (componentsx and componentsy), i.e. a resistor networks in both directions. Importing these files into the circuit simulator (https://lushprojects.com/circuitjs/) allows a calculation to be performed.
line 4: the first parameter represents the network size (n); the second parameter represents the resisitance vaules of the second mineral phases; the third parameter represents the number of the second mineral phases in the network (Single-phase model that is, the third parameter ie equal to zero).
lines 6 to 22 : the distribution functions of electrical anisotropy for high-anisotropy minerals (Qtz or Pl).

Layering (Middle crust).py: the code generates compenents20x and components20y, which composed of 9 layers (Qtz and Qtz+Plag layers) .
line 4 : the first parameter represents the network size (n); the second parameter represents the resisitance vaules of the second mineral phases; the third parameter is none; the 4-7th parameters represent the numbers of the second mineral phases in the polymineralic layers (Qtz+Plag layers).

Layering (Lower crust).py: the code generates a resistor network consisting of 10 layers (Plag-rich and Cpx-rich layers).
line 4 : the 4-13th parameters represent the numbers of the second mineral phases in each layer.
