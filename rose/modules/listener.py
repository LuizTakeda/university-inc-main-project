import speech_recognition as sr

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

      return text.lower()

    except sr.UnknownValueError:
      print("Could not understand audio.")

    except sr.RequestError as e:
      print(f"Error communicating with the recognition service: {e}")

    except sr.WaitTimeoutError:
      print("Listening timed out while waiting for speech.")

  return None