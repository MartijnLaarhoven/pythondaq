import click
import matplotlib.pyplot as plt
import csv

from pythondaq.diode_experiment import DiodeExperiment

@click.group()
def cmd_group():
    pass

@cmd_group.command()
@click.option(
    "-s",
    "--startvalue",
    type=click.FloatRange(0, 3.3),
    default = 0,
    help = "startvalue in Volt",
)
@click.option(
    "-e",
    "--endvalue",
    type=click.FloatRange(0, 3.3),
    default = 3.3,
    help = "endvalue in Volt",
)
@click.option(
    "-m",
    "--output/--no-makefile",
    "--FILENAME",
    help = "make a CVS file",
)
def scan(startvalue, endvalue, output):
    """running the experiment and making a csv file
    """
    port = "ASRL4::INSTR"
    Experiment = DiodeExperiment()
    voltagelist, Currentlist = Experiment.scan(int(startvalue*(1023/3.3)), int(endvalue*(1023/3.3)))
    # plt.scatter(voltagelist,Currentlist, s=5,c='green')
    # plt.xlabel('$U_\mathrm{LED}$ [V]')
    # plt.ylabel('$I$ [A]')
    # plt.show()

    if output:
    # making a csv file
        with open("FILENAME.txt", "w",newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["voltage_LED,Current_resistor"])
            for u, i in zip(voltagelist,Currentlist):
                writer.writerow([u,i])
    return 


@cmd_group.command()
@click.option(
    "-l",
    "--list/--no_list",
    default = 0,
    help = "list or no list"
)
def lijst(list):
    print("list")
    return

