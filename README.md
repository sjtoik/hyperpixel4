# Hyperpixel4 project stuff

* store page: https://shop.pimoroni.com/products/hyperpixel-4?variant=12569485443155
* pinout: https://pinout.xyz/pinout/hyperpixel4#
* github: https://github.com/pimoroni/hyperpixel4
* interesting github thread: https://github.com/pimoroni/hyperpixel4/issues/119

Needs i2c invocation source or external input device to turn on the screen.
There is i2c bus, 3,3V power and ground available for sensors for example.
External invocation source is required as the turning off the backlight also turns of the touchscreen.
This is oddity in the hardware design, which can't be ironed out with a software upgrade.

The interaction on shutdown is also counterintuitive. 
On system shutdown, the gpio-backlight module is unloaded, and the systems returns the pin to the default state of high impedance. 
This results the backlight first turning off while halting, but then turning back on and staying on for the as long there is juice left in the Pi.
A systemd hack hyperpixel4-backlight.service will sort the problem as proposed [in issues by the original developer](https://github.com/pimoroni/hyperpixel4/issues/3).

## Notes
* regex cheat sheet https://regexr.com/
