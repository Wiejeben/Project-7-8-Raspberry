import threading
import urllib
import urllib2
from helpers import *

gps_poller = GpsPoller()

def app():
    threading.Timer(10.0, app).start()
    global gps_poller
    gps = gps_poller.gps_instance

    interface = "wlan0"

    data = {
        'lan_ip': get_lan_ip(interface),
        'mac_address': get_mac_address(interface),
        'gps_latitude': gps.fix.latitude,
        'gps_longitude': gps.fix.longitude
    }

    # Send data to API
    reader = urllib2.urlopen("http://project.maarten.co.uk/test", urllib.urlencode(data))

    print reader.read()

    reader.close()

gps_poller.start()
app()