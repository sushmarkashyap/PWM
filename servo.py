import RPi.GPIO as IO          

import time                            

IO.setwarnings(False)            

IO.setmode (IO.BOARD)          

IO.setup(7,IO.OUT)                       

p = IO.PWM(7,50)        
p.start(7.5)                            
try:
    while True:                            
        p.ChangeDutyCycle(7.5)                 
        time.sleep(1) 
        p.ChangeDutyCycle(12.5)                 
        time.sleep(1)
        p.ChangeDutyCycle(2.5)                 
        time.sleep(1)              
except KeyboardInterrupt:
    pass
p.stop()
IO.cleanup()
