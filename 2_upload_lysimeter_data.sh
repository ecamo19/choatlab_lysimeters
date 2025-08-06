#!/bin/bash

# 1) Define paths ---------------------------------------------------------------

# 1.1) Path to the weight data 
SOURCE_FILE="/home/choatlab/phidget_{SERIAL_NUMBER}_data/phidget_{SERIAL_NUMBER}_data_weights.txt"

# 1.2) Mount OneDrive folder and phidget data 
REMOTE_PATH="onedrive:/lysimeters_data/phidget_{SERIAL_NUMBER}_data"

# 1.3) Path to the copied files in /temp 
TEMP_FILE="/tmp/phidget_{SERIAL_NUMBER}_data.txt"

# 1.4) Path to the compressed file
COMPRESSED_FILE="/tmp/phidget_{SERIAL_NUMBER}_data.7z"

# 2) Check if source file exists ------------------------------------------------
if [[ ! -f "$SOURCE_FILE" ]]; then
    echo $(date  "+%d_%m_%y_%Hh_%M"): Source file $SOURCE_FILE not found
    exit 1
fi

# 3) Copy file to temp location to avoid uploading while it's being written -----
cp "$SOURCE_FILE" "$TEMP_FILE"

# 4) Compress file using 7zip ---------------------------------------------------
# Ref: https://labex.io/tutorials/linux-how-to-use-7zip-cli-for-efficient-file-compression-398414
7z a "$COMPRESSED_FILE" "$TEMP_FILE"

# 5) Upload the file ------------------------------------------------------------
if rclone copy "$COMPRESSED_FILE" "$REMOTE_PATH" --verbose; then
    echo $(date "+%d_%m_%y_%Hh_%M"): Successfully uploaded compressed lysimeter data to OneDrive
else
    echo $(date "+%d_%m_%y_%Hh_%M"): Failed to upload compressed lysimeter data to OneDrive
fi

# 6) Clean up temp and compressed file ------------------------------------------
rm "$TEMP_FILE" "$COMPRESSED_FILE"