# adapted from raspberrypi.stackexchange.com/questions/1661/how-can-i-connect-a-hd44780-based-lcd


#!/usr/bin/env python

import time

class LCD_23017(object):
    # Timing constants
    E_PULSE = 0.00005
    E_DELAY = 0.00005
    def __init__(self, bus, addr, port, rs, en):
        self.bus = bus
        self.addr = addr
        self.rs = rs
        self.en = en

        self.DIRECTION = 0x00 if port == 'A' else 0x01
        self.DATA = 0x12 if port == 'A' else 0x13

        self.bus.write_byte_data(addr, self.DIRECTION, 0x00)

    def lcd_byte(self, data, rs):
        rs <<= self.rs
        en = 1 << self.en
        for nybble in (data&0xf0, data<<4):
            self.bus.write_byte_data(self.addr, self.DATA, nybble | rs)
            time.sleep(self.E_DELAY)
            self.bus.write_byte_data(self.addr, self.DATA, nybble | rs | en)
            time.sleep(self.E_PULSE)
            self.bus.write_byte_data(self.addr, self.DATA, nybble | rs)


class HD47780(object):
    LCD_CHR = True
    LCD_CMD = False
    # Base addresses for lines on a 20x4 display
    LCD_BASE = 0x80, 0xC0, 0x94, 0xD4

    def __init__(self, driver, rows=2, width=16):
        self.rows = rows
        self.width = width
        self.driver = driver
        self.lcd_init()

    def lcd_init(self):
        # Initialise display
        lcd_byte = self.driver.lcd_byte
        for i in 0x33, 0x32, 0x28, 0x0C, 0x06, 0x01:
            lcd_byte(i, self.LCD_CMD)

    def lcd_string(self, message, line=0):
        # Send string to display
        lcd_byte = self.driver.lcd_byte
        lcd_byte(self.LCD_BASE[line], self.LCD_CMD)
        for i in bytearray(message.ljust(self.width)):
            lcd_byte(i, self.LCD_CHR)


class lcd:
	def __init__(self, bus):
		driver1 = LCD_23017(bus, addr=0x20, port='B', rs=0, en=1)
   		# driver2 = LCD_23017(bus, addr=0x20, port='B', rs=0, en=2)
		
		self.lcd1 = HD47780(driver1, rows=2, width=16)
   		# lcd2 = HD47780(driver=driver2, rows=2, width=16)
   		self.lcds = []
   		self.lcds.append(self.lcd1)
   
   
   
	def writeLCD(self, LCD, line, message):
		if LCD < len(self.lcds):
			if len(message)>16:
				print "LCD: message too long, printed first 16 characters"
			self.lcds[LCD].lcd_string(message, line)


def test_i2c():
	import smbus
	driver



def main():
    test_i2c()

if __name__ == "__main__":
	main()
