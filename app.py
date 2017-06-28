import httplib
import urllib
import urllib2
from helpers import *

gps_poller = GpsPoller()
try:
    gps_poller.start()

    while True:
        gps = gps_poller.gps_instance

        interface = "wlan0"

        data = {
            'lan_ip': get_lan_ip(interface),
            'mac_address': get_mac_address(interface),
            'gps_latitude': gps.fix.latitude,
            'gps_longitude': gps.fix.longitude
        }

        try:
            # Send data to API
            reader = urllib2.urlopen("http://project.maarten.co.uk/test", urllib.urlencode(data))
            print reader.read()
            reader.close()
        except urllib2.HTTPError, e:
            print 'HTTPError = ' + str(e.code)
        except urllib2.URLError, e:
            print 'URLError = ' + str(e.reason)
        except httplib.HTTPException, e:
            print 'HTTPException'
        except Exception:
            import traceback

            print 'generic exception: ' + traceback.format_exc()
        finally:
            time.sleep(5)

except(KeyboardInterrupt, SystemExit):
    print "\nKilling Thread.."
    gps_poller.running = False
    gps_poller.join()
    print "Done.\nExiting."