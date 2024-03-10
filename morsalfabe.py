import asyncio
import websockets
import webbrowser
morse_code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
              'Q': '--.-',
              'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
              'Z': '--..',
              '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
              '8': '---..',
              '9': '----.', '0': '-----', ' ': '/', '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
              '!': '-.-.--',
              '/': '-..-.', '(': '-.--.', ')': '-.--.-'}

correct_password = "HOOGN3RP1CNG89AYS"

def check_password(password):
    return password == correct_password

def text_to_morse(text):
    morse_list = []
    for char in text:
        if char.upper() in morse_code:
            morse_list.append(morse_code[char.upper()])
    return " ".join(morse_list)

async def handle_message(websocket, path):
    password_attempt = await websocket.recv()
    if check_password(password_attempt):
        print("Password verified.")
        await websocket.send("Password verified")
        while True:
            message = await websocket.recv()
            print("Received message:", message)
            decoded_message = text_to_morse(message)
            print(f"Morse encoded message: {decoded_message}")
            await websocket.send(decoded_message)
    else:
        print("Yanlıs Sifre")
        await websocket.send("Yanlıs Sifre / Baglantı Kapatıldı")


async def start_server():
    webbrowser.open_new_tab('morsalfabe.html')
    server = await websockets.serve(handle_message, "localhost", 8765)
    print("WebSocket server started. Listening on port 8765...")
    await server.wait_closed()
if __name__ == "__main__":
    asyncio.run(start_server())
