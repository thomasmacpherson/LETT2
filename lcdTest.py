import time
import RPi.GPIO as GPIO

class LCD_GPIO(object):
    # Timing constants
    E_PULSE = 0.00005
    E_DELAY = 0.00005
    def __init__(self, RS, E, D4, D5, D6, D7):
        self.RS = RS
        self.E = E
        self.D4 = D4
        self.D5 = D5
        self.D6 = D6
        self.D7 = D7

        GPIO.setmode(GPIO.BCM)        # Use BCM GPIO numbers
        GPIO.setup(self.E, GPIO.OUT)  # E
        GPIO.setup(self.RS, GPIO.OUT) # RS
        GPIO.setup(self.D4, GPIO.OUT) # DB4
        GPIO.setup(self.D5, GPIO.OUT) # DB5
        GPIO.setup(self.D6, GPIO.OUT) # DB6
        GPIO.setup(self.D7, GPIO.OUT) # DB7

    def lcd_byte(self, data, mode):
        GPIO.output(self.RS, mode)

        for bits in (data>>4, data):
            GPIO.output(self.D4, bits&0x01)
            GPIO.output(self.D5, bits&0x02)
            GPIO.output(self.D6, bits&0x04)
            GPIO.output(self.D7, bits&0x08)

            # Toggle E
            time.sleep(self.E_DELAY)
            GPIO.output(self.E, True)
            time.sleep(self.E_PULSE)
            GPIO.output(self.E, False)
            time.sleep(self.E_DELAY)


class LCD_23017(object):
    pass

class LCD_4094(object):
    pass    

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


    def lcd_string(self, message):
        # Send string to display
        lcd_byte = self.driver.lcd_byte
        lcd_byte(self.LCD_BASE[0], self.LCD_CMD)
        for i in bytearray(message.ljust(self.width)):
            lcd_byte(i, self.LCD_CHR)

def test_gpio():
    driver = LCD_GPIO(RS=7, E=8, D4=25, D5=24, D6=23, D7=18)
    lcd = HD47780(driver=driver, rows=4, width=20)
    lcd.lcd_string("Welcome gnibbler")


def main():
    test_gpio()

if __name__ == "__main__":
    main()
