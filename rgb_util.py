import time
import threading 
from rpi_ws281x import *

# LED strip configuration:
LED_COUNT      = 10     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating a signal (try 10)
LED_BRIGHTNESS = 65      # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)

# Intialize the library (must be called once before other functions).
strip.begin()

# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)
    
def effect_rainbow(stop):
    """Draw rainbow that fades across all pixels at once."""
    wait_ms=20
    iterations=100
    for j in range(256*iterations):
        if stop():
            return

        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i+j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def effect_theater_chase_rainbow(stop):
    """Rainbow movie theater light style chaser animation."""
    wait_ms=50
    iterations=100
    for j in range(256*iterations):
        if stop():
            return
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, wheel((i+j) % 255))
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def effect_green_wipe(stop):
    wait_ms=50
    while True:
        if stop():
            return
        colorWipe(strip, Color(0, 255, 0), 120)  # Red wipe
        time.sleep(wait_ms/1000.0)
        colorWipe(strip, Color(0,0,0), 120)
        time.sleep(wait_ms/1000.0)

def animation_stop():
    colorWipe(strip, Color(0,0,0), 10)

def thread_start(function_name):
    global stop_threads
    stop_threads = False
    t = threading.Thread(target = function_name, args =(lambda : stop_threads, )) 
    t.start() 
    return t

def thread_stop(t):
    global stop_threads
    stop_threads = True
    t.join() 
    animation_stop()

def thread_run(function_name, run_for):
    tt = thread_start(function_name)
    time.sleep(run_for) 
    thread_stop(tt)

# Main program logic follows:
if __name__ == '__main__':
    thread_run(effect_theater_chase_rainbow, 60)

