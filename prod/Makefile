.PHONY: status ls change

wlan-status:
	iwconfig wlan0
	ip a show wlan0

wlan-ls:
	iwlist wlan0 scan | grep ESSID

wlan-change: ssid ?= ""
wlan-change: psk ?= ""
wlan-change:
	@if [ -z "$(ssid)" ]; then printf "\e[31m%s\e[m\n" "SSIDが指定されていません。"; exit 1; fi
	@if [ -z "$(psk)" ]; then printf "\e[31m%s\e[m\n" "PSKが指定されていません"; exit 1; fi
	sudo sed -i '/network={/,/}/d' /etc/wpa_supplicant/wpa_supplicant.conf
	wpa_passphrase $(ssid) $(psk) | grep -v '^[[:space:]]*#psk' | sudo tee -a /etc/wpa_supplicant/wpa_supplicant.conf > /dev/null
	sudo wpa_cli -i wlan0 reconfigure
