# duper8
DigitalSuper8Camera



https://hackaday.io/project/184748-a-spring-drive-digital-movie-camera

https://hackaday.io/project/178439/logs

https://cults3d.com/de/modell-3d/werkzeuge/super8-film-cartridge-printtable-parts-to-refil-iso-asa-100

https://gist.github.com/befinitiv/fd44a597a48460c100a54649c97d5984

Neue Inspo:
3d Housing:
https://www.thingiverse.com/thing:6085558

In dem Projekt Sensor dauerhaft an und wenn licht kommt dann startet Aufnahme glaub
Code und Projekt: 
https://github.com/Codaea/DigitalSuper8



### Installation requirements on RaspberryPi

Camera requirements
```
sudo apt install -y python3-picamera2 --no-install-recommends
```


To convert h264 to MP4
```
sudo apt-get -y install gpac
```


### Workflow 

- Convert h265 to mp4 -> 
```
MP4Box -add test.h264 test.mp4
```
- Copy File to Desktop -> 
```
scp pi@duper8:/home/pi/test.mp4 /Users/hpe/Desktop
```


### for chron job

@reboot sh /home/duper8/launcher.sh >/home/duper8/logs/cronlog 2>&1


### Copy files to folder
ssh duper8@duper8.local "python convert.py"
scp -r duper8@duper8.local:Videos/MP4 /Volumes/T7\ Shield/Joel\ Weiss/Bilder_Videos/duper8/2024/0216_ersteAufnahmen
ssh duper8@duper8.local "rm /home/duper8/Videos/MP4/*"
ssh duper8@duper8.local "rm /home/duper8/Videos/*"