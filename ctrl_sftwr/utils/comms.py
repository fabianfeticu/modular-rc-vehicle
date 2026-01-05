import serial
import time

def send_serial(message):
    try:
       
        ser = serial.Serial('COM4', 115200, timeout=1) 
        
       
        time.sleep(2) 
        
       
        formatted_message = f"{message}\n"
        ser.write(formatted_message.encode('utf-8'))
        
        
        ser.close()
    except Exception as e:
        print(f"Error: {e}")