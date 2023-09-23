.PHONY: scan pssh ssh remkey wlstatus wlls wlchange

scan:
	arp-scan -l --interface en0 | grep "Raspberry Pi"

pssh: host ?= "uyunpunion-01.local"
pssh:
	ssh -i id_ed25519 pi@$(host)

ssh: host ?= "uyunpunion-01.local"
ssh:
	ssh -i ../playbook/roles/user/files/id_ed25519 takashi@$(host)

remkey: host ?= "uyunpunion-01.local"
remkey:
	ssh-keygen -R $(host)

wlstatus:
	iwconfig wlan0
	ip a show wlan0

wlls:
	iwlist wlan0 scan | grep ESSID

wlchange: ssid ?= ""
wlchange: psk ?= ""
wlchange:
	@if [ -z "$(ssid)" ]; then printf "\e[31m%s\e[m\n" "SSIDが指定されていません。"; exit 1; fi
	@if [ -z "$(psk)" ]; then printf "\e[31m%s\e[m\n" "PSKが指定されていません"; exit 1; fi
	sudo sed -i '/network={/,/}/d' /etc/wpa_supplicant/wpa_supplicant.conf
	wpa_passphrase $(ssid) $(psk) | grep -v '^[[:space:]]*#psk' | sudo tee -a /etc/wpa_supplicant/wpa_supplicant.conf > /dev/null
	sudo wpa_cli -i wlan0 reconfigure
