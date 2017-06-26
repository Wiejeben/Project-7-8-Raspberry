import threading
import urllib
import urllib2
from helpers import *

def app():
    threading.Timer(10.0, app).start()

    data = {
        'lan_ip': get_lan_ip("wlan0"),
        'location': {
            'lat': 0.0,
            'long': 0.0
        }
    }

    # Send data to API
    urllib2.urlopen("http://project.maarten.co.uk/test", urllib.urlencode(data)).close()

app()