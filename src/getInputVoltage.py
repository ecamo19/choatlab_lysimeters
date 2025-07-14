# Code from phidget web page ----------------------------------------------------
# https://www.phidgets.com/?prodid=1270#Tab_Code_Samples

# Load dependecies --------------------------------------------------------------
from Phidget22.Phidget import *
from Phidget22.Devices.Log import *
from Phidget22.LogLevel import *
from Phidget22.Devices.VoltageRatioInput import *
import time
import os

# Methods -----------------------------------------------------------------------
# Declare any event handlers here. These will be called every time the associated 
# event occurs.

## Get Phidget device serial number ---------------------------------------------
def getSerialNumber():
	bridge_input = VoltageRatioInput()
	try:
		# Open the device (this will connect to the first available bridge input)
		bridge_input.openWaitForAttachment(5000)  # Wait up to 5 seconds for attachment
		# Wait up to 5 seconds for attachment
		bridge_input.openWaitForAttachment(5000)  

		# Get the serial number
		serial_number =  bridge_input.getDeviceSerialNumber()

	except PhidgetException as e:
		print(f"Phidget Exception: {e.details}")

	finally:
		# Always close the device when done
		bridge_input.close()

	return serial_number

serial_number = getSerialNumber()

## Channel 0 methods ------------------------------------------------------------

### Append data from channel 0 to file ------------------------------------------     
def onVoltageRatioInput0_VoltageRatioChange(self,voltageRatio): 

    # Append data
    with open(f'../{serial_number}_data/{serial_number}_channel_0_data.txt', 'a') as file:
    	file.write(f"{time.strftime('%D %H:%M:%S')}, {voltageRatio}\n")

### Handle errors ---------------------------------------------------------------
def onVoltageRatioInput0_Error(self, code, description):
	print("Code [0]: " + ErrorEventCode.getName(code))
	print("Description [0]: " + str(description))
	print("----------")

## Channel 1 methods ------------------------------------------------------------
def onVoltageRatioInput1_VoltageRatioChange(self, voltageRatio):

 	# Append data
    with open(f'../{serial_number}_data/{serial_number}_channel_1_data.txt', 'a') as file:
    	file.write(f"{time.strftime('%D %H:%M:%S')}, {voltageRatio}\n")

### Handle errors ---------------------------------------------------------------
def onVoltageRatioInput1_Error(self, code, description):
	print("Code [1]: " + ErrorEventCode.getName(code))
	print("Description [1]: " + str(description))
	print("----------")

## Channel 2 methods ------------------------------------------------------------
def onVoltageRatioInput2_VoltageRatioChange(self, voltageRatio):
	pass
 	#print("VoltageRatio [2]: " + str(voltageRatio))

### Handle errors ---------------------------------------------------------------
def onVoltageRatioInput2_Error(self, code, description):
	print("Code [2]: " + ErrorEventCode.getName(code))
	print("Description [2]: " + str(description))
	print("----------")

## Channel 3 methods ------------------------------------------------------------
def onVoltageRatioInput3_VoltageRatioChange(self, voltageRatio):
	pass

### Handle errors ---------------------------------------------------------------
def onVoltageRatioInput3_Error(self, code, description):
	print("Code [3]: " + ErrorEventCode.getName(code))
	print("Description [3]: " + str(description))
	print("----------")

