#!/usr/bin/python
import socket
import sys
import requests
import time
import syslog
from xml.etree import ElementTree as ET

DOMOTICZ_IP = 'x.x.x.x'
DOMOTICZ_PORT = '8080'

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('0.0.0.0', 22600)
sock.bind(server_address)
while True:
    data, address = sock.recvfrom(4096)
    
    if data:
        sent = sock.sendto(data, address)
	Current_L1 = (ET.fromstring(data).find(".//curr/..[@id='0']"))[0].text
	Current_L2 = (ET.fromstring(data).find(".//curr/..[@id='1']"))[0].text
	Current_L3 = (ET.fromstring(data).find(".//curr/..[@id='2']"))[0].text
	Battery = ET.fromstring(data).find('battery').attrib['level'].replace("%","")
	url = 'http://%s:%s/json.htm?type=command&param=udevice&idx=19&nvalue=0&svalue=%s;%s;%s&battery=%s' % (DOMOTICZ_IP, DOMOTICZ_PORT, Current_L1, Current_L2, Current_L3, Battery)
	try:
		r = requests.get(url)
		if r.status_code == 200:
			time.sleep(60)
	except:
		syslog.syslog('%s: Failed to push data. Retrying in 30sec...' % sys.argv[0])
		time.sleep(30)
		pass
