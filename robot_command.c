/* EEPROM Data.side
 * */

#include "simpletools.h"                      // Include simpletools header    .
#include "abdrive.h"
#include "ping.h"

int main(void)                                // main function
{
  int distance;
  int addr = 32769;                           // Pick EEPROM base address. 
  int side = 1;                               // 0=Left, 1=Right
  int exit = 0;

  while(!exit) {
    print("Enter direction (0 - forward, 1 - backward, 2 - Exit): ");  // User prompt 
    scan("%d\n", &side);

    freqout(4, 250, 3000); //pin, duration, frequency

    switch(side)
    {

      case 0: // forward with turn
        high(26);
        pause(300);
        drive_speed(-25, 26); //90deg Left turn
        pause(1000);
        drive_speed(0, 0);
        break;
      case 1: // backward with turn
        high(27);
        pause(300);
        drive_speed(26, -25); //90deg Right turn
        pause(1000);
        drive_speed(0, 0);
        break;
      case 2:
        print("Exit");
        exit = 1;
    }
  }
  print("\xff\x00\x00");
}

