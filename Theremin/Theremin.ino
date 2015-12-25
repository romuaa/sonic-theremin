/*
  Pitch follower

 Plays a pitch that changes based on a changing analog input

 circuit:
 * 8-ohm speaker on digital pin 9
 * ultrasonic sensor
 * couple of resistors

 created 21 Jan 2010
 modified 31 May 2012
 by Tom Igoe, with suggestion from Michael Flynn
 Hacked for own purposes 2015 by Aapo Romu
This example code is in the public domain.

Original example for photoresistor:
 http://www.arduino.cc/en/Tutorial/Tone2

 */

#define ECHOPIN 11
#define TRIGPIN 12

void setup() {
  // initialize serial communications (for feeding python ui):
  Serial.begin(19200);
  pinMode(ECHOPIN, INPUT);
  pinMode(TRIGPIN, OUTPUT);
}

void loop() {
  // Start ranging
  digitalWrite(TRIGPIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIGPIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIGPIN, LOW);

  float sensorValue = pulseIn(ECHOPIN, HIGH);
  float pitch=(sensorValue/2)+100;

  // play the pitch:
  if(pitch > 40 && pitch < 3000) {
    Serial.print(sensorValue, DEC);
    Serial.print(",");
    Serial.println(pitch, DEC);

    noTone(9);
    tone(9, pitch, 50);
  } else {
    noTone(9);
  }
  delay(5);        // delay in between reads for stability
}


