# osc/send_gestures.py
from pythonosc.udp_client import SimpleUDPClient

ip = "127.0.0.1"
port = 5005
client = SimpleUDPClient(ip, port)

def send_gesture(gesture_name):
    client.send_message("/gesture", gesture_name)
