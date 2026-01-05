import serial
import time
#testing components
# Configuration

SERIAL_PORT = 'COM6'  # REPLACE WITH YOUR PICO'S COM PORT
BAUD_RATE = 115200

def main():
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        print(f"Connected to {SERIAL_PORT} at {BAUD_RATE} baud.")
        time.sleep(2) # Wait for connection to settle

        print("Type a command to send (or 'exit' to quit):")
        
        while True:
            command = input("> ")
            if command.lower() == 'exit':
                break
            
            # Send command
            ser.write((command + '\n').encode('utf-8'))
            print(f"Sent: {command}")

            # Optional: Read response if Pico sends one back
            # if ser.in_waiting > 0:
            #     response = ser.readline().decode('utf-8').strip()
            #     print(f"Received: {response}")

    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        if 'ser' in locals() and ser.is_open:
            ser.close()
            print("Serial port closed.")

if __name__ == "__main__":
    main()
