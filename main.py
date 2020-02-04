 from ota_update.main.ota_updater import OTAUpdater
 from machine import Pin
 from time import sleep 

 def download_and_install_update_if_available():
     o = OTAUpdater('https://github.com/enocax/ESP8266-Classe')
     o.download_and_install_update_if_available('Raspberry', 'raspberry')


 def start():
     # your custom code goes here. Something like this: ...
    p2= Pin(5, Pin.OUT)
    while 1:
        p2.on
        sleep(2)
        p2.off


 def boot():
     download_and_install_update_if_available()
     start()


 boot()
 
