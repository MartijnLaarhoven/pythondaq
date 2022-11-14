# Gemaakt door Martijn Laarhoven 12579866 op 11/11/2022

from arduino_device import ArduinoVISADevice, list_devices

class DiodeExperiment:

    # Eerst een init
    def __init__(self):
        port = "ASRL4::INSTR"
        self.device = ArduinoVISADevice(port=port)

    # Functie om de scan te maken
    def scan(self):
        # Het aanmaken van lijsten om later te kunnen plotten
        Currentlist = []
        voltagelist = []

        # Een for loop om het voltage steeds iets op te kunnen laten lopen
        for Voltage in range(1023):

            # Het voltage steeds iets verhogen
            self.device.set_output_value(Voltage)

            # De Voltage en Curretn waarden over de weerstand verkrijgen
            voltage_resistor = self.device.get_input_voltage(2)
            Current_resistor = voltage_resistor / 220
            Currentlist.append(Current_resistor) #current LED = current resistor

            # Het voltage over de LED verkrijgen
            voltage_LED = self.device.get_input_voltage(1) - self.device.get_input_voltage(2)
            voltagelist.append(voltage_LED)

        # Device uitzetten als het klaar is
        self.device.turn_off_device()

        return voltagelist, Currentlist


