/*
  MLX90393 Magnetometer Example Code
  By: Nathan Seidle
  SparkFun Electronics
  Date: February 6th, 2017
  License: This code is public domain but you buy me a beer if you use this and we meet someday (Beerware license).

  Read the mag fields on three XYZ axis

  Hardware Connections (Breakoutboard to Arduino):
  3.3V = 3.3V
  GND = GND
  SDA = A4
  SCL = A5

  Serial.print it out at 9600 baud to serial monitor.
*/

#include <Wire.h>
#include <MLX90393.h> //From https://github.com/tedyapo/arduino-MLX90393 by Theodore Yapo

MLX90393 mlx;
MLX90393::txyz data; //Create a structure, called data, of four floats (t, x, y, and z)
char buffer[50];

void setup()
{
  Serial.begin(9600);
  Wire.begin();
  mlx.begin(0); //Assumes I2C jumpers are GND. No DRDY pin used.
  mlx.setGainSel(7);
  mlx.setResolution(0, 0, 0); //x, y, z
  mlx.setOverSampling(0);
  mlx.setDigitalFiltering(4);
  mlx.setHallConf(0xC);
  Serial.println(7777777);
  delay(20);
}

void loop()
{
  mlx.readData(data); //Read the values from the sensor
  sprintf(buffer,"%d\t%d\t%d",int(data.x),int(data.y),int(data.z));
  Serial.println(buffer);
 
  delay(20);
}
