# Configure steps for crontab ---------------------------------------------------

# Web page for figuring out crontab time: https://crontab.guru/ 

## 1) Change the persimission of rclone file ------------------------------------

# chmod +x ~/choatlab_lysimeters/2_upload_lysimeter_data.sh

## 2) Configure rclone  ---------------------------------------------------------

# Watch the following video if forgotten how...
# https://www.youtube.com/watch?v=u_W0-HEVOyg

# rclone config 

# Check rclone is working
# The code should list some files in the OneDrive 

# rclone ls onedrive:/ | tail

## 3) Configure crontab ---------------------------------------------------------

# List current user's cron jobs

# crontab -l

# Configure crontab

# crontab -e

## Copy and paste one the following: 

# Run upload code every minute
# * * * * * /home/choatlab/choatlab_lysimiters/2_upload_lysimeter_data.sh >> /home/choatlab/upload.log 2>&1

# Run upload code every 5 minutes
# */5 * * * * /home/choatlab/choatlab_lysimiters/2_upload_lysimeter_data.sh >> /home/choatlab/upload.log 2>&1 

# Run upload code every hour
# 0 * * * * /home/choatlab/choatlab_lysimiters/2_upload_lysimeter_data.sh >> /home/choatlab/upload.log 2>&1

# Run upload code every day at midnight 
# 0 0 * * * /home/choatlab/choatlab_lysimiters/2_upload_lysimeter_data.sh >> /home/choatlab/upload.log 2>&1
