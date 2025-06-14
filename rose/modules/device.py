import serial
import serial.tools.list_ports
import time

class Device:
    """
    Represents a connection handler for an ESP device over a serial port.

    This class provides methods to:
    - Automatically detect the serial port of an ESP device based on common USB-to-Serial chip identifiers.
    - Establish and manage a serial connection to the ESP.
    - Send text-based commands to the ESP.
    - Disconnect safely when done.

    Typical usage:
        device = Device()
        device.connect()
        device.send_command("Hello ESP")
        device.disconnect()
    """
    def __init__(self):
      """
      Initializes the Device instance with no active ESP connection.
      """
      self.esp = None      # Serial connection to the ESP device
      self.port = None     # Port where the ESP device is connected

    def _find_esp_port(self):
      """
      Scans available serial ports and tries to identify one that matches
      common ESP USB-to-Serial chip identifiers (like CP210x, CH340, etc.).

      Returns:
          The device port string (e.g., 'COM3' or '/dev/ttyUSB0') if found, else None.
      """
      ports = serial.tools.list_ports.comports()

      for port in ports:
        if "USB" in port.description or "UART" in port.description or "CP210" in port.description or "CH340" in port.description:
          self.port = port.device
          print(f"Device found on {self.port}")
          return self.port

      print("Device not found")
      return None

    def connect(self):
      """
      Attempts to connect to the ESP device on the identified serial port.
      Sets up the serial connection with a baud rate of 115200.

      If successful, stores the connection in self.esp.
      """
      port = self._find_esp_port()

      if not port:
        print("No ESP device found.")
        return

      try:
        self.esp = serial.Serial(port, 115200, timeout=1)
        self.esp.setDTR(False)
        self.esp.setRTS(False)
        time.sleep(1)           # Allow time for the ESP to remain stable
        print("Success connecting")
      except Exception as e:
        print(f"Error connecting: {e}")
        self.esp = None

    def disconnect(self):
      """
      Closes the serial connection to the ESP if it is currently open.
      """
      if self.esp and self.esp.is_open:
        self.esp.close()
        print("Disconnected from device")
        self.esp = None
      else:
        print("No connection to disconnect")

    def send_command(self, target, action):
      """
      Sends a command string to the ESP device over the serial connection.

      Args:
          command (str): The text to send to the ESP.
      """
      if self.esp and self.esp.is_open:
        self.esp.reset_input_buffer();

        self.esp.write((f"{target}:{action}\n").encode())
        print(f"Command sent: {target}:{action}")

        response = self.esp.read_until()
        print(f"Response: {response.decode().strip()}")
        if response.decode().strip() == "OK":
          return True

      else:
        print("Device is not connected")
        
      return False
    
    def send_command_with_response(self, target, action):
        """
        Sends a command string to the ESP device over the serial connection.

        Args:
            command (str): The text to send to the ESP.
        """
        if self.esp and self.esp.is_open:
            self.esp.reset_input_buffer();
            
            self.esp.write((f"{target}:{action}\n").encode())
            print(f"Command sent: {target}:{action}")

            response = self.esp.read_until()
            print(f"Response: {response.decode().strip()}")
            return response.decode().strip()
            
        else:
            print("Device is not connected")
        
        return None