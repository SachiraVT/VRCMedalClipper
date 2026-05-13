from pythonosc import dispatcher, osc_server
from pynput.keyboard import Key, Controller

keyboard = Controller()
last_state = False

def is_on(value):
    return value is True or value == 1.0

def hotkey_handler(address, value):
    global last_state

    print(address, value)

    current = is_on(value)

    if current and not last_state:
        keyboard.press(Key.f8)

        keyboard.release(Key.f8)

    last_state = current

dispatcher = dispatcher.Dispatcher()
dispatcher.map("/avatar/parameters/ClipMedal", hotkey_handler)

server = osc_server.ThreadingOSCUDPServer(
    ("127.0.0.1", 9010),
    dispatcher
)

print("Listening...")
server.serve_forever()
