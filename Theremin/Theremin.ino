/*
  Pitch follower

 Plays a pitch that changes based on a changing analog input

 circuit:
 * 8-ohm speaker on digital pin 9
 * photoresistor on analog 0 to 5V
 * 4.7K resistor on analog 0 to ground

 created 21 Jan 2010
 modified 31 May 2012
 by Tom Igoe, with suggestion from Michael Flynn

This example code is in the public domain.

 http://www.arduino.cc/en/Tutorial/Tone2

 */

#define ECHOPIN 11
#define TRIGPIN 12

void setup() {
  // initialize serial communications (for debugging only):
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

  float distance = pulseIn(ECHOPIN, HIGH);
  distance=distance/2+100;
  
  //Serial.println(" cm");
  
  
  
  //int sensorReading = analogRead(A0);
  // print the sensor reading so you know its range
  //Serial.println(sensorReading);
  // map the analog input range (in this case, 400 - 1000 from the photoresistor)
  // to the output pitch range (120 - 1500Hz)
  // change the minimum and maximum input numbers below
  // depending on the range your sensor's giving:
  //int thisPitch = map(distance, 400, 1000, 120, 1500);
  //Serial.print("D: ");
  //Serial.print(distance);
  //Serial.print(" P: ");
  //Serial.println(thisPitch);
  // play the pitch:
  if(distance > 40 && distance < 3000) {
    noTone(9);
    tone(9, distance, 50);
  } else {
    noTone(9);
  }
  delay(5);        // delay in between reads for stability
}






