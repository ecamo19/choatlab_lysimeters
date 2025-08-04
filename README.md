# Run the choatlab lysimeters code on a Raspberry Pi 

## 1) Flash Raspberry pi image

## 2) Configure wifi network on terminal

```bash
# Find ssid
nmcli device wifi rescan
nmcli device wifi list
```

```bash
# Log in into Uni Wifi

nmcli connection add type wifi con-name "UniWiFi" ifname wlan0 ssid "Western Wifi" wifi-sec.key-mgmt wpa-eap \ 
 802-1x.eap peap \ 
 802-1x.phase2-auth mschapv2 \
 802-1x.identity "YOUR_USERNAME" \
 802-1x.password "YOUR_PASSWORD"
```

## 3) Install linux dependencies

```bash
apt update
apt upgrade
```

```bash
# Install git
apt install git
```

```bash
# Install pixi-dev
curl -fsSL https://pixi.sh/install.sh | sh
```

```bash
# Install raspberry connect
apt install rpi-connect-lite
```
```bash
# Install rclone
apt install rclone
```
## 4) Configure rpi-connect-lite

```bash
raspi-config
```

```bash
rpi-connect on
rpi-connect signin
rpi-connect shell on
loginctl enable-linger
rpi-connect doctor
rpi-connect status
rpi-connect restart
```

## 5) Clone repo into the raspberry pi and enter the folder

```bash
git clone https://github.com/ecamo19/choatlab_lysimeters.git
```

```bash
cd choatlab_lysimeters
```

## 6) Configure udev rule

```bash
bash 1_config_udev_rule.sh
```

## 7) Run lysimeter

### Quick tmux cheatsheet:

+ `Ctrl+B`, `D` -> Detach session
+ `tmux ls` -> List sessions
+ `tmux attach -t sessionname` -> Reattach
+ `Ctrl+B`, `C` -> Create new window in session
+ `Ctrl+B`, `[` -> Scroll mode (use arrow keys, press q to exit)

### 7.1) Start pixi shell

```bash
pixi shell
```

### 7.2) Create tmux session

```bash
tmux new -s lysimeter_session
```

### 7.3) Run open pixi shell again and run pixi task

```bash
pixi shell
pixi run balance
```

### 7.4) Detach tmux session

Press Ctrl-b and then d

### 7.5) Attach to tmux session

```bash
pixi shell

# Check if the session is running
tmux ls
tmux attach
```

## 8) Configure crontab for uploading data to Onedrive

Follow the instructions outlined in the `instructions_for_crontab_config.sh` file

```bash
cat instructions_for_crontab_config.sh
```
