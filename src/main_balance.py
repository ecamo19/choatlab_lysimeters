from Phidget22.Phidget import *
from Phidget22.Devices.VoltageRatioInput import *
import time

# Configuration - specify which channels to use
CHANNELS = [0, 1, 2, 3]  # Add or remove channels as needed

# Global variables for calibration data
calibrated = {channel: False for channel in CHANNELS}
m = {channel: 0 for channel in CHANNELS}
b = {channel: 0 for channel in CHANNELS}

def onVoltageRatioChange(self, voltageRatio):
    channel = self.getChannel()
    if calibrated[channel]:
        # Calculate calibrated weight with y = mx + b
        weight = round((m[channel] * voltageRatio) + b[channel], 2)
        print(f"\rChannel {channel} Weight: {weight}g      ", end="")

def main():
    global calibrated, m, b
    
    # Create VoltageRatioInput objects for each channel
    voltage_inputs = {}
    
    # Initialize and open all channels
    for channel in CHANNELS:
        voltage_inputs[channel] = VoltageRatioInput()
        voltage_inputs[channel].setOnVoltageRatioChangeHandler(onVoltageRatioChange)
        voltage_inputs[channel].setChannel(channel)
        
        try:
            voltage_inputs[channel].openWaitForAttachment(5000)
            print(f"Channel {channel} attached successfully")
        except PhidgetException as e:
            print(f"Failed to attach channel {channel}: {e}")
            continue
    
    # Calibrate each channel
    for channel in CHANNELS:
        if channel not in voltage_inputs:
            continue
            
        print(f"\n--- Calibrating Channel {channel} ---")
        
        try:
            input(f"Clear the scale on channel {channel} and press Enter\n")
        except (Exception, KeyboardInterrupt):
            break
        
        v1 = voltage_inputs[channel].getVoltageRatio()
        
        try:
            w2 = input(f"Place a known weight on channel {channel}, type the weight in grams, and press Enter:\n")
        except (Exception, KeyboardInterrupt):
            break
        
        v2 = voltage_inputs[channel].getVoltageRatio()
        
        # Calculate slope 'm'
        m[channel] = (float(w2) - 0) / (v2 - v1)
        # solve for b using zero point : b = y-mx
        b[channel] = 0 - (m[channel] * v1)
        
        print(f"Channel {channel} Calibration Complete: y = {m[channel]}x + {b[channel]}")
        calibrated[channel] = True
    
    print("\n--- All channels calibrated ---")
    print("Reading weights from all channels...")
    
    try:
        input("Press Enter to Stop\n")
    except (Exception, KeyboardInterrupt):
        pass
    
    # Close all channels
    for channel in CHANNELS:
        if channel in voltage_inputs:
            voltage_inputs[channel].close()

if __name__ == "__main__":
    main()