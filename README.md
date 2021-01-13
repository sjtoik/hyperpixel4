# Hyperpixel4 backlight utilities

A winter project to enable system integration with Hyperpixel4 screen and Raspberry Pi 4.
Backlight service uses XScreenSaver events to control the GPIO 19 pin which turns of the backlight, and wakes up the screen when touch is applied.

## Installation hack

There is a problem with debian packaging scripts for systemd that I haven't figured out yet.
The packagin rules are misconfigured to enable systemd service delivery, but the scripts will not install the service for the user.
You need to manually enable and start the screensaver backlight service.
```
systemctl --user enable hyperpixel4-backlight
systemctl --user start hyperpixel4-backlight
```
The issue is tracked in https://github.com/sjtoik/hyperpixel4/issues/1

## About shutdown-hack

On system shutdown, the gpio-backlight module is unloaded, and the systems returns the pin to the default state of high impedance.
This results the backlight first turning off while halting, but then turning back on and staying on for the as long there is juice left in the Pi.
A systemd hack [hyperpixel4-shutdown-hack.service](./package/debian/hyperpixel4-shutdown-hack.service) will sort the problem as proposed [in issues by the original developer](https://github.com/pimoroni/hyperpixel4/issues/3).

## Background
* store page: https://shop.pimoroni.com/products/hyperpixel-4?variant=12569485443155
* pinout: https://pinout.xyz/pinout/hyperpixel4#
* github: https://github.com/pimoroni/hyperpixel4
* interesting github thread: https://github.com/pimoroni/hyperpixel4/issues/119

There is i2c bus, 3,3V power and ground available for sensors for example.

## Notes
* regex cheat sheet https://regexr.com/
