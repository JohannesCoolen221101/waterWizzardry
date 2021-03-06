from network import WLAN
import urequests as requests
import machine
import pycom
import time

wlan = WLAN(mode=WLAN.STA)

def set_connect():
    teller = 0

    #wlan.connect(ssid='IoT', auth=(WLAN.WPA2, 'KdGIoT92!'))
    wlan.connect(ssid='telenet-2201056', auth=(WLAN.WPA2, '4XpNpfyjhuh3'))
    while not wlan.isconnected():
        machine.idle()
        teller = teller+1

        if teller==10:
            print("nowifi")
            break



def send(info):
    if not wlan.isconnected():
        set_connect()
    aio_key = "aio_hAbO53exUEWrujXobH9FN2gaqKZi"
    username = "joske"
    feed_name = "peter"

# Create an instance of the REST client
    url = 'https://io.adafruit.com/api/v2/' + username + '/feeds/' + feed_name + '/data'
    body = {'value': info}
    headers = {'X-AIO-Key': aio_key, 'Content-Type': 'application/json'}
    try:
        r = requests.post(url, json=body, headers=headers)
        r.close()

    except Exception as e:
        print(e)
