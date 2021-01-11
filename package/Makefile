default:

.PHONY: build-source
build-source:
	dpkg-source -b

.PHONY: build
build:
	dpkg-buildpackage -us -uc --host-arch armhf --build=any

