import RPi.GPIO as IO          

import time                            

IO.setwarnings(False)            

x=0                                         
IO.setmode (IO.BCM)          

IO.setup(13,IO.OUT)         
IO.setup(19,IO.IN)             
IO.setup(26,IO.IN)             

p = IO.PWM(13,100)        
p.start(0)                            
try:
    while 1:                            
        p.ChangeDutyCycle(x)                 
        if(IO.input(26) == False):           
            if(x<50):
             x=x+1                                 
             time.sleep(0.2)                   

        if(IO.input(19) == False):         
            if(x>0):
              x=x-1                               
              time.sleep(0.2)                
except KeyboardInterrupt:
    pass
p.stop()
IO.cleanup()
