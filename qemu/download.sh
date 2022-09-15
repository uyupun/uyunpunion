#!/bin/sh

curl -O https://raw.githubusercontent.com/raspberrypi/firmware/master/boot/kernel7l.img
curl -O https://raw.githubusercontent.com/raspberrypi/firmware/master/boot/bcm2710-rpi-3-b-plus.dtb

curl -O http://ftp.jaist.ac.jp/pub/raspberrypi/raspios_oldstable_armhf/images/raspios_oldstable_armhf-2022-09-07/2022-09-06-raspios-buster-armhf.img.xz
xz -d 2022-09-06-raspios-buster-armhf.img.xz
