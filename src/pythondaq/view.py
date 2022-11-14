# Gemaakt door Martijn Laarhoven 12579866 op 4/11/2022 tot 11/11/2022

import matplotlib.pyplot as plt
import csv

from pythondaq.diode_experiment import DiodeExperiment

def view():

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



# opdracht 3.7 is niet gelukt door de tijd.
# Het idee van opdracht 3.7 was om de fout op de waarden te vinden, dit zou gedaan kunnen worden door de meting een aantal keer te doen, 
# daar het gemiddelde van te nemen en de fout als de standaarddeviatie / sqrt(n) te nemen.