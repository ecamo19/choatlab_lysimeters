#!/bin/bash

# Path to the weight data
SOURCE_FILE="/home/choatlab/phidget_{serial_number}_data/phidget_{serial_number}_data_weights.txt"

# Mount OneDrive folder and phidget data 
REMOTE_PATH="onedrive:/lysimeters_data/phidget_{serial_number}_data"

# Path to /temp 
TEMP_FILE="/tmp/data_upload_$(date + %d_%m_%Y_%Hh_%M).txt"

# Check if source file exists
if [[ ! -f "$SOURCE_FILE" ]]; then
    echo "$(date + %d_%m_%Y_%Hh_%M): Source file $SOURCE_FILE not found"
    exit 1
fi

# Copy file to temp location to avoid uploading while it's being written
cp "$SOURCE_FILE" "$TEMP_FILE"

# Upload the file
if rclone copy "$TEMP_FILE" "$REMOTE_PATH" --verbose; then
    echo "$(date + %d_%m_%Y_%Hh_%M): Successfully uploaded lysimeter data to OneDrive"
else
    echo "$(date + %d_%m_%Y_%Hh_%M): Failed to upload data.txt to OneDrive"
fi

# Clean up temp file
rm "$TEMP_FILE"
