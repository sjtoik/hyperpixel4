# Hyperpixel4 project stuff

* store page: https://shop.pimoroni.com/products/hyperpixel-4?variant=12569485443155
* pinout: https://pinout.xyz/pinout/hyperpixel4#
* github: https://github.com/pimoroni/hyperpixel4
* interesting github thread: https://github.com/pimoroni/hyperpixel4/issues/119

Needs i2c invocation source to turn on the screen. XScreenSaver puts it to rest and GPIO 19 toggling turns of the backlight also,
but there is no way to invoke the black screen, as turning the backlight of turns also the touch screen
off.
This is oddity in the design, which can't be ironed out with a software upgrade.

The interaction on shutdown is also counterintuitive. 
On system shutdown, the gpio-backlight module is unloaded, and the systems returns the pin to the default state of high impedance. This results the backlight first turning off while halting, but then turning back on and staying on for the as long there is juice left in the Pi.
A systemd hack ./hyperpixel4-backlight.service will sort the problem as proposed [in issues by the original developer](https://github.com/pimoroni/hyperpixel4/issues/3).

## Notes
* regex cheat sheet https://regexr.com/
