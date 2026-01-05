/*
 * nRF24L01 Scanner
 * 
 * This sketch scans all channels (0-127) and displays the signal level.
 * Use this on the MEGA to see if the Pico is actually transmitting.
 */
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
#include <printf.h>

// Mega Pins
#define CE_PIN  7
#define CSN_PIN 8

RF24 radio(CE_PIN, CSN_PIN);

const uint8_t num_channels = 128;
uint8_t values[num_channels];

void setup() {
  Serial.begin(115200);
  printf_begin();
  Serial.println(F("\n\n--- nRF24L01 Scanner ---"));

  if (!radio.begin()) {
    Serial.println(F("Radio hardware not responding!"));
    while (1) {}
  }

  radio.setAutoAck(false);

  // Scan all channels
  Serial.println(F("Scanning... (Hex 0-F indicates signal strength)"));
  Serial.println(F("   0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567"));
}

void loop() {
  // Clear measurement storage
  memset(values, 0, sizeof(values));

  // Scan channels 0..127
  for (int k = 0; k < 50; ++k) { // Repeat 50 times to catch intermittent signals
    for (int i = 0; i < num_channels; ++i) {
      radio.setChannel(i);
      radio.startListening();
      delayMicroseconds(128);
      radio.stopListening();
      if (radio.testCarrier()) {
        ++values[i];
      }
    }
  }

  // Print results
  for (int i = 0; i < num_channels; ++i) {
    if (values[i] > 0)
      Serial.print(min(0xF, (values[i] + 1) / 2), HEX);
    else
      Serial.print(F("-"));
  }
  Serial.println(F(""));
}
