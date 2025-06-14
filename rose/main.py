from modules.voice import Voice
from modules.listener import *
from modules.device import Device

# --- Exemplo de Uso ---
if __name__ == "__main__":
  voice = Voice()
  device = Device()

  device.connect()

  try:
    while True:
      if listen_call():
        voice.say_listenning()

        action, target = listen_command()

        if action is None or target is None:
          voice.say_dont_understand()
          continue
      
        if  action != "get" and not device.send_command(target, action):
          voice.say_fail()
          continue

        if action == "get":

          response = device.send_command_with_response(target, action)

          if response is None:
            voice.say_fail()  
            continue

          voice.say(f"Atualmente é de {response}")
          continue

        voice.say_done();



  except KeyboardInterrupt:
    device.disconnect()
    print("\nGoodbye!")