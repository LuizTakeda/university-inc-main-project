import os
import threading
import time
import errno
from gtts import gTTS
import pygame

class Voice:
    """
    Handles speech synthesis and audio playback using gTTS and pygame.

    This class is designed to:
    - Generate predefined or custom audio responses.
    - Automatically generate audio files if they are not already available.

    Typical usage:
        voice = Voice()
        voice.say_listenning()
        voice.say("Custom message here")
    """

    def __init__(self, lang="pt-br"):
        """
        Initializes the Voice system.

        Args:
            lang (str): Language code for speech synthesis (default is 'pt-br').
        """
        self.BASE_AUDIO_DIR = os.path.join(os.path.dirname(__file__), "audio")
        self.LANG = lang
        os.makedirs(self.BASE_AUDIO_DIR, exist_ok=True)
        pygame.mixer.init()

        # Mapping of predefined speech keys to (text, filename)
        self._audio_files = {
            "listenning": ("Estou ouvindo", "listenning.mp3"),
            "dont_understand": ("Não entendi", "dont_understand.mp3"),
            "done": ("Feito", "done.mp3"),
            "temperature": ("A temperatura atual é de", "temperature.mp3"),
            "humidity": ("A umidade atual é de", "humidity.mp3"),
            "fail": ("Falha ao executar ação", "fail.mp3"),
        }

        self._generate_audios()

    def _generate_audios(self):
        """
        Generates and saves audio files for predefined text if they do not already exist.
        """
        for _, (text, file_name) in self._audio_files.items():
            path = os.path.join(self.BASE_AUDIO_DIR, file_name)

            if not os.path.exists(path):
                print(f"Generate audio: {text}")
                gTTS(text=text, lang=self.LANG).save(path)

    def _play(self, key):
        """
        Plays a predefined audio file synchronously.

        Args:
            key (str): Key for the predefined audio (must exist in self._audio_files).
        """
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

    def _play_async(self, key):
        """
        Plays a predefined audio file asynchronously in a separate thread.

        Args:
            key (str): Key for the predefined audio.
        """
        thread = threading.Thread(target=self._play, args=(key,))
        thread.start()

    def say_listenning(self):
        """Plays the 'listening' predefined message asynchronously."""
        self._play_async("listenning")

    def say_dont_understand(self):
        """Plays the 'don't understand' predefined message asynchronously."""
        self._play_async("dont_understand")

    def say_done(self):
        """Plays the 'done' predefined message asynchronously."""
        self._play_async("done")

    def say_temperature(self):
        """Plays the 'temperature' predefined message asynchronously."""
        self._play_async("temperature")

    def say_humidity(self):
        """Plays the 'humidity' predefined message asynchronously."""
        self._play_async("humidity")

    def say_fail(self):
        """Plays the 'fail' predefined message asynchronously."""
        self._play_async("fail")

    def _say_text(self, text):
        """
        Generates and plays custom audio text synchronously.

        Args:
            text (str): The message to be converted to speech and played.
        """
        file_name = "temp.mp3"
        path = os.path.join(self.BASE_AUDIO_DIR, file_name)

        # Attempt to delete old temp file
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
                    print(f"Error deleting '{path}': {e}")
                    break

        # Generate new audio
        try:
            print(f"Generate audio: {text}")
            gTTS(text=text, lang=self.LANG).save(path)
        except Exception as e:
            print(f"Error saving audio: {e}")
            return

        # Play audio
        try:
            print(f"Playing: {file_name} {text}")
            pygame.mixer.music.load(path)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

        except Exception as e:
            print(f"Error playing audio: {e}")

    def say(self, text):
        """
        Generates and plays custom audio text asynchronously in a new thread.

        Args:
            text (str): The message to be converted to speech and played.
        """
        thread = threading.Thread(target=self._say_text, args=(text,))
        thread.start()
