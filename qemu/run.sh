#!/bin/sh

# QEMU上でRaspberry Pi 3 model Bをエミュレートするスクリプト

qemu-system-aarch64 \
-M raspi3b \
-cpu cortex-a53 -smp 4 \
-m 1024 \
-dtb bcm2710-rpi-3-b.dtb \
-kernel kernel8.img \
-sd 2022-09-06-raspios-bullseye-arm64-lite.img \
-netdev user,id=net0,hostfwd=tcp::2222-:22 \
-serial stdio \
-usb -device usb-mouse -device usb-kbd \
-device usb-net,netdev=net0 \
-append "rw earlyprintk loglevel=8 console=ttyAMA0,115200 dwc_otg.lpm_enable=0 root=/dev/mmcblk0p2 rootdelay=1"
