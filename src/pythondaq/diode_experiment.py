from pythondaq.arduino_device import ArduinoVISADevice, list_devices

import numpy as np
class DiodeExperiment():
    """The class which runs the experiment
    """
    def __init__(self):
        """The initial module which has the self function and the port
        """
        port = "ASRL::SIMPV::INSTR"
        self.device = ArduinoVISADevice(port=port)
        # self.list_devices = list_devices
        # return list_devices

    def scan(self, startvalue, endvalue):
        """The scan function which makes the current and the voltagelists

        Returns:
            lists: Voltagelist and Currentlist
        """
        # Het aanmaken van lijsten om later te kunnen plotten
        Currentlist = []
        voltagelist = []
        powerlist = []
        Ressistancelist = []

        # Een for loop om het voltage steeds iets op te kunnen laten lopen
        for Voltage in range(startvalue, endvalue):
            # Het voltage steeds iets verhogen
            self.device.set_output_value(Voltage)

            # De Voltage en Curretn waarden over de weerstand verkrijgen
            voltage_resistor = self.device.get_input_voltage(2)
            Current_resistor = voltage_resistor /4.7
            Currentlist.append(Current_resistor) #current LED = current resistor

            # Het voltage over de LED verkrijgen
            voltage_zc = (self.device.get_input_voltage(2) - self.device.get_input_voltage(1)) * 3 #times 3 because of the voltagesplitter
            voltage_zc = np.abs(voltage_zc)
            voltagelist.append(voltage_zc)
            powerlist.append(voltage_zc * Current_resistor)
            # Ressistancelist.append(voltage_zc / Current_resistor) 

        # Device uitzetten als het klaar is
        self.device.turn_off_device()
        # print(voltagelist)

        return voltagelist, Currentlist, powerlist, Ressistancelist
