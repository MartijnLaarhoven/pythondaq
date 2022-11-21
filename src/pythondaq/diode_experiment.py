from pythondaq.arduino_device import ArduinoVISADevice, list_devices

class DiodeExperiment():
    """The class which runs the experiment
    """
    def __init__(self):
        """The initial module which has the self function and the port
        """
        port = "ASRL4::INSTR"
        self.device = ArduinoVISADevice(port=port)

    def scan(self, startvalue, endvalue):
        """The scan function which makes the current and the voltagelists

        Returns:
            lists: Voltagelist and Currentlist
        """
        # Het aanmaken van lijsten om later te kunnen plotten
        Currentlist = []
        voltagelist = []

        # Een for loop om het voltage steeds iets op te kunnen laten lopen
        for Voltage in range(startvalue, endvalue):

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

    # def 
