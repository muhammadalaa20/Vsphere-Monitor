import time
import pyautogui
import pywhatkit
import requests
from pyVim.connect import SmartConnect, Disconnect
import ssl
import json
import threading
from requests.auth import HTTPBasicAuth
from urllib3.exceptions import InsecureRequestWarning

# Suppress SSL warnings for self-signed certificates
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# vSphere connection details
server = '' # your vSphere server
username = '' # your vSphere username
password = '' # your vSphere password
host_ip = "" # the IP address of the host
json_file_path = 'temperature_readings.json'

# Phone numbers to send the message
phone_numbers = [
    "+201000000000",   # Phone number to send the message to.
]

# Function to establish a connection to vSphere
def connect_to_vsphere():
    s = ssl.create_default_context()
    s.check_hostname = False
    s.verify_mode = ssl.CERT_NONE
    try:
        connection = SmartConnect(host=host_ip, user='root', pwd='P@ssw0rd', sslContext=s)
        print("Connected to vSphere successfully.")
        return connection
    except Exception as e:
        print(f"Error connecting to vSphere: {e}")
        return None

# Function to retrieve temperature data
def get_temperature_data(connection):
    try:
        health = connection.content.searchIndex.FindByIp(ip=host_ip, vmSearch=False)
        
        if health:
            sensors = health.runtime.healthSystemRuntime.systemHealthInfo.numericSensorInfo
            readings = {}

            if not sensors:
                print("No sensor information available.")
                return False, None

            for i, sensor in enumerate(sensors):
                if sensor.sensorType == 'temperature':
                    temp = sensor.currentReading / 100
                    sensor_name = sensor.name
                    formatted_output = f"{sensor_name}: {temp:.1f} degrees C"
                    print(formatted_output)
                    readings[sensor_name] = {"value": temp, "units": "degrees C"}

            with open(json_file_path, 'w') as json_file:
                json.dump(readings, json_file, indent=4)

            first_sensor_name = list(readings.keys())[0] if readings else None
            first_sensor_reading = readings.get(first_sensor_name, {}).get('value') if first_sensor_name else None
            return True, first_sensor_reading
        else:
            print("No sensor information available.")
            return False, None

    except Exception as e:
        print(f"Error retrieving temperature data: {e}")
        return False, None

# Function to send sensor reading via WhatsApp
def send_sensor_reading(sensor_value):
    if sensor_value > 25:
        message = f"The room's Temperature is Approx. : {sensor_value} °C"
        
        for phone_number in phone_numbers:
            try:
                pywhatkit.sendwhatmsg_instantly(
                    phone_number,
                    message,
                    wait_time=10,
                    tab_close=False,
                    close_time=10
                )

                time.sleep(5)

                first_screen_center_x = 1230
                first_screen_center_y = 540

                pyautogui.moveTo(first_screen_center_x, first_screen_center_y, duration=1)
                pyautogui.click()
                
                time.sleep(2)
                pyautogui.press("enter")
                time.sleep(1)
                pyautogui.hotkey('ctrl', 'w')

                time.sleep(15)

            except Exception as e:
                print(f"An error occurred: {e}")
    else:
        print(f"Temperature is {sensor_value}°C, which is not greater than 25°C. No message sent.")

# Main loop
def main():
    connection = connect_to_vsphere()

    while True:
        if connection:
            success, first_sensor_reading = get_temperature_data(connection)
            
            if not success:
                print("Re-establishing connection due to error in fetching data.")
                Disconnect(connection)
                connection = connect_to_vsphere()
            
            if first_sensor_reading:
                send_sensor_reading(first_sensor_reading)
        else:
            print("Attempting to reconnect...")
            connection = connect_to_vsphere()
        
        time.sleep(5)

# Entry point
if __name__ == "__main__":
    main()
