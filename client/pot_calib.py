import Adafruit_BBIO.ADC as ADC
import time
#37, 38, 39, 40
ADC.setup("P9_40")
while True:
  print ADC.read("P9_40")
  time.sleep (0.0100)
