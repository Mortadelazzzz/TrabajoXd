int LV1 = 41; // LUZ VERDE
int LV2 = 20;
int LR1 = 39; // LUZ ROJA
int LR2 = 22;
int BU1 = 43; // BUZZER
int BU2 = 24;
int ONOFF = 45;
int ZERO = 47;
int EXTRA = 49;

void setup() {

  Serial.begin(9600);

  pinMode(LV1, OUTPUT);
  digitalWrite(LV1, HIGH);

  pinMode(LV2, OUTPUT);
  digitalWrite(LV2, HIGH);

  pinMode(LR1, OUTPUT);
  digitalWrite(LR1, HIGH);

  pinMode(LR2, OUTPUT);
  digitalWrite(LR2, HIGH);

  pinMode(BU1, OUTPUT);
  digitalWrite(BU1, HIGH);

  pinMode(BU2, OUTPUT);
  digitalWrite(BU2, HIGH);

  pinMode(ONOFF, OUTPUT);
  digitalWrite(ONOFF, HIGH);

  pinMode(ZERO, OUTPUT);
  digitalWrite(ZERO, HIGH);

  pinMode(EXTRA, OUTPUT);
  digitalWrite(EXTRA, HIGH);
  
}

void loop(){

  if (Serial.available()){
    // Lectura de caracteres
    int val = Serial.read();

    if (val == 'a') {
      digitalWrite(LV1, LOW);
    }

    else if (val == 'b') {
      digitalWrite(LV2, LOW);
    }

    else if (val == 'c') {
      digitalWrite(LR1, LOW);
    }

    else if (val == 'd') {
      digitalWrite(LR2, LOW);
    }

    else if (val == 'e'){
      digitalWrite(LV1, HIGH);
    }

    else if (val == 'f'){
      digitalWrite(LV2, HIGH);
    }

    else if (val == 'g'){
      digitalWrite(LR1, HIGH);
    }

    else if (val == 'h'){
      digitalWrite(LR2, HIGH);
    }

    else if (val == 'i'){
      digitalWrite(BU1, LOW);
    }

    else if (val == 'j'){
      digitalWrite(BU2, LOW);
    }

    else if (val == 'k'){
      digitalWrite(BU1, HIGH);
    }

    else if (val == 'l'){
      digitalWrite(BU2, HIGH);
    }

    else if (val == 'x'){
      digitalWrite(ONOFF, LOW);
      delay(2000);
      digitalWrite(ONOFF, HIGH);
    }

    else if (val == 'z'){
      digitalWrite(ZERO, LOW);
      delay(500);
      digitalWrite(ZERO, HIGH);
    }

    else if (val == 'v') {
      digitalWrite(EXTRA, LOW);
    }

    else if (val == 'w'){
      digitalWrite(EXTRA, HIGH);
    }

    else{
      Serial.flush();
    }   
  }

};