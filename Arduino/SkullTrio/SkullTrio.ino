// Adafruit Motor shield library
// copyright Adafruit Industries LLC, 2009
// this code is public domain, enjoy!

#include <AFMotor.h>

AF_DCMotor skull1(1);
AF_DCMotor skull2(2);
AF_DCMotor skull3(3);

int threshold = 200;

const int a0 = A0;
const int a1 = A1;
const int a2 = A2;// Analog input pin that the potentiometer is attached to
const int analogOutPin = 9; // Analog output pin that the LED is attached to

int a0Out = 0;
int a2Out = 0;
int a1Out = 0; // value read from the pot
int outputValue = 0;        // value output to the PWM (analog out)

const int numReadings = 5;
int average = 0;
int average1 = 0;
int average2 = 0;

int readings1[numReadings];  // the readings from the analog input
// the index of the current reading
int total1 = 0;

int readings2[numReadings];  // the readings from the analog input
// the index of the current reading
int total2 = 0;


int readings[numReadings];  // the readings from the analog input
int readIndex = 0;          // the index of the current reading
int total = 0;



void setup() {
  Serial.begin(9600);           // set up Serial library at 9600 bps
  Serial.println("Motor test!");

  // turn on motor
  skull1.setSpeed(255);
  skull1.run(RELEASE);
  skull2.setSpeed(255);
  skull2.run(RELEASE);
  skull3.setSpeed(255);
  skull3.run(RELEASE);

  for (int thisReading = 0; thisReading < numReadings; thisReading++) {
    readings[thisReading] = 0;
    readings1[thisReading] = 0;
  }
}

void loop() {
  // read the analog in value:
  a0Out = analogRead(a0);
  a1Out = analogRead(a1);
  a2Out = analogRead(a2);
  // map it to the range of the analog out:
  //outputValue = map(sensorValue, 0, 1023, 0, 255);
  // change the analog out value:
  //analogWrite(analogOutPin, outputValue);

  total = total - readings[readIndex];
  // read from the sensor:
  readings[readIndex] = a0Out;
  // add the reading to the total:
  total = total + readings[readIndex];


  total1 = total1 - readings1[readIndex];
  // read from the sensor:
  readings1[readIndex] = a1Out;
  // add the reading to the total:
  total = total + readings[readIndex];

  total1 = total1 - readings1[readIndex];


  // read from the sensor:
  readings2[readIndex] = a2Out;
  // add the reading to the total:
  total2 = total2 + readings2[readIndex];
  // advance to the next position in the array:
  readIndex = readIndex + 1;

  // if we're at the end of the array...
  if (readIndex >= numReadings) {
    // ...wrap around to the beginning:
    readIndex = 0;
  }

  // calculate the average:
  average = total / numReadings;
  average1 = total1 / numReadings;
  average2 = total2 / numReadings;
  // print the results to the Serial Monitor:
  //Serial.print("sensor = ");
  Serial.print(average);
  Serial.print(",");
  Serial.print(average1);
  Serial.print(",");
  Serial.println(average2);
  //Serial.print("\t output = ");
  //Serial.println(outputValue);
//
//  if (a0Out > abs(threshold)) {
//    skull1.run(FORWARD);
//  }
//  else {
//    skull1.run(RELEASE);
//  }
//
//  if (a1Out > abs(threshold)) {
//    skull2.run(FORWARD);
////    skull1.run(FORWARD);
////    skull3.run(FORWARD);
//
//  }
//  else {
//    skull2.run(RELEASE);
////    skull1.run(RELEASE);
////    skull3.run(RELEASE);
//
//
//  }
//
//  if (a2Out > abs(threshold)) {
//    skull3.run(FORWARD);
//
//  }
//  else {
//    skull3.run(RELEASE);
//  }


  if (a0Out > abs(threshold)) {
    skull1.run(FORWARD);
  }
  else {
    skull1.run(RELEASE);
  }

  if (a1Out > abs(threshold)) {
    skull2.run(FORWARD);
//    skull1.run(FORWARD);
//    skull3.run(FORWARD);

  }
  else {
    skull2.run(RELEASE);
//    skull1.run(RELEASE);
//    skull3.run(RELEASE);


  }

  if (a2Out > abs(threshold)) {
    skull3.run(FORWARD);

  }
  else {
    skull3.run(RELEASE);
  }

  delay(3);
}
