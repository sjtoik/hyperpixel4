# command line testing
# $ raspi-gpio set 19 op dl
# $ raspi-gpio set 19 op dh

# pi@pascal:~ $ DISPLAY=:0 xscreensaver-command -watch
# UNBLANK Sun Oct  4 14:48:25 2020
# BLANK Sun Oct  4 14:48:37 2020
# UNBLANK Sun Oct  4 14:48:47 2020

import gpiozero

screen_backlight = gpiozero.OutputDevice(pin=19)
screen_backlight.toggle()
