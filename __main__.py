print("loading eel...")
import eel
print("initializing...")
eel.init('html')
print("starting...")

@eel.expose
def print(a, b):
    print(a, b, a + b)

eel.start('index.html')
print("ended...")
