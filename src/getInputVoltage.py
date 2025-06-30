# Code from phidget web page ----------------------------------------------------
# https://www.phidgets.com/?prodid=1270#Tab_Code_Samples

# Load dependecies --------------------------------------------------------------
from Phidget22.Phidget import *
from Phidget22.Devices.Log import *
from Phidget22.LogLevel import *
from Phidget22.Devices.VoltageRatioInput import *
import time
import os

# Close any existing connections before running the code ------------------------
# Try all 4 channels
for each_channel in range(4):  
    try:
        channel = VoltageRatioInput()
        channel.setChannel(each_channel)
        channel.open()
        channel.close()
    except:
        pass

print("Cleanup complete")

# Methods -----------------------------------------------------------------------
# Declare any event handlers here. These will be called every time the associated 
# event occurs.

## Create folder to store data --------------------------------------------------
if not os.path.exists("../data"):
    os.mkdir("../data")
else:
    print("Directory already exists.")

## Channel 0 methods ------------------------------------------------------------

### Create file -----------------------------------------------------------------
with open("../data/channel_0_data.txt", "w") as file:
    	file.write("date_time, voltage\n")

### Append data from channel 0 to file ------------------------------------------     
def onVoltageRatioInput0_VoltageRatioChange(self, voltageRatio): 
    
    # Append data
    with open('../data/channel_0_data.txt', 'a') as file:
    	file.write(f"{time.strftime('%D %H:%M:%S')}, {voltageRatio}\n")

def onVoltageRatioInput0_Error(self, code, description):
	print("Code [0]: " + ErrorEventCode.getName(code))
	print("Description [0]: " + str(description))
	print("----------")

## Channel 1 methods ------------------------------------------------------------

def onVoltageRatioInput1_VoltageRatioChange(self, voltageRatio):
	pass
 	#print("VoltageRatio [1]: " + str(voltageRatio))

def onVoltageRatioInput1_Error(self, code, description):
	print("Code [1]: " + ErrorEventCode.getName(code))
	print("Description [1]: " + str(description))
	print("----------")

## Channel 2 methods ------------------------------------------------------------

def onVoltageRatioInput2_VoltageRatioChange(self, voltageRatio):
	pass
 	#print("VoltageRatio [2]: " + str(voltageRatio))

def onVoltageRatioInput2_Error(self, code, description):
	print("Code [2]: " + ErrorEventCode.getName(code))
	print("Description [2]: " + str(description))
	print("----------")

## Channel 2 methods ------------------------------------------------------------

def onVoltageRatioInput3_VoltageRatioChange(self, voltageRatio):
	pass

def onVoltageRatioInput3_Error(self, code, description):
	print("Code [3]: " + ErrorEventCode.getName(code))
	print("Description [3]: " + str(description))
	print("----------")

# Main method -------------------------------------------------------------------
def main():
	try:
        # Log errors and warnings
		Log.enable(LogLevel.PHIDGET_LOG_INFO, "phidgetlog.log")
  
		# 1) Create your Phidget channels
		voltageRatioInput0 = VoltageRatioInput()
		voltageRatioInput1 = VoltageRatioInput()
		voltageRatioInput2 = VoltageRatioInput()
		voltageRatioInput3 = VoltageRatioInput()

		# 2) Set addressing parameters to specify which channel to open (if any)
		voltageRatioInput0.setDeviceSerialNumber(716364)
		voltageRatioInput0.setChannel(0)
  
		voltageRatioInput1.setDeviceSerialNumber(716364)
		voltageRatioInput1.setChannel(1)
  
		voltageRatioInput2.setDeviceSerialNumber(716364)
		voltageRatioInput2.setChannel(2)
  
		voltageRatioInput3.setDeviceSerialNumber(716364)
		voltageRatioInput3.setChannel(3)

		# 3) Assign any event handlers you need before calling open so that no events are missed.
		voltageRatioInput0.setOnVoltageRatioChangeHandler(onVoltageRatioInput0_VoltageRatioChange)
		voltageRatioInput0.setOnErrorHandler(onVoltageRatioInput0_Error)
  
		voltageRatioInput1.setOnVoltageRatioChangeHandler(onVoltageRatioInput1_VoltageRatioChange)
		voltageRatioInput1.setOnErrorHandler(onVoltageRatioInput1_Error)
  
		voltageRatioInput2.setOnVoltageRatioChangeHandler(onVoltageRatioInput2_VoltageRatioChange)
		voltageRatioInput2.setOnErrorHandler(onVoltageRatioInput2_Error)
  
		voltageRatioInput3.setOnVoltageRatioChangeHandler(onVoltageRatioInput3_VoltageRatioChange)
		voltageRatioInput3.setOnErrorHandler(onVoltageRatioInput3_Error)

		# Open your Phidgets and wait for attachment
		voltageRatioInput0.openWaitForAttachment(5000)
		voltageRatioInput1.openWaitForAttachment(5000)
		voltageRatioInput2.openWaitForAttachment(5000)
		voltageRatioInput3.openWaitForAttachment(5000)

		#Interact with your Phidgets here or in your event handlers.

		try:
			input("Press Enter to Stop\n")
		except (Exception, KeyboardInterrupt):
			pass

		#Close your Phidgets once the program is done.
		voltageRatioInput0.close()
		voltageRatioInput1.close()
		voltageRatioInput2.close()
		voltageRatioInput3.close()

	except PhidgetException as ex:
		#We will catch Phidget Exceptions here, and print the error informaiton.
		traceback.print_exc()
		print("")
		print("PhidgetException " + str(ex.code) + " (" + ex.description + "): " + ex.details)


main()