# Load dependecies --------------------------------------------------------------
from Phidget22.Phidget import *
from Phidget22.Devices.Log import *
from Phidget22.LogLevel import *
from Phidget22.Devices.VoltageRatioInput import *
import time
import os

## Call functions from getInputVoltage
from getInputVoltage import *

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

# Create folder to store data --------------------------------------------------
serial_number = getSerialNumber()

if not os.path.exists(f"../{serial_number}_data"):
    os.mkdir(f"../{serial_number}_data")
else:
    print(f"Directory ../{serial_number}_data already exists.")


## Create files to store data ---------------------------------------------------
for each_file in range(4):
	with open(f"../{serial_number}_data/{serial_number}_channel_{each_file}_data.txt", "w") as file:
    		file.write("date_time, voltage\n")

# Main method -------------------------------------------------------------------
def main():
	try:
        # 0) Log errors and warnings
		Log.enable(LogLevel.PHIDGET_LOG_INFO, "phidgetlog.log")

		# 1) Create your Phidget channels
		voltageRatioInput0 = VoltageRatioInput()
		voltageRatioInput1 = VoltageRatioInput()
		voltageRatioInput2 = VoltageRatioInput()
		voltageRatioInput3 = VoltageRatioInput()

		# 2) Set addressing parameters to specify which channel to open (if any)
		voltageRatioInput0.setDeviceSerialNumber(serial_number)
		voltageRatioInput0.setChannel(0)

		voltageRatioInput1.setDeviceSerialNumber(serial_number)
		voltageRatioInput1.setChannel(1)

		voltageRatioInput2.setDeviceSerialNumber(serial_number)
		voltageRatioInput2.setChannel(2)

		voltageRatioInput3.setDeviceSerialNumber(serial_number)
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

		# 4) Open your Phidgets and wait 7 seconds for attachment
		voltageRatioInput0.openWaitForAttachment(7000)
		voltageRatioInput1.openWaitForAttachment(7000)
		voltageRatioInput2.openWaitForAttachment(7000)
		voltageRatioInput3.openWaitForAttachment(7000)

		# Interact with your Phidgets here or in your event handlers.
		try:
			input("\nPress Enter to Stop\n")
		except (Exception, KeyboardInterrupt):
			pass

		# 5) Close your Phidgets once the program is done.
		voltageRatioInput0.close()
		voltageRatioInput1.close()
		voltageRatioInput2.close()
		voltageRatioInput3.close()

	except PhidgetException as ex:
     
		# We will catch Phidget Exceptions here, and print the error informaiton.
		traceback.print_exc()
		print("")
		print("PhidgetException " + str(ex.code) + " (" + ex.description + "): " + ex.details)

# Idiom to run main as a script -------------------------------------------------
if __name__ == "__main__":
    main()
    
    