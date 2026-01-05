///uint8_t data3 = 0b11100110; uint8_t data2 = 0b00101000; uint8_t data1 = 0b00100000; digitalWrite(lastPin,HIGH); left up
///uint8_t data3 = 0b00100011; uint8_t data2 = 0b10101010; uint8_t data1 = 0b01000010; digitalWrite(lastPin,LOW);  left
///uint8_t data3 = 0b00111000; uint8_t data2 = 0b11001010; uint8_t data1 = 0b10001000; digitalWrite(lastPin,LOW);  left down
///uint8_t data3 = 0b00100000; uint8_t data2 = 0b10111110; uint8_t data1 = 0b00100010; digitalWrite(lastPin,LOW);  down
///uint8_t data3 = 0b10000010; uint8_t data2 = 0b00001010; uint8_t data1 = 0b00110011; digitalWrite(lastPin,HIGH); down right
///uint8_t data3 = 0b00100001; uint8_t data2 = 0b00101010; uint8_t data1 = 0b11100010; digitalWrite(lastPin,LOW);  right
///uint8_t data3 = 0b00001000; uint8_t data2 = 0b10101001; uint8_t data1 = 0b10001110; digitalWrite(lastPin,LOW);  right up
///uint8_t data3 = 0b00100010; uint8_t data2 = 0b00111110; uint8_t data1 = 0b10000010; digitalWrite(lastPin,LOW);  up


const uint8_t dat3[] = {0b00000000, 0b11100110, 0b00100011, 0b00111000, 0b00100000, 0b10000010, 0b00100001, 0b00001000, 0b00100010, 0b11111111,0b10001010, 0b01010111, 0b10101000};
const uint8_t dat2[] = {0b00000000, 0b00101000, 0b10101010, 0b11001010, 0b10111110, 0b00001010, 0b00101010, 0b10101001, 0b00111110, 0b11111111,0b10001000, 0b11010101, 0b00101010};
const uint8_t dat1[] = {0b00000000, 0b00100000, 0b01000010, 0b10001000, 0b00100010, 0b00110011, 0b11100010, 0b10001110, 0b10000010, 0b11111111,0b10101000, 0b11110101, 0b00001010};
const bool lastPinForPattern[] = {
  false, 
  true,  
  false, 
  false, 
  false, 
  true,  
  false, 
  false, 
  false, 
  true,
  true,
  false,
  true
};

int latchPin = 24;
int clockPin = 23;
int dataPin = 22;
int lastPin = 25;
int i = 1;
const unsigned long blinkInterval = 50; 
bool blinkState = false;

int state = 0;   
unsigned long previousMillis = 0;
int index = 0;
int blinktime=0;



void display(uint8_t d3, uint8_t d2, uint8_t d1){
  digitalWrite(latchPin, LOW);
  shiftOut(dataPin, clockPin, LSBFIRST, d3); 
  shiftOut(dataPin, clockPin, LSBFIRST, d2); 
  shiftOut(dataPin, clockPin, LSBFIRST, d1);
  digitalWrite(latchPin, HIGH);
}


void setup() {
  Serial.begin(115200);
  pinMode(lastPin, OUTPUT); 
  pinMode(latchPin, OUTPUT);
  pinMode(dataPin, OUTPUT);
  pinMode(clockPin, OUTPUT);
}



void loop() {

  
  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n'); 
    input.trim(); 
    int spaceIndex = input.indexOf(' '); 

    if (spaceIndex != -1) {
      String firstValueStr = input.substring(0, spaceIndex);
      String secondValueStr = input.substring(spaceIndex + 1);

      state = firstValueStr.toInt();
      blinktime = secondValueStr.toInt();

      Serial.print("First: "); Serial.println(state);
      Serial.print("Second: "); Serial.println(blinktime);
    }
    else{
      state = input.toInt();
      blinktime = 0;
    }
  }




  if (state < 0 || state >= (int)(sizeof(dat1) / sizeof(dat1[0]))) return;

  if (blinktime != 0) {

    unsigned long currentMillis = millis();

    if (currentMillis - previousMillis >= blinktime) {
      previousMillis = currentMillis;
      blinkState = !blinkState;

      bool lastOn = lastPinForPattern[state];

      if (blinkState) {
        display(dat3[state], dat2[state], dat1[state]);
        digitalWrite(lastPin, lastOn ? HIGH : LOW);
      } 
      else {
        display(0, 0, 0);
        digitalWrite(lastPin, LOW);
      }
    }
  }
  else {
    display(dat3[state], dat2[state], dat1[state]);
    digitalWrite(lastPin, lastPinForPattern[state] ? HIGH : LOW);
  }
}


