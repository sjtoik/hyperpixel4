install: hyperpixel4-backlight.service
	cp hyperpixel4-backlight.service /etc/systemd/system/
	systemctl enable /etc/systemd/system/hyperpixel4-backlight.service
	systemctl start hyperpixel4-backlight

remove:
	rm /etc/systemd/system/hyperpixel4-backlight.service
	systemctl disable /etc/systemd/system/hyperpixel4-backlight.service
