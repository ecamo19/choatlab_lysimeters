# Code from phidget web page ----------------------------------------------------
# https://www.phidgets.com/?prodid=1270#Tab_Code_Samples
# https://www.phidgets.com/docs/Calibrating_Load_Cells

# Load dependecies --------------------------------------------------------------
from Phidget22.Phidget import *
from Phidget22.Devices.Log import *
from Phidget22.LogLevel import *
from Phidget22.Devices.VoltageRatioInput import *
import time


## Get Phidget device serial number ---------------------------------------------
def getSerialNumber():
	bridge_input = VoltageRatioInput()
	try:
		# Open the device (this will connect to the first available bridge input)
		# Wait up to 5 seconds for attachment
		bridge_input.openWaitForAttachment(5000)

		# Get the serial number
		serial_number = bridge_input.getDeviceSerialNumber()

	except PhidgetException as e:
		print(f'Phidget Exception: {e.details}')

	finally:
		# Always close the device when done
		bridge_input.close()

	return serial_number

