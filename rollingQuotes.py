import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import RPi.GPIO as GPIO

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import subprocess

import json, os, random
import util
import sys

DELAY = sys.argv[1]
# Get data
curr_path = os.getcwd()
jsonfiles = []
for fileItem in os.listdir(curr_path):
    if '.json' in fileItem:
        jsonfiles.append(fileItem)
#print jsonfiles

jsonfile = random.choice(jsonfiles)
with open(jsonfile) as jsondata:
    quotes = json.load(jsondata)
short_quotes = util.getShortQuotes(quotes,60)
print short_quotes
print 'Loading + '+str(jsonfile)
# Input pins:
L_pin = 27
R_pin = 23
C_pin = 4
U_pin = 17
D_pin = 22

A_pin = 5
B_pin = 6

GPIO.setmode(GPIO.BCM)

GPIO.setup(A_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(B_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(L_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(R_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(U_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(D_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(C_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up

# Raspberry Pi pin configuration:
RST = 24     # on the PiOLED this pin isnt used
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# 128x32 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
#image = Image.new('1', (width, height))

# Get drawing object to draw on image.
#draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
#draw.rectangle((0,0,width,height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0


# Load default font.
font = ImageFont.load_default()

# Alternatively load a TTF font.  Make sure the .ttf font file is in the same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
#font = ImageFont.truetype('pixelmix.ttf', 8)
print 'Loading Fonts'
# Var Inits
u_pin_old = 0
d_pin_old = 0
l_pin_old = 0
r_pin_old = 0
key = random.choice(short_quotes.keys())
quote = short_quotes[key]
quote_sentence = util.convertToDisplay(quote, 17)
max_len = len(quote_sentence)
count  = 0
while True:
   # Draw a black filled box to clear the image.
    #draw.rectangle((0,0,width,height), outline=0, fill=0)
    if count > DELAY:
        key = random.choice(short_quotes.keys())
        quote = short_quotes[key]
        quote_sentence = util.convertToDisplay(quote, 17)
        print quote_sentence
        count = 0
       
    count = count + 1

    #print quote
    x = 0
    for x in range(len(quote)):
        image = Image.new('1', (width, height))
        draw = ImageDraw.Draw(image)
        draw.rectangle((0,0,width,height), outline=0, fill=0)
        draw.text((2,15),str(quote[x+1:len(quote)]),font=font,fill=255)
        #draw.text((0,24),str(subquote),font=font, fill = 255)
        disp.image(image)
        disp.display()
        time.sleep(0.5)

