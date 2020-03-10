# smartsrmiot

## Tasks:
* Python Script to interface the RFID scanner and store it locally in a csv file along with timestamp
* Shell Script to read as soon as a response is recorded and create a JSON file
* Shell Script to check connection and send the file to remote server
* Database Design (My SQL)
* Setting up Apache Server in Ubuntu VM
## Hardware used:
- Raspberry Pi 4
- RC532 NFC Sensor

## Configure the Rasperry Pi4:

- Make sure the Rasbian distro is up-to-date:
  ```
  sudo apt-get update
  sudo apt-get upgrade
  ```
- Install the following packages
  ```
  sudo apt-get install build-essential git python3-dev python3-pip python3-smbus
  ```
## Interface the RFID RC522 Reader:

| RFID RC522 Reader  | RaspberryPi4 |
| ------------- | ------------- |
| SDA  | GPIO8 (Physical Pin 24)  |
| SCK  | GPIO11 (Physical Pin 23) |
| MOSI | GPIO10 (Physical Pin 19) |
| MISO | GPIO9 (Physical Pin 21)  |
| GND  | Ground (Physical Pin 6)  |
| RST  | GPIO25 (Physical Pin 22)  |
| 3.3V | 3v3 (Physical Pin 1) |

![Raspberry Pi 4](/images/raspberrypi4._gpio_pins.png)
![RC522 RFID Sensor](/images/rfid_rc522.jpg)


