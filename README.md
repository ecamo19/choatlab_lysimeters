# Configure Raspberry Pi to run choatlab lysimeters code  

## 1) Flash Raspberry pi image

## 2) Configure wifi network on terminal

### Find ssid

```bash
nmcli device wifi rescan
nmcli device wifi list
```

### Log in into Uni Wifi

```bash
nmcli connection add type wifi con-name "UniWiFi" ifname wlan0 ssid "Western Wifi" wifi-sec.key-mgmt wpa-eap \ 
 802-1x.eap peap \ 
 802-1x.phase2-auth mschapv2 \
 802-1x.identity "YOUR_USERNAME" \
 802-1x.password "YOUR_PASSWORD"
```

## 3) Install linux dependencies that are _NOT_ included in pixi 

```bash
apt update
apt upgrade
```

### Git

```bash
apt install git
```

### Raspberry connect

```bash
apt install rpi-connect-lite
```

### Pixi-dev

```bash
curl -fsSL https://pixi.sh/install.sh | sh
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

### rclone

```bash
apt install rclone
```

## 5) Clone githib repo into the raspberry pi and enter the folder

```bash
git clone https://github.com/ecamo19/choatlab_lysimeters.git
```

```bash
cd choatlab_lysimeters
```

## 6) Configure udev rule for accessing USB ports

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

### 7.3) Start pixi shell _again_ and run the pixi task

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

## 9) Check raspberry pi stats

### Watch raspberry temp every 2 seconds

```bash
watch -n 2 vcgencmd measure_temp
```

### Check memory ram usage

```bash
htop
```