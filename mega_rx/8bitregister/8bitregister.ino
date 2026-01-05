int latchPin = 24;
int clockPin = 23;
int dataPin = 22;
int i = 0;

void display(uint8_t pattern) {
  digitalWrite(latchPin, LOW); 
  shiftOut(dataPin, clockPin, LSBFIRST, pattern); 
  digitalWrite(latchPin, HIGH);  
}
void strobe(uint8_t ptn,int time){
  display(ptn);
  delay(time);
}

void setup() {
  Serial.begin(115200);
  pinMode(22, OUTPUT); 

  Serial.println("nr for pattern, 256 for strobe");
  pinMode(latchPin, OUTPUT);
  pinMode(dataPin, OUTPUT);
  pinMode(clockPin, OUTPUT);
}

void loop() {
  

  digitalWrite(latchPin, HIGH); 
  if (Serial.available() > 0) { 
    
    String inputString = Serial.readStringUntil('\n'); 
    int state = inputString.toInt();

    if (state>=0 && state<=255){

    uint8_t myData = state;
      

    digitalWrite(latchPin, LOW); 

  
    shiftOut(dataPin, clockPin, LSBFIRST, myData); 


    digitalWrite(latchPin, HIGH); 


      Serial.print("Showing pattern for "); 
      Serial.println(state);
    }
    else if (state==256){
       
      
       while(i<=100){
        if (i<=25 || (i>=30 && i<=55) || (i>=60 && i<=85)){
          strobe(85,50);
          strobe(170,50);
        }
        else {
          strobe(255,35);
          strobe(0,35);
        }
        i+=1;
       }
        
        

      i=0;
    }
    else{

      Serial.println("please give amount less than 255");
    }

  }
}