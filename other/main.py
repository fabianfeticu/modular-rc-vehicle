import tkinter as tk
import serial
import time
#most basic version of my project not used anymore
class GUI:
    def __init__(self, root):
        self.root = root
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()
        self.root.title("nRF24L01 Raw AT Command GUI")
        self.root.geometry(f"{self.screen_width}x{self.screen_height}")
        self.root.config(bg="light blue")

        try:
            # Set the COM port and 9600 baud rate (matching your latest code)
            self.ser = serial.Serial('COM5', 11520, timeout=1) 
            time.sleep(2)  # Wait for connection to establish
            print("Serial port opened successfully.")

            # --- Explicitly Configure the NRF Module and read responses ---
            print("\n--- Sending Config Commands ---")
            self.send_and_read_response("AT+ADDR=E8E8F0F0E1\r\n") 
            self.send_and_read_response("AT+RATE=2\r\n")             
            self.send_and_read_response("AT+CH=76\r\n")             
            self.send_and_read_response("AT+PWR=2\r\n")             
            print("--- Config Commands Sent ---")
            # ------------------------------------------

        except serial.SerialException as e:
            print(f"Failed to open serial port: {e}")
            self.ser = None
        
        self.create_button()

    def send_and_read_response(self, command_string):
        """Sends command, reads the response (e.g., OK or ERROR) and prints it."""
        if self.ser and self.ser.is_open:
            try:
                self.ser.write(command_string.encode('utf-8'))
                print(f"Sent: {command_string.strip()}")
                time.sleep(0.1) # Give module time to respond

                # Read all available response data from the serial buffer
                while self.ser.in_waiting > 0:
                    response_line = self.ser.readline().decode('utf-8').strip()
                    if response_line:
                        print(f"Received Response: {response_line}")
            except Exception as e:
                print(f"Serial write/read error: {e}")
        else:
            print(f"Port closed, command failed: {command_string.strip()}")

    def btn_pressed(self, n):
        # Determine the single-character payload ('R', 'G', 'B', 'O')
        if n == 0:
            payload = 'O' 
        elif n == 1:
            payload = 'R'
        elif n == 2:
            payload = 'G'
        else:
            payload = 'B'
        
        # Format the command: AT+TX=<length>,<data>\r\n
        command = f"AT+TX=1,{payload}\r\n"
        # Use the standard send function for transmissions
        self.send_and_read_response(command)

    def create_button(self):
        self.frame = tk.Frame(self.root, bg="#2ca8e7")
        self.frame.pack(pady=50)

        self.red = tk.Button(self.frame, text="Send Red (R)", bg="red", relief="raised", fg="gold", command=lambda: self.btn_pressed(1), width=25, height=3)
        self.red.pack(padx=3,pady=10)

        self.green = tk.Button(self.frame, text="Send Green (G)",  bg="green", relief="raised", fg="gold", command=lambda: self.btn_pressed(2), width=25, height=3)
        self.green.pack(padx=3,pady=10)

        self.blue = tk.Button(self.frame, text="Send Blue (B)",  bg="blue", relief="raised", fg="gold", command=lambda: self.btn_pressed(3), width=25, height=3)
        self.blue.pack(padx=3,pady=10)

        self.off = tk.Button(self.frame, text="Send Off (O)",  bg="grey", relief="raised", fg="gold", command=lambda: self.btn_pressed(0), width=25, height=3)
        self.off.pack(padx=3,pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()

