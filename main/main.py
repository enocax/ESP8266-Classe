 from ota_update.main.ota_updater import OTAUpdater


 def download_and_install_update_if_available():
     o = OTAUpdater('https://github.com/enocax/ESP8266-Classe')
     o.download_and_install_update_if_available('Raspberry', 'raspberry')


 def start():
     # your custom code goes here. Something like this: ...
     # from main.x import YourProject
     # project = YourProject()
     # ...
     


 def boot():
     download_and_install_update_if_available()
     start()


 boot()
 