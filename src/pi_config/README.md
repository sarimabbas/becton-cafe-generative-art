This folder is for starting Processing sketches on boot of the Raspberry Pi.

1. `sudo nano ~/.config/lxsession/LXDE-pi/autostart`
2. Add this to the end: `@bash /path/to/src/pi_config/runSketch.sh`
3. `sudo reboot`
