#include "main.h"

void delay()
{
	for(uint32_t i=0x1FFFF; i>0; i--)
	{
		asm("mov r0,r0"); //NOP
	}
}

int main(void)
{
	//Enable GPIOG peripheral clock
	RCC_AHB1PeriphClockCmd(RCC_AHB1Periph_GPIOG, ENABLE);

	//Initialise GPIO pins for LEDs, PG13 and PG14
	GPIO_InitTypeDef g;
	g.GPIO_Pin = GPIO_Pin_13 | GPIO_Pin_14;
	g.GPIO_Mode = GPIO_Mode_OUT;
	g.GPIO_OType = GPIO_OType_PP;
	g.GPIO_Speed = GPIO_Low_Speed;
	g.GPIO_PuPd = GPIO_PuPd_NOPULL;
	GPIO_Init(GPIOG, &g);

	//Turn LED PG13 on
	GPIOG->BSRRL = GPIO_Pin_13;

	for(;;)
	{
		//Toggle both LEDs
		GPIOG->ODR ^= GPIO_Pin_13 | GPIO_Pin_14;

		delay();
	}
}
