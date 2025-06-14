from gtts import gTTS
import os
import pygame
import time
import errno

class Voice:

  def __init__(self, lang="pt-br"):
    self.BASE_AUDIO_DIR = os.path.join(os.path.dirname(__file__), "audio")
    self.LANG = lang
    os.makedirs(self.BASE_AUDIO_DIR, exist_ok=True)
    pygame.mixer.init()

    self._audio_files = {
        "listenning": ("Na escuta", "listenning.mp3"),
        "dont_understand": ("Não entendi", "dont_understand.mp3"),
        "done": ("Feito", "done.mp3"),
        "temperature": ("A temperatura atual é de", "temperature.mp3"),
        "humidity": ("A umidade atual é de", "humidity.mp3"),
        "fail": ("Falha ao executar ação", "fail.mp3"),
    }

    self._generate_audios()

  def _generate_audios(self):
    for _, (text, file_name) in self._audio_files.items():
      path = os.path.join(self.BASE_AUDIO_DIR, file_name)

      if not os.path.exists(path):
        print(f"Generate audio: {text}")
        gTTS(text=text, lang=self.LANG).save(path)

  def _play(self, key):
    if key not in self._audio_files:
      print(f"Invalid key: {key}")
      return
        
    _, file_name = self._audio_files[key]
    path = os.path.join(self.BASE_AUDIO_DIR, file_name)

    print(f"Playing: {file_name}")
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
      pygame.time.Clock().tick(10)

  def say_listenning(self):
    self._play("listenning")

  def say_dont_understand(self):
    self._play("dont_understand")

  def say_done(self):
    self._play("done")

  def say_temperature(self):
    self._play("temperature")

  def say_humidity(self):
    self._play("humidity")

  def say_fail(self):
    self._play("fail")

  def say(self, text):
    file_name = "temp.mp3"
    path = os.path.join(self.BASE_AUDIO_DIR, file_name)

    if os.path.exists(path):
      for _ in range(20): 
        try:
          os.remove(path)
          break
        except PermissionError as e:
          if e.errno == errno.EACCES:
            time.sleep(0.1)
          else:
            raise
        except Exception as e:
          print(f"Erro ao tentar deletar '{path}': {e}")
          break

    try:
      print(f"Generate audio: {text}")
      gTTS(text=text, lang=self.LANG).save(path)
    except Exception as e:
      print(f"Error saving audio: {e}")
      return

    try:
      print(f"Playing: {file_name} {text}")
      pygame.mixer.music.load(path)
      pygame.mixer.music.play()

      while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    except Exception as e:
      print(f"Error playing audio: {e}")
        

if __name__ == "__main__":
  voice = Voice()

  voice.say_listenning()
  voice.say_dont_understand()
  voice.say_done()
  voice.say_temperature()
  voice.say_humidity()

  voice.say("Texto gerado")
