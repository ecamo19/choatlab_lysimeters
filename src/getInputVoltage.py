# Code from phidget web page ----------------------------------------------------
# https://www.phidgets.com/?prodid=1270#Tab_Code_Samples
# https://www.phidgets.com/docs/Calibrating_Load_Cells

# Load dependecies --------------------------------------------------------------
from Phidget22.Phidget import *
from Phidget22.Devices.Log import *
from Phidget22.LogLevel import *
from Phidget22.Devices.VoltageRatioInput import *
import time

# Phidget values ----------------------------------------------------------------

# Insert your gain value from the Phidget Control Panel
gain = 0

# The offset is calculated in tareScale
offset = 0

calibrated = False

# Methods -----------------------------------------------------------------------

## Tare scale -------------------------------------------------------------------
def tareScale(ch):    
    global calibrated
    num_samples = 16
    
    offset_name = f'offset_{ch}'
    print(f'Taring {offset_name}')
    
     # Initialize the global variable
    globals()[offset_name] = 0 
    
    for i in range(num_samples):
        globals()[offset_name] += ch.getVoltageRatio()
        time.sleep(ch.getDataInterval()/1000.0)
        
    globals()[offset_name] /= num_samples
    calibrated = True
 
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
def onVoltageRatioChange_0(self, voltageRatio):
    
    if(calibrated):
        
        # Apply the calibration parameters (gain, offset) to the raw voltage 
        # ratio
        weight_0 = (voltageRatio - offset_0) * gain
        with open(f'../{serial_number}_data/{serial_number}_channel_0_data.txt', 'a') as file:
            file.write(f"{time.strftime('%D %H:%M:%S')}, {weight_0}\n")

### Handle errors ---------------------------------------------------------------
def onVoltageRatioInput0_Error(self, code, description):
	print("Code [0]: " + ErrorEventCode.getName(code))
	print("Description [0]: " + str(description))
	print("----------\n")

## Channel 1 methods ------------------------------------------------------------
def onVoltageRatioChange_1(self, voltageRatio):
    if(calibrated):
        
        # Apply the calibration parameters (gain, offset) to the raw voltage 
        # ratio
        weight_1 = (voltageRatio - offset_1) * gain
        with open(f'../{serial_number}_data/{serial_number}_channel_1_data.txt', 'a') as file:
            file.write(f"{time.strftime('%D %H:%M:%S')}, {weight_1}\n")

### Handle errors ---------------------------------------------------------------
def onVoltageRatioInput1_Error(self, code, description):
	print("Code [1]: " + ErrorEventCode.getName(code))
	print("Description [1]: " + str(description))
	print("----------\n")

## Channel 2 methods ------------------------------------------------------------
def onVoltageRatioChange_2(self, voltageRatio):
    if(calibrated):
        
        # Apply the calibration parameters (gain, offset) to the raw voltage 
        # ratio
        weight_2 = (voltageRatio - offset_2) * gain
        
        # Append data
        with open(f'../{serial_number}_data/{serial_number}_channel_2_data.txt', 'a') as file:
            file.write(f"{time.strftime('%D %H:%M:%S')}, {weight_2}\n")

### Handle errors ---------------------------------------------------------------
def onVoltageRatioInput2_Error(self, code, description):
	print("Code [2]: " + ErrorEventCode.getName(code))
	print("Description [2]: " + str(description))
	print("----------\n")

## Channel 3 methods ------------------------------------------------------------
def onVoltageRatioChange_3(self, voltageRatio):
		if(calibrated):
		
		    # Apply the calibration parameters (gain, offset) to the raw voltage 
      		# ratio
		    weight_3 = (voltageRatio - offset_3) * gain
		
		    # Append data
		    with open(f'../{serial_number}_data/{serial_number}_channel_3_data.txt', 'a') as file:
		        file.write(f"{time.strftime('%D %H:%M:%S')}, {weight_3}\n")

### Handle errors ---------------------------------------------------------------
def onVoltageRatioInput3_Error(self, code, description):
	print("Code [3]: " + ErrorEventCode.getName(code))
	print("Description [3]: " + str(description))
	print("----------\n")