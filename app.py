import threading
import urllib
import urllib2
from helpers import *

def app():
    threading.Timer(10.0, app).start()

    interface = "wlan0"

    data = {
        'lan_ip': get_lan_ip(interface),
        'mac_address': get_mac_address(interface),
        'location': {
            'lat': 0.0,
            'long': 0.0
        }
    }

    # Send data to API
    reader = urllib2.urlopen("http://project.maarten.co.uk/test", urllib.urlencode(data))

    # print reader.read()

    reader.close()

app()