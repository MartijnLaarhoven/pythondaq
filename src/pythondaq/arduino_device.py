# Gemaakt door Martijn Laarhoven 12579866 op 11/11/2022

import pyvisa

class ArduinoVISADevice:

    # altijd eerst een init
    def __init__(self, port):
        rm = pyvisa.ResourceManager("@py")
        ports = rm.list_resources()
        print(ports)
        self.device = rm.open_resource(port, read_termination="\r\n", write_termination="\n")

    # find identification string
    def get_identification(self):
        return self.device.query("*IDN?")

    #  set OUTPUT voltage on channel 0, using ADC values (0 - 1023)
    def set_output_value(self,Value):
        return self.device.query(f"OUT:CH0 {Value}")

    # get the output value of channel 0
    def get_output_value(self):
        return self.device.query(f"meas:CH0?")

    # get the output value of a chosen channel
    def get_input_value(self,channel):
        return int(self.device.query(f"MEAS:CH{channel}?"))

    # get the output voltage of a chosen channel
    def get_input_voltage(self,channel):
        return int(self.device.query(f"MEAS:CH{channel}?")) * (3.3/1023)

    def turn_off_device(self):
        return self.device.query(f"OUT:CH0 {0}")

def list_devices():
    rm = pyvisa.ResourceManager("@py")
    ports = rm.list_resources()
    return ports





