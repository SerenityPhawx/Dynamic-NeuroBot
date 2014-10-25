/*
 * */

#include "simpletools.h"
#include "abdrive.h"
#include "ping.h"

int distance;

int main()
{
  freqout(4, 1000, 3000);  //pin, duration, frequency

  while(1)     //endless loop
  {
      high(26);  //set P26 I/O pin high
      pause(100);  //wait 1/10 second
      low(26);   //set P26 low
      pause(100);

      //drive_pins(14, 15, 12, 13); 

      drive_goto(100, 100); //forward
      pause(100);
      drive_goto(-100, -100);  //backward
      pause(100);
      drive_speed(0, 0);
    }
}
