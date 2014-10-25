/* EEPROM Data.side
*/

#include "simpletools.h"                      // Include simpletools header    .
#include "abdrive.h"
#include "ping.h"

int main(void)                                // main function
{
  int distance;
  int addr = 32769;                           // Pick EEPROM base address. 
  
  int side = 1;                       // 0=Left, 1=Right
  
  freqout(4, 1000, 3000); //pin, duration, frequency
  
  switch(side)
  {
	case 0:
		high(26);
		//drive_goto(256, 256); //forward 4 wheel turns
		pause(200);
		drive_goto(-25, 26); //90deg Left turn
		break;
	case 1:
		high(27);
		//drive_goto(256, 256); //forward 4 wheel turns
		pause(200);
		drive_goto(26, -25); //90deg Right turn
		break;
	}
	while(1);
}

