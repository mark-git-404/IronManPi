#include <wiringPi.h>

int main (void)
{
  wiringPiSetup();
  pinMode(3, OUTPUT);
  for(i = 1; i < 11; ++i)
  {
    digitalWrite(3, HIGH); 
    delay(500);
    digitalWrite(3, LOW);
    delay(500);
  }
  return 0 ;
}