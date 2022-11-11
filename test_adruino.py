# Gemaakt door Martijn Laarhoven 12579866 op 11/11/2022

import matplotlib.pyplot as plt
import pandas as pd
import csv

from arduino_device import ArduinoVISADevice, list_devices

from diode_experiment import DiodeExperiment

port = "ASRL4::INSTR"

Experiment = DiodeExperiment()

voltagelist, Currentlist = Experiment.scan()

# plotje
plt.scatter(voltagelist,Currentlist, s=5,c='green')
plt.xlabel('$U_\mathrm{LED}$ [V]')
plt.ylabel('$I$ [A]')
plt.show()


# Het maken van een csv file
with open("adruinodata.txt", "w",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["voltage_LED,Current_resistor"])
    for u, i in zip(voltagelist,Currentlist):
        writer.writerow([u,i])


