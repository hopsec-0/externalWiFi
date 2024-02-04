import os
import pwnagotchi
import pwnagotchi.plugins as plugins
import logging


class externalWiFi(plugins.Plugin):
    __author__ = 'matt@hopsec.co'
    __version__ = '0.0.1'
    __license__ = 'GPL3'
    __description__ = 'Automatically detects and switches to external WiFi adapters'

    def __init__(self):
        self.externalWiFi = false

    def on_loaded(self):
        logging.info("externalWiFi plugin loaded for %s" % self.options['device'])

        for
            logging.info("")

        if [ -e cat /sys/class/net/wlan1 ]:
            with open("/boot/config.txt", 'r+') as conFile:
                lines = conFile.readlines()
                for row in lines:
                    wifiConfig = 'dtoverlay=disable-wifi'
                    if row.find(word) != -1:
                        conFile.write(wifiConfig)
                        self.externalWiFi = true
             os.system('sudo shutdown -r now')
        elif [ ! -e cat /sys/class/net/wlan0 ]:
            with open("/boot/config.txt", 'r+') as conFile:
                lines = conFile.readlines()
                conFile.seek(0)
                for row in lines:
                    if row.find != "dtoverlay=disable-wifi":
                        f.write(row)
                f.truncate()
                self.externalWiFi = false
            os.system('sudo shutdown -r now')
                        