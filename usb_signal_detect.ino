void setup() {
  Serial.begin (9600);
  pinMode(9,OUTPUT);
}

void loop() {
  int data = Serial.read();
 
  if (data == '1'){
    analogWrite(9, 170);
    delay(300);
    digitalWrite(9,LOW);
  }

}
