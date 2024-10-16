/*
  Controlling a servo position using a potentiometer (variable resistor)
  by Michal Rinott <http://people.interaction-ivrea.it/m.rinott>

  modified on 8 Nov 2013
  by Scott Fitzgerald
  http://www.arduino.cc/en/Tutorial/Knob
*/

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
               //count = 0;
               int potpin = A0;  // analog pin used to connect the potentiometer
int val;    // variable to read the value from the analog pin

void setup() {
  myservo.attach(4);  // attaches the servo on pin 9 to the servo object
  Serial.begin(9600);
}

void loop() {
  val = analogRead(potpin);
  //Serial.println(val);// reads the value of the potentiometer (value between 0 and 1023)
  if (val > 20) {
    //  val = map(val, 50, 100, 60, 70);
    //count +=1
    avg = (avg + val) / 2; // scale it for use with the servo (value between 0 and 180)
    if (pavg > avg + avgDiff || pavg < avg - avgDiff) {
      servoVal = map(pavg, 10, 120, servoMin, servoMax);
      servoVal = int(servoVal + (servoVal-pservo)/1.5);
      if( servoVal > servoMax){
        servoVal = servoMax;
      }
      if (servoVal < servoMin){
        servoVal = servoMin;
      }
      myservo.write(servoVal);
      pservo = servoVal;
      pavg = avg;
    }

    Serial.println(pavg);
  }// sets the servo position according to the scaled value
  delay(15);                           // waits for the servo to get there
}
