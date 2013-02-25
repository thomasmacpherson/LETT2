import smbus
from math import pow

bus = smbus.SMBus(0)

res = 16 # length in pixel

numberOfRDs = pow((res/8),2)

RDsAdrs={}

baseAdr = 0x40

for i in range(0,4):
	RDsAdrs[i] = baseAdr + i

print RDsAdrs[3]

bus.write_byte_data(RDsAdrs[2],114)