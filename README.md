# RaspberryPi_LightSwitch
This project is meant to be the first step in home automation. To replicate this project you will need a raspberry pi, a 3v relay module, and a 3 way switch. The idea is to be able to turn on and off any light at home from the raspberry py keeping the option to turn it on and off from the switch.
We created a simple tornado webserver so you will be able to turn on and off the light from any web browser.

-------

## Wiring diagram

<p align="center">
  <img src="https://raw.githubusercontent.com/craguila/RaspberryPi_LightSwitch/master/schematics_bb.png" width="350"/>
</p>

-----

## Instalation
### Check your switch
The first thing you need to do is to check if at home you have the correct switch type. You will need a 3 way switch in order to be able to continue using your home switch. If you want to control your light only from the raspberry, this step is optional.
The 3 way switch is the one used to light stairs and corridors, where we have one switch at the beginning and another at the end of the corridor. In this case our raspberry pi will be replacing the one on the other side of the corridor.

### Connecting the 3v Relay to your home wiring
<p align="center">
  <img src="https://raw.githubusercontent.com/craguila/RaspberryPi_LightSwitch/master/3v-relay-module-240vac-10a.jpg" width="200"/>
</p>
Because of the 3.3v GPIO, we will be using a 3v Relay Module. This module can be purchased on ebay or your favorite store. Make sure it can be controled using a 3v input.
This relay module has 3 pins for the light and 3 pins for the raspberry.
The folowing diagram shows how to connect the 3 pins for the light. The Com pin must be connected to the home wiring. :warning: It's dangerous to play arround with 220 or 110 v. Make shure you have turned off the electric current at home before wiring the relay module. Also make sure that there are no wires at sight after making the connections. :warning:
<p align="center">
  <img src="https://raw.githubusercontent.com/craguila/RaspberryPi_LightSwitch/master/fig02.gif" width="200"/>
</p>

### Conneting the 3v Relay module to the raspberry pi
The Relay module has 3 pins, VCC, IN and GND. The VCC pin must be connected to a 3,3v pin. In this example it has been connected to Pin 1. The GND pin must be connected to any GND pin on the raspberry. In this case we have connected it to Pin 6.
The IN pin is the one that controls the relay. When the pin is set high the relay will turn on, and the light state will change. If the pin is set low, the relay will turn off, also the light state will change.
In this case we have setup the pin 3 as the control pin.

## Setup
### Seting up the server
In the server.py file a tornado server is running on port 80
There are two routes stablished, http://localhost/ and http://localhost/onoff
The first route renders the luz.html file, and shows the clients a switch to change the state of pin 3.
The second route id a direct link to change the state of pin 3.
After wiring the relay module, the only thing left to do is to start the server.

### Starting the server
Start server 

` sudo python server.py `

To access the server go to
[ http://localhost/ ](http://localhost/)
or to [ http://localhost/onoff ](http://localhost/onoff)
