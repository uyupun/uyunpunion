#!/bin/sh

# QEMU上でRaspberry Pi 3 model Bをエミュレートするために必要なファイルのダウンロードや設定を行うスクリプト

# source: https://github.com/dhruvvyas90/qemu-rpi-kernel/tree/master/native-emulation
curl -O https://raw.githubusercontent.com/dhruvvyas90/qemu-rpi-kernel/master/native-emulation/5.4.51%20kernels/kernel8.img
curl -O https://raw.githubusercontent.com/dhruvvyas90/qemu-rpi-kernel/master/native-emulation/dtbs/bcm2710-rpi-3-b.dtb

curl -O http://ftp.jaist.ac.jp/pub/raspberrypi/raspios_lite_arm64/images/raspios_lite_arm64-2022-09-07/2022-09-06-raspios-bullseye-arm64-lite.img.xz
xz -d 2022-09-06-raspios-bullseye-arm64-lite.img.xz

qemu-img \
resize -f raw 2022-09-06-raspios-bullseye-arm64-lite.img 4G
