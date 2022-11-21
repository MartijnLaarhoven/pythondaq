# Gemaakt door Martijn Laarhoven 12579866 op 11/11/2022

import pyvisa

class ArduinoVISADevice:
    """The class ArduinoVISADevice which gets and sets the values of the experiment
    """

    def __init__(self, port):
        """The initial module 

        Args:
            port (string): The port which is given when running the module
        """
        rm = pyvisa.ResourceManager("@py")
        ports = rm.list_resources()
        self.device = rm.open_resource(port, read_termination="\r\n", write_termination="\n")

    def get_identification(self):
        """Identifying the device

        Returns:
            string: The device
        """
        return self.device.query("*IDN?")

    #  set OUTPUT voltage on channel 0, using ADC values (0 - 1023)
    def set_output_value(self,Value):
        """_summary_

        Args:
            Value (_type_): _description_

        Returns:
            _type_: _description_
        """
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
    """_summary_

    Returns:
        Tuple: A list of strings
    """
    rm = pyvisa.ResourceManager("@py")
    ports = rm.list_resources()
    return ports

