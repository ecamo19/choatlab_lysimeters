#!/bin/bash

# Find ssid
# nmcli device wifi rescan
# nmcli device wifi list

# Login into Uni Wifi
nmcli connection add type wifi con-name "UniWiFi" ifname wlan0 ssid "Western Wifi" wifi-sec.key-mgmt wpa-eap 802-1x.eap peap 802-1x.phase2-auth mschapv2 \
802-1x.identity "YOUR_USERNAME" \
802-1x.password "YOUR_PASSWORD"
