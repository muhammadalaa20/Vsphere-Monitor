
# Vsphere Monitor

A desktop application using Electron To monitor my Server's approximate temprature instead of manually checking or buying an expensive sensor.

The app can send messages if the tempratures exceeded a certain number and also play an alarm while sending the messages.

```
This code only includes the py script and the json file.
```

## Screenshots

![App Screenshot](https://raw.githubusercontent.com/muhammadalaa20/Vsphere-Monitor/refs/heads/main/screenshot.png)

## Tech

```
Python
```

## Installation

Install with pip

```bash
  pip install pyautogui pywhatkit requests pyvmomi urllib3
```
    
## DEMO

```
{
    "System Board 1 Exhaust Temp": {
        "value": 24.0,
        "units": "degrees C"
    },
    "System Board 1 Inlet Temp": {
        "value": 17.0,
        "units": "degrees C"
    },
    "Processor 2 Temp": {
        "value": 34.0,
        "units": "degrees C"
    },
    "Processor 1 Temp": {
        "value": 29.0,
        "units": "degrees C"
    }
}
```


## Authors

- [@muhammadalaa20](https://github.com/muhammadalaa20)
