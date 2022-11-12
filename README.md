# wifi-qrcode-generator

Generates QR Code to join wifi networks

## Installation

```
python -m pip install wifi-qrcode-generator
```

- Requires Python 3.9 or later

## Usage

```sh
wifi-qrcode-generator [-h] --output OUTPUT --ssid SSID --password PASSWORD --alg {WEP,WPA,nopass} [--random-password] [--verbose]

options:
  -h, --help               show this help message and exit
  --output OUTPUT          The PNG file that will store the QR Code
  --ssid SSID              The SSID of the network
  --password PASSWORD      The password of the network
  --alg {WEP,WPA,nopass}   The authentication algorithm
  --random-password        Generate a random password for the network
  --verbose                Print verbose information
```
