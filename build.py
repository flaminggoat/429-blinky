import os, glob, time, shutil, sys

cc = 'arm-none-eabi-gcc'
cflags = "-DSTM32F429_439xx -DUSE_STDPERIPH_DRIVER -std=gnu99 -g -mlittle-endian -mthumb -mcpu=cortex-m4 "
cflags += "-lc --specs=nosys.specs -lnosys -TSTM32F439NI_FLASH.ld"

project = '429-blinky'
extension = 'elf'
build_dir = 'build'

sources = glob.glob('src/*.[cs]')

std_periph_src = '/home/theo/Embedded/STM32F4xx_DSP_StdPeriph_Lib_V1.5.1/Libraries/STM32F4xx_StdPeriph_Driver/src/'
sources.append(std_periph_src + 'stm32f4xx_gpio.c')
sources.append(std_periph_src + 'stm32f4xx_rcc.c')

include_dirs = ['inc', 
				'cow',
				'/home/theo/Embedded/STM32F4xx_DSP_StdPeriph_Lib_V1.5.1/Libraries/STM32F4xx_StdPeriph_Driver/inc',
				'/home/theo/Embedded/STM32F4xx_DSP_StdPeriph_Lib_V1.5.1/Libraries/CMSIS/Device/ST/STM32F4xx/Include',
				'/home/theo/Embedded/STM32F4xx_DSP_StdPeriph_Lib_V1.5.1/Libraries/CMSIS/Include/']

exe = build_dir + '/' + project + '.' + extension

class color:
	GREEN = '\033[92m'
	ENDC = '\033[0m'

def build() :
	#Create build directory if it does not exist
	if not os.path.exists(build_dir):
		os.makedirs(build_dir)

	#Check modification date of project executable
	last_built = 0;
	if os.path.isfile(exe):
		last_built = os.path.getmtime(exe);

	#Compile object files
	print(color.GREEN + "[Compiling]" + color.ENDC)
	objects = []
	for source in sources:
		out = build_dir + '/' + os.path.splitext(os.path.basename(source))[0] + '.o'
		objects.append(out)
		#Compile source files if they have been modified since the last build
		if(os.path.getmtime(source) > last_built):
			print(source)
			os.system(cc + ' -c ' + source + ' -o ' + out  + ' -I'.join([''] + include_dirs) + ' ' + cflags)

	#link executable
	print(color.GREEN + "[Linking]" + color.ENDC)
	os.system(cc + ' -o ' + exe + ' ' + ' '.join(objects) + ' ' + cflags)
	return

def clean():
	#remove the build directory
	shutil.rmtree(build_dir)
	return

if len(sys.argv) == 1 :
	build()
elif sys.argv[1] == 'clean':
	clean()