#include <Servo.h>

Servo myservo;  // create servo object to control a servo
int avg = 0;
int pavg = 0 ;
int count = 0;
int avgDiff = 15;
int pservo = 0;
int servoVal = 0;
int servoMax = 90;
int servoMin = 65;
const int servoDivLen = 5;
int servodiv[servoDivLen];
int diffs[servoDivLen];
int diff = 1000;
int tempServo = 0;

const int numReadings = 5;
int readings[numReadings];  // the readings from the analog input
int readIndex = 0;          // the index of the current reading
int total = 0;              // the running total
int average = 0;


int audio = A0;

int val;    // variable to read the value from the analog pin
int minVal = 1000;
int maxVal = 1;

void setup() {
  myservo.attach(4);  // attaches the servo on pin 9 to the servo object
  Serial.begin(9600);

  for (int thisReading = 0; thisReading < numReadings; thisReading++) {
    readings[thisReading] = 0;
  }

  for (int i = 0; i < servoDivLen; i++) {
    if (i == 0) {
      servodiv[i] = servoMin;
    }
    else if (i == servoDivLen - 1) {
      servodiv[i] = servoMax;
    }
    else {
      servodiv[i] = servoMin + ((servoMax - servoMin) / (servoDivLen - i));
    }
  }
  for ( int i = 0; i < servoDivLen; i++) {
    Serial.println(servodiv[i]);
  }

}

void loop() {
  total = total - readings[readIndex];
  // read from the sensor:
  readings[readIndex] = analogRead(audio);
  // add the reading to the total:
  total = total + readings[readIndex];

  readIndex = readIndex + 1;

  if (readIndex >= numReadings) {
    readIndex = 0;
  }

  // calculate the average:
  servoVal = total / numReadings;
  if (servoVal < minVal) {
    minVal = servoVal;
  }
  if (servoVal > maxVal) {
    maxVal = servoVal;
  }
  Serial.println(servoVal);
  servoVal = map(servoVal, 650, 720, servoMin  , servoMax);
//  for (int i = 0; i < servoDivLen; i++) {
//    diffs[i] = abs(servoVal - servodiv[i]);
//    if (diffs[i] < diff) {
//      diff = diffs[i];
//      tempServo = servodiv[i];
//    }
//  }
//  diff = 1000;
//  servoVal = tempServo;
  if ( servoVal > servoMax) {
    servoVal = servoMax;
  }
  if (servoVal < servoMin) {
    servoVal = servoMin;
  }
  //Serial.println(servoVal);
  myservo.write(servoVal);
  delay(10);
}
