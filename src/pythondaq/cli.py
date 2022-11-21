import click
import matplotlib.pyplot as plt
import csv

from pythondaq.diode_experiment import DiodeExperiment


@click.group()
def cmd_group():
    pass


@cmd_group.command()
@click.option(
    "-l",
    "--list/--no_list",
)
def lijst(list):
    print("list")
    return


@cmd_group.command()
@click.option(
    "-s",
    "--scanning/--not_scanning",
)
def scan(scanning):
    print("scan")
    return 

