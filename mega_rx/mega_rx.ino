/*
 * Arduino Mega - nRF24L01 Receiver
 * 
 * Libraries required:
 * - RF24 by TMRh20
 * 
 * Pinout (Standard Mega SPI):
 * - MISO: 50
 * - MOSI: 51
 * - SCK:  52
 * - CE:   7   <-- User Configurable
 * - CSN:  8   <-- User Configurable
 * - VCC:  3.3V (Do NOT connect to 5V!)
 * - GND:  GND
 */

#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
#include <printf.h> // Required for printf support

// Pin Definitions
#define CE_PIN  7
#define CSN_PIN 8

// Radio Pipe Address
const byte address[6] = "00001";

RF24 radio(CE_PIN, CSN_PIN);

void setup() {
  Serial.begin(115200);
  while (!Serial) delay(10); 

  Serial.println(F("\n\n--- Mega nRF24L01 Receiver ---"));
  printf_begin();

  if (!radio.begin()) {
    Serial.println(F("Radio hardware not responding!"));
    Serial.println(F("CHECK WIRING: VCC(3.3V), GND, CE(7), CSN(8), SCK(52), MOSI(51), MISO(50)"));
    while (1) {} // Hold in infinite loop
  }

  if (!radio.isChipConnected()) {
    Serial.println(F("Radio chip not detected (isChipConnected failed)."));
  } else {
    Serial.println(F("Radio chip detected successfully."));
  }

  radio.openReadingPipe(0, address);
  
  // OPTIMIZATION: Improve reliability
  radio.setPALevel(RF24_PA_LOW);
  radio.setDataRate(RF24_250KBPS); // Must match Transmitter!
  radio.setChannel(76);            // Must match Transmitter!
  
  radio.startListening(); // Set as receiver

  Serial.println(F("Radio Configuration:"));
  radio.printDetails();
  Serial.println(F("---------------------------------"));
  Serial.println(F("Mega Receiver Ready. Waiting for data..."));
}

void loop() {
  if (radio.available()) {
    char text[32] = "";
    radio.read(&text, sizeof(text));
    
    Serial.print(F("Received: "));
    Serial.println(text);
    
    // Add your command handling logic here
    // if (strcmp(text, "LED_ON") == 0) { ... }

    if(strcmp(text, "test") == 0){
      Serial.println(F("Test"));
    }
    else{
      Serial.println(F("Unknown command"));
    }
  }
}
