import socket
import fcntl
import struct
import time
import threading
from gps import *

def get_lan_ip(interface):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack('256s', interface[:15])
        )[20:24])
    except:
        return "0.0.0.0" # default

def get_mac_address(interface):
    try:
        str = open('/sys/class/net/' + interface + '/address').read()
    except:
        str = "00:00:00:00:00:00" # default

    return str[:17]


# Threat that will poll the latest GPS info from the serial
class GpsPoller(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.gps_instance = gps(mode=WATCH_ENABLE)
		self.running = True

	def run(self):
		try:
			while self.running:
				self.gps_instance.next()
				time.sleep(0.2)
		except StopIteration:
			pass