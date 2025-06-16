import speech_recognition as sr

def analyze_command(sentence: str):
    """
    Analyzes a spoken sentence to extract the intended action and target.

    This function performs basic keyword matching to determine the user's intent,
    converting phrases such as "ligar luz" or "qual é a temperatura" into
    machine-friendly commands like ("on", "light") or ("get", "temperature").

    Args:
        sentence (str): The spoken sentence to analyze.

    Returns:
        tuple: A tuple (action, target) where:
            - action (str or None): One of "on", "off", "get" if detected.
            - target (str or None): One of "light", "temperature", or "humidity" if detected.
            Returns (None, None) if no recognizable action or target is found.
    """
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
    """
    Listens for a specific wake word (e.g., a name like "rose").

    Uses the microphone to capture a short audio snippet and checks if the
    recognized speech matches the given name.

    Args:
        name (str): The wake word to listen for (default is "rose").

    Returns:
        bool: True if the recognized word matches the wake word, False otherwise.
    """
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening...")
        try:
            audio = recognizer.listen(source, phrase_time_limit=10)
            text = recognizer.recognize_google(audio, language="pt-BR")
            print(f"You said: {text}")

            return text.lower().find(name.lower())

        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print(f"Error communicating with the recognition service: {e}")
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for speech.")

    return False


def listen_command():
    """
    Listens for a full spoken command and interprets it.

    Uses the microphone to capture a spoken sentence and attempts to convert
    it into an (action, target) tuple using the `analyze_command()` function.

    Returns:
        tuple or None:
            A tuple (action, target) if a valid command is recognized.
            Returns None if speech could not be understood or an error occurs.
    """
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

    return (None, None)
