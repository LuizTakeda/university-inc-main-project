from modules.voice import Voice
from modules.listener import *
from modules.device import Device

# --- Exemplo de Uso ---
if __name__ == "__main__":
  voice = Voice()
  device = Device()

  device.connect()

  device.send_command("ligar", "luz")

  response = device.send_command_with_response("ligar", "luz")

  print(f"Response {response}")

  device.disconnect()

  try:
    while True:
      if listen_call():
        voice.say_listenning()

        command = listen_command()

        if command is None:
          voice.say_dont_understand()

  except KeyboardInterrupt:
    print("\nGoodbye!")