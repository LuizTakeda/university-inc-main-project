import asyncio
import websockets
import speech_recognition as sr


# Função para reconhecer comandos de voz
def reconhecer_comando():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Ajustando para ruído ambiente...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("Ouvindo...")
        try:
            audio = recognizer.listen(source, phrase_time_limit=10)
            texto = recognizer.recognize_google(audio, language="pt-BR")
            print(f"Você disse: {texto}")
            return texto.lower()
        except sr.UnknownValueError:
            print("Não entendi o que foi dito.")
        except sr.RequestError as e:
            print(f"Erro ao se comunicar com o serviço de reconhecimento: {e}")
        except sr.WaitTimeoutError:
            print("Tempo esgotado aguardando fala.")

    return None


# Função principal com loop e envio por WebSocket
async def loop_voz_websocket(uri):
    async with websockets.connect(uri) as websocket:
        print("Conectado ao servidor WebSocket.")
        while True:
            texto = reconhecer_comando()
            if texto and "rose" in texto:
                comandos = [
                    "ligar luz",
                    "apagar luz",
                    "abrir porta",
                    "fechar porta",
                ]
                for kw in comandos:
                    if kw in texto:
                        print(f"Comando reconhecido: {kw}")
                        await websocket.send(kw)
                        break
                else:
                    print("Comando inválido ou não reconhecido.")
            await asyncio.sleep(2)


# Executa o loop
if __name__ == "__main__":
    try:
        asyncio.run(loop_voz_websocket("ws://localhost:8765"))
    except KeyboardInterrupt:
        print("\nEncerrando...")
