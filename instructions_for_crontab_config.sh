# Configure steps for crontab ---------------------------------------------------

# Watch the following video if forgotten how to configure rclone:
# https://www.youtube.com/watch?v=u_W0-HEVOyg

# Web page for figuring out crontab time: https://crontab.guru/ 

## 1) Change the persimission of rclone file ------------------------------------

```bash
# chmod +x ~/choatlab_lysimeters/2_upload_lysimeter_data.sh
```

## 2) Configure rclone  ---------------------------------------------------------

```bash
# rclone config 
```

## Remember to input N on question:

 # Use web browser to automatically authenticate rclone with remote?
 # * Say Y if the machine running rclone has a web browser you can use
 # * Say N if running rclone on a (remote) machine without web browser access

## Remember to name the folder as onedrive

# Check rclone is working
# The code should list some files in the OneDrive 

```bash
# rclone ls onedrive:/ | tail
```

## 3) Configure crontab ---------------------------------------------------------

# Configure crontab

```bash
# crontab -e
```

## Copy and paste one the following: 

## Remember to edit the 2_upload_lysimeter_data.sh with the correct phidget 

# Run upload code every minute
# * * * * * /home/choatlab/choatlab_lysimeters/2_upload_lysimeter_data.sh >> /home/choatlab/upload.log 2>&1

# Run upload code every 5 minutes
# */5 * * * * /home/choatlab/choatlab_lysimeters/2_upload_lysimeter_data.sh >> /home/choatlab/upload.log 2>&1 

# Run upload code every hour
# 0 * * * * /home/choatlab/choatlab_lysimeters/2_upload_lysimeter_data.sh >> /home/choatlab/upload.log 2>&1

# Run upload code every day at midnight 
# 0 0 * * * /home/choatlab/choatlab_lysimeters/2_upload_lysimeter_data.sh >> /home/choatlab/upload.log 2>&1

# List current user's cron jobs

```bash
# crontab -l
```
