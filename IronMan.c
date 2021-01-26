#include <wiringPi.h>

#define GPIO2 3;
int main (void)
{
  wiringPiSetup () ;
  pinMode (GPIO2, OUTPUT) ;
  for (;;)
  {
    digitalWrite (GPIO2, HIGH) ; delay (500) ;
    digitalWrite (GPIO2,  LOW) ; delay (500) ;
  }
  return 0 ;
}