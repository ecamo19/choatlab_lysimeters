# Reference Code from phidget web page ------------------------------------------
# https://www.phidgets.com/?prodid=1270#Tab_Code_Samples
# https://www.phidgets.com/docs/Calibrating_Load_Cells
# https://www.phidgets.com/docs/KIT4007_User_Guide
# https://www.phidgets.com/?prodid=1196#Tab_User_Guide

# Load dependecies --------------------------------------------------------------
from Phidget22.Phidget import *
from Phidget22.Devices.VoltageRatioInput import *
from Phidget22.Devices.Log import *
from Phidget22.LogLevel import *
import time
import os

## Call function from getSerialNumber
from lysimetersUtils import *

# Configuration - specify which channels to use
# Add or remove channels as needed
CHANNELS = [0, 1, 2, 3]

# Global variables for calibration data
calibrated = {each_channel: False for each_channel in CHANNELS}
m = {each_channel: 0 for each_channel in CHANNELS}
b = {each_channel: 0 for each_channel in CHANNELS}


# Method for reading the voltage ------------------------------------------------
def onVoltageRatioChange(self, voltageRatio):
	"""
	Transfrom input voltage to weight in Kilograms. This function uses a
	linear transformation to calcualte weight with y = mx + b.

	Example:
	weight = round((m[channel] * voltageRatio) + b[channel], 3)
	"""
	# Get channel
	channel = self.getChannel()

	if calibrated[channel]:
		# Print in the console
		# sys.stdout.write("\rWeight: " + str(round((m*voltageRatio)+b,2)) + "g      ")

		# Append the channel id, the time and the estimated weight
		with open(f'../{serial_number}_data/{serial_number}_weights_data.txt', 'a') as file:
			file.write(
				f'{channel}, {time.strftime("%D %H:%M:%S")}, {round((m[channel] * voltageRatio) + b[channel], 3)}\n'
			)


# Create folder to store data ---------------------------------------------------
serial_number = getSerialNumber()

if not os.path.exists(f'../{serial_number}_data'):
	os.mkdir(f'../{serial_number}_data')

	print(f'Directory {serial_number}_data created')

else:
	print(f'Directory ../{serial_number}_data already exists.')

# Create folder to store logs ---------------------------------------------------
if not os.path.exists(f'../{serial_number}_data/{serial_number}_logs'):
	os.mkdir(f'../{serial_number}_data/{serial_number}_logs')

else:
	print(f'Directory for storing logs already exists.')

# Create txt file for storing data from each channel  ---------------------------
with open(f'../{serial_number}_data/{serial_number}_weights_data.txt', 'w') as file:
	file.write('channel, date_time, weight_grams\n')


# Main method -------------------------------------------------------------------
def main_balance():
	global calibrated, m, b

	# 0) Log errors and warnings
	Log.enable(
		LogLevel.PHIDGET_LOG_INFO, f'../{serial_number}_data/{serial_number}_logs/phidget.log'
	)

	# Create VoltageRatioInput objects for each channel
	voltage_inputs = {}

	# Initialize and open all channels
	for each_channel in CHANNELS:
		# 1) Create your Phidget channels
		voltage_inputs[each_channel] = VoltageRatioInput()

		# 2) Set addressing parameters to specify which channel to open (if any)
		voltage_inputs[each_channel].setChannel(each_channel)

		# 3) Assign any event handlers you need before calling open so that no
		# events are missed.
		voltage_inputs[each_channel].setOnVoltageRatioChangeHandler(onVoltageRatioChange)

		try:
			# 4) Open your Phidgets and wait 5 seconds for attachment
			voltage_inputs[each_channel].openWaitForAttachment(5000)

			# Set data collection interval to 1 second
			voltage_inputs[each_channel].setDataInterval(1000)

			print(f'Channel {each_channel} attached successfully')

		except PhidgetException as e:
			print(f'Failed to attach channel {each_channel}: {e}')
			continue

	# Calibrate each channel
	for each_channel in CHANNELS:
		if each_channel not in voltage_inputs:
			continue

		print(f'\n--- Calibrating Channel {each_channel} ---')

		try:
			input(f'Clear the scale on channel {each_channel} and press Enter\n')
		except (Exception, KeyboardInterrupt):
			break

		v1 = voltage_inputs[each_channel].getVoltageRatio()

		try:
			w2 = input(
				f'Place a known weight on channel {each_channel}, type the weight in kilograms, and press Enter:\n'
			)

		except (Exception, KeyboardInterrupt):
			break

		v2 = voltage_inputs[each_channel].getVoltageRatio()

		# Calculate slope 'm'
		m[each_channel] = (float(w2) - 0) / (v2 - v1)

		# solve for b using zero point : b = y-mx
		b[each_channel] = 0 - (m[each_channel] * v1)

		print(
			f'Channel {each_channel} Calibration Complete: y = {m[each_channel]}x + {b[each_channel]}'
		)

		calibrated[each_channel] = True

	print('\n--- All channels calibrated ---')
	print('Reading weights from all channels...')

	try:
		input('Press Enter to Stop\n')

	except (Exception, KeyboardInterrupt):
		pass

	# Close all channels
	for each_channel in CHANNELS:
		if each_channel in voltage_inputs:
			voltage_inputs[each_channel].close()


# Run main as a script ----------------------------------------------------------
if __name__ == '__main__':
	main_balance()
