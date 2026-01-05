/*
 * Raspberry Pi Pico - nRF24L01 Transmitter
 * 
 * Libraries required:
 * - RF24 by TMRh20
 * 
 * Pinout (Default SPI0):
 * - MISO: GP4 (Pin 6)
 * - CSN:  GP5 (Pin 7)  <-- User Configurable
 * - SCK:  GP2 (Pin 4)
 * - MOSI: GP3 (Pin 5)
 * - CE:   GP6 (Pin 9)  <-- User Configurable
 * - VCC:  3.3V
 * - GND:  GND
 */

#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
#include <printf.h> // Required for printf support

// Pin Definitions
#define CE_PIN  6
#define CSN_PIN 5

// Radio Pipe Address
const byte address[6] = "00001";

RF24 radio(CE_PIN, CSN_PIN);

void setup() {
  Serial.begin(115200);
  while (!Serial) delay(10); // Wait for serial connection so we don't miss messages

  Serial.println(F("\n\n--- Pico nRF24L01 Transmitter ---"));

  // Initialize printf for radio.printDetails()
  printf_begin();

  // CRITICAL: Configure SPI pins to match the wiring!
  // Default SPI pins might be different (often GP16-19), so we force them here.
  SPI.setRX(4);  // MISO
  SPI.setTX(3);  // MOSI
  SPI.setSCK(2); // SCK
  SPI.begin();

  if (!radio.begin()) {
    Serial.println(F("Radio hardware not responding!"));
    Serial.println(F("CHECK WIRING: VCC(3.3V), GND, CE, CSN, SCK, MOSI, MISO"));
    while (1) {
      // Blink LED to indicate error
      // digitalWrite(LED_BUILTIN, !digitalRead(LED_BUILTIN));
      delay(1000);
    } 
  }

  if (!radio.isChipConnected()) {
    Serial.println(F("Radio chip not detected (isChipConnected failed)."));
  } else {
    Serial.println(F("Radio chip detected successfully."));
  }

  radio.openWritingPipe(address);
  
  // OPTIMIZATION: Improve reliability
  radio.setPALevel(RF24_PA_LOW); 
  radio.setDataRate(RF24_250KBPS); // Lower speed = longer range/better reliability
  radio.setChannel(76);            // Moved to Channel 76 based on scan
  radio.setRetries(15, 15);        // Max delay between retries, max retries

  radio.stopListening(); // Set as transmitter

  Serial.println(F("Radio Configuration:"));
  radio.printDetails(); // Prints full register dump to Serial
  Serial.println(F("---------------------------------"));
  Serial.println(F("Ready. Type a command and press Enter."));
}

void loop() {
  if (Serial.available()) {
    String input = Serial.readStringUntil('\n');
    input.trim(); // Remove whitespace/newlines

    if (input.length() > 0) {
      Serial.print(F("Sending: ["));
      Serial.print(input);
      Serial.print(F("] ... "));

      // Convert String to char array
      char text[32];
      input.toCharArray(text, 32);

      bool report = radio.write(&text, sizeof(text));

      if (report) {
        Serial.println(F("OK"));
      } else {
        Serial.println(F("FAILED (No Ack or Timeout)"));
      }
    }
  }
}
