# Code from phidget web page ----------------------------------------------------
# https://www.phidgets.com/?prodid=1270#Tab_Code_Samples
# https://www.phidgets.com/docs/Calibrating_Load_Cells
# https://www.phidgets.com/docs/KIT4007_User_Guide

# Load dependecies --------------------------------------------------------------
from Phidget22.Phidget import *
from Phidget22.Devices.Log import *
from Phidget22.LogLevel import *
from Phidget22.Devices.VoltageRatioInput import *
import time
import os

## Call function from getSerialNumber
from getSerialNumber import *


# Set global values for linear calibration --------------------------------------
calibrated = False
m = 0
b = 0


# Method for reading the voltage ------------------------------------------------
def onVoltageRatioChange_2(self, voltageRatio):
	if calibrated:
		# Calculate calibrated weight with y = mx + b
		# sys.stdout.write("\rWeight: " + str(round((m*voltageRatio)+b,2)) + "g      ")

		# Apply the calibration parameters (gain, offset) to the raw voltage
		# ratio
		with open(f'../{serial_number}_data/{serial_number}_channel_2_data.txt', 'a') as file:
			file.write(f'{time.strftime("%D %H:%M:%S")}, {round((m * voltageRatio) + b, 3)}\n')


# Create folder to store data ---------------------------------------------------
serial_number = getSerialNumber()

if not os.path.exists(f'../{serial_number}_data'):
	os.mkdir(f'../{serial_number}_data')

	print(f'Directory {serial_number}_data created')

else:
	print(f'Directory ../{serial_number}_data already exists.')

## Create folder to store logs --------------------------------------------------
if not os.path.exists(f'../{serial_number}_data/{serial_number}_logs'):
	os.mkdir(f'../{serial_number}_data/{serial_number}_logs')

else:
	print(f'Directory for storing logs already exists.')

# Create txt file for storing data from channel 2 -------------------------------
with open(f'../{serial_number}_data/{serial_number}_channel_2_data.txt', 'w') as file:
	file.write('date_time, weight_grams\n')


# Main method -------------------------------------------------------------------
def balance_2_main():
	global calibrated
	global m
	global b

	# 0) Log errors and warningss
	Log.enable(
		LogLevel.PHIDGET_LOG_INFO, f'../{serial_number}_data/{serial_number}_logs/phidgetlog_2.log'
	)

	# 1) Create your Phidget channels
	voltageRatioInput2 = VoltageRatioInput()

	# 2) Set addressing parameters to specify which channel to open (if any)
	voltageRatioInput2.setDeviceSerialNumber(serial_number)
	voltageRatioInput2.setChannel(2)

	# 3) Assign any event handlers you need before calling open so that no
	# events are missed.
	voltageRatioInput2.setOnVoltageRatioChangeHandler(onVoltageRatioChange_2)

	# 4) Open your Phidgets and wait 5 seconds for attachment
	voltageRatioInput2.openWaitForAttachment(5000)

	# Set data collection interval to 1s
	voltageRatioInput2.setDataInterval(1000)

	try:
		input('Clear any weight over the scale connected to the channel 2 and then press Enter\n')
	except (Exception, KeyboardInterrupt):
		pass

	v1 = voltageRatioInput2.getVoltageRatio()

	#
	try:
		w2 = input(
			'Place a known weight in grams on the scale connected to the channel 2, type the weight in grams, and then press Enter:\n'
		)
	except (Exception, KeyboardInterrupt):
		pass

	# Linear calibration --------------------------------------------------------
	v2 = voltageRatioInput2.getVoltageRatio()

	# Calculate slope 'm'
	m = (float(w2) - 0) / (v2 - v1)

	# solve for b using zero point : b = y-mx
	b = 0 - (m * v1)

	# Print message
	print('Calibration Complete: y = ' + str(m) + 'x + ' + str(b))
	calibrated = True
	try:
		input('Press Enter to Stop the scale connected to the channel 2s\n')
	except (Exception, KeyboardInterrupt):
		pass

	# 5) Close your Phidgets once the program is done.
	voltageRatioInput2.close()


# Run main as a script ----------------------------------------------------------
if __name__ == '__main__':
	balance_2_main()
