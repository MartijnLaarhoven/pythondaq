import click
import matplotlib.pyplot as plt
import csv

from pythondaq.diode_experiment import DiodeExperiment, list_devices

@click.group()
def cmd_group():
    pass

@cmd_group.command()
@click.option(
    "-s",
    "--startvalue",
    type=click.FloatRange(0, 3.3),
    default = 0,
    help = "startvalue in Volt, this value should be lower than the endvalue and a mimimum of 0 Volt. Type -s STARTVALUE (in Volt)",
)
@click.option(
    "-e",
    "--endvalue",
    type=click.FloatRange(0, 3.3),
    default = 3.3,
    help = "endvalue in Volt, this value should be higher than the startvalue and a maximum of 3.3 Volt. Type -e ENDVALUE (in Volt)",
)
@click.option(
    "-output",
    "--FILENAME",
    help = "make a CVS file, type -output FILENAME to make a csv file and name it with FILENAME",
)
@click.option(
    "--graph/--no-graph",
    help = "make a plot, type --graph to make a plot",
)
def scan(startvalue, endvalue, filename, graph):
    """running the experiment and making a csv file and a plot
    """
    port = "ASRL4::INSTR"
    Experiment = DiodeExperiment()
    voltagelist, Currentlist = Experiment.scan(int(startvalue*(1023/3.3)), int(endvalue*(1023/3.3)))

    if filename:
        # making a csv file
        with open(f"{filename}.txt", "w",newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["voltage_LED,Current_resistor"])
            for u, i in zip(voltagelist,Currentlist):
                writer.writerow([u,i])
    if graph:
        # making a plot
        plt.scatter(voltagelist,Currentlist, s=5,c='green')
        plt.xlabel('$U_\mathrm{LED}$ [V]')
        plt.ylabel('$I$ [A]')
        plt.show()
    return 

# @cmd_group.command()
# @click.option(
#     "-l",
#     "--lijst/--no_lijst",
#     help = "list or no list"
# )
# def lijst(lijst):
#     from list_devices 
#     if lijst:
#         print(ports)
#     return

