from fasthtml.common import *
from Phidget22.Phidget import *
from Phidget22.Devices.VoltageRatioInput import *
import asyncio
import json
from datetime import datetime

# Global variable to store the latest reading
Check if the values are being appended to the latest_reading 

latest_reading = {"value": 0.0, "timestamp": "", "connected": False}

# Phidget event handlers
def onVoltageRatioChange(self, voltageRatio):
    """Called when voltage ratio changes"""
    global latest_reading
    latest_reading["value"] = voltageRatio
    latest_reading["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    latest_reading["connected"] = True

def onAttach(self):
    """Called when Phidget is attached"""
    print("PhidgetBridge attached!")
    # Set data interval to 100ms for responsive updates
    self.setDataInterval(100)
    latest_reading["connected"] = True

def onDetach(self):
    """Called when Phidget is detached"""
    print("PhidgetBridge detached!")
    latest_reading["connected"] = False

def onError(self, code, description):
    """Called when an error occurs"""
    print(f"Error {code}: {description}")
    latest_reading["connected"] = False

# Initialize Phidget
ch = None
phidget_error = None

def initialize_phidget():
    global ch, phidget_error
    try:
        ch = VoltageRatioInput()
        ch.setOnVoltageRatioChangeHandler(onVoltageRatioChange)
        ch.setOnAttachHandler(onAttach)
        ch.setOnDetachHandler(onDetach)
        ch.setOnErrorHandler(onError)
        
        # Set channel 0 (adjust if your load cell is on a different channel)
        ch.setChannel(2)
        
        ch.openWaitForAttachment(5000)
        print("PhidgetBridge connected successfully")
        phidget_error = None
        return True
    except PhidgetException as e:
        error_msg = str(e)
        print(f"Failed to connect to PhidgetBridge: {error_msg}")
        phidget_error = error_msg
        
        if "device is in use" in error_msg:
            print("\nTroubleshooting tips:")
            print("1. Close the Phidget Control Panel if it's open")
            print("2. Check for other Python processes using the device")
            print("3. Try unplugging and replugging the PhidgetBridge")
            print("4. Wait a few seconds and restart this application")
        
        ch = None
        return False

# Try to initialize the Phidget
phidget_connected = initialize_phidget()

# Create FastHTML app
app, rt = fast_app(
    hdrs=(
        Script(src="https://unpkg.com/htmx.org@1.9.10"),
        Style("""
            body { 
                font-family: Arial, sans-serif; 
                max-width: 800px; 
                margin: 0 auto; 
                padding: 20px;
                background-color: #f5f5f5;
            }
            .container {
                background-color: white;
                border-radius: 10px;
                padding: 30px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }
            .status {
                display: inline-block;
                padding: 5px 15px;
                border-radius: 20px;
                font-weight: bold;
                margin-bottom: 20px;
            }
            .connected { 
                background-color: #4CAF50; 
                color: white; 
            }
            .disconnected { 
                background-color: #f44336; 
                color: white; 
            }
            .reading {
                font-size: 48px;
                font-weight: bold;
                color: #333;
                margin: 20px 0;
                text-align: center;
            }
            .timestamp {
                color: #666;
                text-align: center;
                font-size: 14px;
            }
            .info {
                background-color: #e3f2fd;
                border-left: 4px solid #2196F3;
                padding: 15px;
                margin-top: 20px;
            }
            h1 {
                color: #333;
                text-align: center;
            }
        """)
    )
)

@rt('/')
def get():
    if phidget_error:
        return Div(
            H1("PhidgetBridge Load Cell Monitor"),
            Div(
                H2("⚠️ Connection Error", style="color: #f44336;"),
                P(f"Error: {phidget_error}", style="color: #666;"),
                Div(
                    H3("Troubleshooting Steps:"),
                    Ol(
                        Li("Close the Phidget Control Panel if it's open"),
                        Li("Check Task Manager for other Python processes using the device"),
                        Li("Unplug and replug the PhidgetBridge USB connection"),
                        Li("Wait a few seconds and refresh this page")
                    ),
                    cls="info"
                ),
                Button(
                    "Retry Connection",
                    onclick="window.location.reload()",
                    style="background-color: #2196F3; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; font-size: 16px;"
                ),
                cls="container",
                style="text-align: center;"
            )
        )
    
    return Div(
        H1("PhidgetBridge Load Cell Monitor"),
        Div(
            Div(
                "Connected" if latest_reading["connected"] else "Disconnected",
                cls=f"status {'connected' if latest_reading['connected'] else 'disconnected'}"
            ),
            Div(
                f"{latest_reading['value']:.6f}",
                cls="reading",
                id="voltage-ratio"
            ),
            Div(
                f"Last update: {latest_reading['timestamp'] or 'Never'}",
                cls="timestamp",
                id="timestamp"
            ),
            Div(
                H3("Configuration"),
                P("Channel: 0"),
                P("Data Interval: 100ms"),
                P("This app continuously monitors the voltage ratio from a load cell connected to a PhidgetBridge."),
                cls="info"
            ),
            cls="container",
            hx_get="/reading",
            hx_trigger="every 100ms",
            hx_target="this",
            hx_swap="outerHTML"
        )
    )

@rt('/reading')
def get_reading():
    if phidget_error:
        return Div("Error: Unable to connect to PhidgetBridge", style="color: red; text-align: center; padding: 20px;")
    
    return Div(
        Div(
            "Connected" if latest_reading["connected"] else "Disconnected",
            cls=f"status {'connected' if latest_reading['connected'] else 'disconnected'}"
        ),
        Div(
            f"{latest_reading['value']:.6f}",
            cls="reading",
            id="voltage-ratio"
        ),
        Div(
            f"Last update: {latest_reading['timestamp'] or 'Never'}",
            cls="timestamp",
            id="timestamp"
        ),
        Div(
            H3("Configuration"),
            P("Channel: 0"),
            P("Data Interval: 100ms"),
            P("This app continuously monitors the voltage ratio from a load cell connected to a PhidgetBridge."),
            cls="info"
        ),
        cls="container",
        hx_get="/reading",
        hx_trigger="every 100ms",
        hx_target="this",
        hx_swap="outerHTML"
    )

@rt('/api/reading')
def get_api_reading():
    """API endpoint to get the current reading as JSON"""
    return json.dumps(latest_reading)

# Cleanup function
def cleanup():
    global ch
    if ch:
        try:
            ch.close()
            print("PhidgetBridge connection closed")
        except:
            pass

# Run the app
if __name__ == "__main__":
    try:
        serve()
    except KeyboardInterrupt:
        cleanup()
        print("\nApp stopped")