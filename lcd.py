from driver.gpio import CharLCD
from RPi import GPIO
import sys

try:
    pinstype_splited = sys.argv[1].split(",")
    pins = [pinstype_splited[0], pinstype_splited[1], pinstype_splited[2], pinstype_splited[3], pinstype_splited[4], pinstype_splited[5]]
    position = [pinstype_splited[6], pinstype_splited[7]]
except:
    raise TypeError("The entered Pins, Type is not correct")
try:
    text_splited = sys.argv[2].split(":")
    rowcol = text_splited[0].split(",")
    text = text_splited[1]
    text = text.replace("#/@$%", " ")
except:
    raise TypeError("The sended text is not correct")
lcd = CharLCD(rows=int(position[0]), cols=int(position[1]), pin_rs=int(pins[0]), pin_e=int(pins[1]), pins_data=[int(pins[2]), int(pins[3]), int(pins[4]), int(pins[5])], numbering_mode=GPIO.BOARD)
lcd.cursor_pos = (int(rowcol[0])-1, int(rowcol[1])-1)
if (text):
    lcd.write_string(unicode(text))
else:
    lcd.clear()

