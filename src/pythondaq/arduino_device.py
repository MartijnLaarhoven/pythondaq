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

    def set_output_value(self,Value):
        """The output value module which sets the output value

        Args:
            Value (int): The outpout value that is set on channel 0, having ADC values between 0-1023

        Returns:
            int: value between 0 and 1023
        """
        return self.device.query(f"OUT:CH0 {Value}")

    def get_output_value(self):
        """get the output channel of CH0

        Returns:
            int: output value of CH0
        """        
        return self.device.query(f"meas:CH0?")

    def get_input_value(self,channel):
        """get the input value of a chosen channel

        Args:
            channel (int): channel number

        Returns:
            int: the input value of the chosen channel
        """
        return int(self.device.query(f"MEAS:CH{channel}?"))

    def get_input_voltage(self,channel):
        """get the output value of a chosen channel

        Args:
            channel (int): channel number

        Returns:
            int: the input voltage of the chosen channel
        """
        return int(self.device.query(f"MEAS:CH{channel}?")) * (3.3/1023)

    def turn_off_device(self):
        """turning off the device afterwards

        Returns:
            varible: putting the output value of channel 0 to 0
        """
        return self.device.query(f"OUT:CH0 {0}")

def list_devices():
    """The list of the devices

    Returns:
        Tuple: A list of strings
    """
    rm = pyvisa.ResourceManager("@py")
    ports = rm.list_resources()
    return ports

