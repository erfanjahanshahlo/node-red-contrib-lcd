# About
This module is lcd node for [node red](https://nodered.org/). in this node you can write a string to liquid crystal lcd.
# Install via Git
Run the following code in your raspberry pi terminal
```
cd /home/pi/.node-red/node_modules
git clone https://github.com/erfanjahanshahlo/node-red-contrib-lcd.git
```
and restart your node red server or reboot your raspberry pi.
# Install via npm
Run the following code in your raspberry pi terminal
```
cd /home/pi/.node-red/node_modules
npm install node-red-contrib-lcd
```
and restart your node red server or reboot your raspberry pi.
# Install via Download
in step one download this repository and rename main folder to ```node-red-contrib-lcd``` like the schematic below and copy to ```/home/pi/.node-red/node_modules``` path in your raspberry pi and restart your node red server or reboot your raspberry pi.
<br/>
-node-red-contrib-lcd<br/>
---driver<br/>
------codecs<br/>
---------_init_.py<br/>
---------hd44780_a00.py<br/>
---------hd44780_a02.py<br/>
------_init_.py<br/>
------common.py<br/>
------compat.py<br/>
------contextmanagers.py<br/>
------gpio.py<br/>
------lcd.py<br/>
---package.json<br/>
---lcd.py<br/>
---lcd.js<br/>
---lcd.html<br/>
# Getting started
Here's how to send data to this node.
```
ROW,COL:YOUR TEXT
```
for clear lcd send ```1,1:``` to the node to clear lcd.
in node settings form in pins, type you must enter the pins to which the LCD is attached and the number of rows and columns shown below. Note that the pin numbering are ***physical*** and ***board*** not ***BCM***. if not set pins and the row,cols the node not working.
```
RS,EN,D4,D5,D6,D7,ROW,COL
```
> Be careful not to use any spaces in any of these commands.
# Example
![Example](http://s6.picofile.com/file/8383964726/example_node.png)
