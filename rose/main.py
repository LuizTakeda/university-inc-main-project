from modules.voice import Voice
from modules.listener import *

# --- Exemplo de Uso ---
if __name__ == "__main__":
  voice = Voice()
  
  while True:
    if listen_call():
      voice.say_listenning()
      
      command = listen_command()
      
      if command == None:
        voice.say_dont_understand()