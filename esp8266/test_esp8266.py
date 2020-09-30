import machine as m
import time
led=m.Pin(2,m.Pin.OUT)
while 1:
  led.value(0);
  time.sleep(1);
  led.value(1);
  time.sleep(1);
