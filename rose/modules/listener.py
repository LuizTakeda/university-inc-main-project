import speech_recognition as sr

def analyze_command(sentence: str):
  if sentence is None:
    return (None, None)

  sentence = sentence.lower()

  actions = {
    "desligar": "off",
    "ligar": "on",
    "qual é": "get"
  }

  targets = {
    "luz": "light",
    "temperatura": "temperature",
    "humidade": "humidity",
    "umidade": "humidity"
  }

  action = None
  for key in actions:
    if key in sentence:
      action = actions[key]
      break

  if action is None:
    return (None, None)

  target = None
  for key in targets:
    if key in sentence:
      target = targets[key]
      break

  return (action, target)


def listen_call(name="rose"):
  recognizer = sr.Recognizer()

  with sr.Microphone() as source:
    print("Adjusting for ambient noise...")
    recognizer.adjust_for_ambient_noise(source, duration=0.5)
    print("Listening...")
    try:
      audio = recognizer.listen(source, phrase_time_limit=10)
      text = recognizer.recognize_google(audio, language="pt-BR") 
      print(f"You said: {text}")
      
      return text.lower() == name.lower()

    except sr.UnknownValueError:
      print("Could not understand audio.")

    except sr.RequestError as e:
      print(f"Error communicating with the recognition service: {e}")

    except sr.WaitTimeoutError:
      print("Listening timed out while waiting for speech.")

  return False


def listen_command():
  recognizer = sr.Recognizer()

  with sr.Microphone() as source:
    print("Adjusting for ambient noise...")
    recognizer.adjust_for_ambient_noise(source, duration=0.5)
    print("Listening...")
    try:
      audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)
      text = recognizer.recognize_google(audio, language="pt-BR") 
      print(f"You said: {text}")

      command = analyze_command(text)

      print(f"Command {command}")

      return command

    except sr.UnknownValueError:
      print("Could not understand audio.")

    except sr.RequestError as e:
      print(f"Error communicating with the recognition service: {e}")

    except sr.WaitTimeoutError:
      print("Listening timed out while waiting for speech.")

  return None
