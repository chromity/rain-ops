
int sensorPin = A0;    // select the input pin for the potentiometer
int sensorValue = 0;  // variable to store the value coming from the sensor

void setup() {
  // declare the ledPin as an OUTPUT:
  Serial.begin(9600);
}

void loop() {
  // read the value from the sensor:

  sensorValue = 0;
  for(int i = 0; i < 100; i++) {
    sensorValue += analogRead(sensorPin);
    delay(10);
  }
  
  Serial.println(sensorValue / 100);
}
