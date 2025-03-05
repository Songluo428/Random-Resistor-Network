# Random-Resistor-Network
This project aims to store the source code of the Random resistor network model used in the electrical anisotropy calculation for the continental crust.

This repository contains 3 source code: 
Random.py: The code can be run once to generate two text files (componentsx and componentsy), i.e. a resistor networks in both directions. Importing these files into the circuit simulator (https://lushprojects.com/circuitjs/) allows a calculation to be performed.
line 4: the first parameter represents the network size (n); the secondy parameter represents the resisitance vaules of secondary mineral phases; the third parameter represents the number of secondary mineral phases in the network.
lines 6 to 22 : the distribution functions of electrical anisotropy for first minerals (Qtz or Pl).

Layering (Middle crust).py: the code generates compenents20x and components20y, which composed of 9 layers (Qtz and Qtz+Plag layers) .
line 4 : the first parameter represents the network size (n); the secondy parameter represents the resisitance vaules of secondary mineral phases; the third parameter is none; the 4-7th parameter represent the numbers secondary mineral phases in different layers.

Layering (Lower crust).py: the code generates a resistor network consisting of 10 layers (Plag-rich and Cpx-rich layers).
