import asyncio
import websockets


# Agora só com o argumento websocket
async def servidor(websocket):
    print("Cliente conectado.")
    try:
        async for mensagem in websocket:
            print(f"Comando recebido: {mensagem}")
    except websockets.exceptions.ConnectionClosed:
        print("Cliente desconectado.")


async def main():
    print("Iniciando servidor WebSocket em ws://localhost:8765...")
    async with websockets.serve(servidor, "localhost", 8765):
        await asyncio.Future()  # Mantém o servidor rodando


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nServidor encerrado.")
