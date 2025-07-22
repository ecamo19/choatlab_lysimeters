# Run the choatlab lysimeters 

## 1) Clone repo into the raspberry pi and enter the folder

```bash
git clone https://github.com/ecamo19/choatlab_lysimeters.git
```

```bash
cd choatlab_lysimeters
```

## 2) Configure udev rule

```bash
bash 1_config_udev_rule.sh
```

## 3) Open pixi shell

```bash
pixi shell
```

## 4) Create tmux session

```bash
tmux new -s lysimeters
```

## 5) Run pixi task

```bash
pixi run balance
```

## 6) Detach tmux session

Press Ctrl-b and then d

# Quick tmux cheat sheet:

+ Ctrl+B, D - Detach session
+ tmux ls - List sessions
+ tmux attach -t sessionname - Reattach
+ Ctrl+B, C - Create new window in session
+ Ctrl+B, [ - Scroll mode (use arrow keys, press q to exit)
