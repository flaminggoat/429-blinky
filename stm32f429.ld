ENTRY(Reset_Handler)

_estack = 0x2002FFFF;    /* end of RAM */
 
MEMORY
{
        FLASH (rx)      : ORIGIN = 0x8000000, LENGTH = 2048K
        RAM (xrw)       : ORIGIN = 0x20000000, LENGTH = 192K
        CCMRAM (rw)     : ORIGIN = 0x10000000, LENGTH = 64K
}
 
REGION_ALIAS("REGION_TEXT", FLASH);
REGION_ALIAS("REGION_RODATA", FLASH);
REGION_ALIAS("REGION_DATA", RAM);
REGION_ALIAS("REGION_BSS", RAM);
 
SECTIONS
{
        .text :
        {
                . = ALIGN(4);
                *(.text)
                *(.text*)
 
                . = ALIGN(4);
                _etext = .;
                _sidata = _etext;
        } > REGION_TEXT
 
        .rodata :
        {
                . = ALIGN(4);
                *(.rodata)
                *(.rodata*)
 
                . = ALIGN(4);
                rodata_end = .;
        } > REGION_RODATA
 
        .data :
        {
                . = ALIGN(4);
                _sdata = .;
                *(.data)
                *(.data*)
 
                . = ALIGN(4);
                _edata = .;
        } > REGION_DATA
 
        .bss :
        {
                . = ALIGN(4);
                _sbss = .;
                __bss_start__ = _sbss;
                *(.bss)
                *(.bss*)
 
                . = ALIGN(4);
                _ebss = .;
                __bss_end__ = _ebss;
        } > REGION_BSS
 
        .heap_stack :
        {
                . = ALIGN(4);
                PROVIDE ( end = . );
                PROVIDE ( _end = . );
                . = ALIGN(4);
        }
 
        .ccmram :
        {
                . = ALIGN(4);
                _sccmram = .;
                *(.ccmram)
                *(.ccmram*)
 
                . = ALIGN(4);
                _eccmram = .;
        } > CCMRAM
 
}