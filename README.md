
# Vsphere Monitor

A desktop application using Electron To monitor my Server's approximate temprature instead of manually checking or buying an expensive sensor.

The app can send messages if the temprature is more that a certain number and also play an alarm wille sending the messages.

```
This code only includes the py script and the json file.
```


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

## DEMO

![App Demo]([https://github.com/muhammadalaa20/DailyReports/blob/main/dailyreports.gif](https://github.com/muhammadalaa20/Vsphere-Monitor/blob/main/screenshot.png))

## Authors

- [@muhammadalaa20](https://github.com/muhammadalaa20)
