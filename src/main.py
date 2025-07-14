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
