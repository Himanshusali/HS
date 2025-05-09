# Dispatch Optimization for Heat Pumps with Buffer Tank
# See article for further details.
# This file contains basic definiton and settings for the heat pump,
# buffer tank and it loads the data file.
# Import all defintions from this file in your python (Jupyter Notebook) code 
#
# Copyright, 2024, Mathias Moog, Hochschule Ansbach, Deutschland, CC-BY-NC-SA

# Load modules
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt



# -----------------------------------------------------
# Heat Pump and CoP
# Nominal electric power of the heatpump in kW
#Pel = 3
# Maximal heating power output of the heatpump in kW
Pth = 12
# Usual eta for air water heat pump
eta   = 0.35
# CoP formula, all temperatures in °C, can be uses with vectors or floats
CoP   = lambda Tcold,Thot: np.minimum(6,eta*(273.1+Thot)/np.maximum(Thot-Tcold,1))
#CoP(Tout,35)

# Flow temperature of the floor heating system (heating curve)
# Estimate flow temperature
# See MeinHausTagEinfach and master thesis Katodia, linear model for flow temp.
# As function of outside Temperature
def fTflow(Tout):
    return Tout*(-0.235)+24.82+7 



# -----------------------------------------------------
# Buffer tank
# Maximal flow temperature provided by heat pump
Tmax = 60
# specific heat capacity for water in kJ/kg/K
cp = 4.2
# Volume of buffer Tank in L
V = 500
# Absolut heat capacity of buffer tank in kWh/K
C = cp*V/3600
# Capacity in kWh
Qmax = (Tmax-35)*C
# Intial condition for buffer Tank temperature
Tinit = 30; # empty

