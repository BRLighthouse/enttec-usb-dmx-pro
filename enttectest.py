import platform
import sys
import time
import EnttecUsbDmxPro

dport = -1

if len(sys.argv) < 2:
	if platform.system() == 'Linux':
		dport = '/dev/ttyUSB0'
	elif platform.system() == 'Mac':
		dport = '/dev/tty.usbserial-ENT095626'
else:
	dport = sys.argv[1]
dmx = EnttecUsbDmxPro.EnttecUsbDmxPro()
if dport == -1:
	dmx.list()
	sys.stderr.write("ERROR: No serial port for DMX detected!\n")
	sys.exit()
dmx.setPort(dport)
dmx.connect()


def pulse():
	while True:
		for i in range(0, 255, 5):
			print(i)
			dmx.sendDMX([i, i, 0, i, i])
			time.sleep(0.01)
		for i in range(255, 1, -5):
			print(i)
			dmx.sendDMX([i, i, i, 0, i])
			# time.sleep(0.01)


def get():
	while True:
		print(dmx.getRecievedFrame())
