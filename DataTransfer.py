import serial 
# more libarys W

sir = serial.Serial('/dev/ttyACM0', 9600)
file = open("DATA_TRANSFER.txt", "a")

while True:
	try:
		line = sir.readline().decode('utf-8').strip()
		# reads line from arudio communcation and does stuff to make it useable 
		print("DATA CAPTURED: ", line)
		file.write(line + "\n")
	except KeyboardInterrupt:
		print("DATA EXPUNGED")
		# W larp and also visual indicator
		file.close()
		break
