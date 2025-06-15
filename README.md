# Project Rose

Project Rose was developed for the Unconventional Interfaces course. It is an interactive assistant capable of communicating via a serial interface to control a light actuator and read temperature and humidity sensors.

<p align="center">
  <img src="https://github.com/user-attachments/assets/1c466cca-b49e-4510-aeac-43c6a6ec5f72" width="300">
</p>

## Hardware

The hardware consists of an ESP32, with an LED connected to pin 19 and a DHT11 sensor connected to pin 22.

<p align="center">
  <img src="https://github.com/user-attachments/assets/72452a20-ab41-496e-b57d-4fdc1de3d542">
</p>

## How to run

Navigate to the "rose" folder:

```bash
  $ cd rose
```

Install the dependencies:

```bash
  $ pip install -r requirements
```

Then run the main script:

```
  $ python main.py
```

## Commands

The commands must be spoken in Portuguese. Before giving a command, you need to call "Rose" and wait for her response.

 - "Ligar luz" -> Turns the light on
 - "Desligar luz" -> Turns the light off
 - "Qual é a temperatura?" -> Asks for the current temperature
 - "Qual é a umidade?" -> Asks for the current humidity
