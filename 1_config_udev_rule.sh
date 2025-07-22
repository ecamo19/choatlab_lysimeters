#!/bin/bash

# Modify the /home/choatlab if required
# Run code by using bash 1_config_udev_rule.sh 

mv /home/choatlab/choatlab_lysimeters/src/99-libphidget22.rules /etc/udev/rules.d/99-libphidget22.rules & udevadm control --reload-rules & udevadm trigger