import RPi.GPIO as IO          
import sys
import time                            

IO.setwarnings(False)            
IO.setmode (IO.BCM)          

IO.setup(4,IO.OUT) 
IO.setup(6,IO.OUT)                
IO.setup(22,IO.OUT)
IO.setup(21,IO.OUT)
IO.setup(20,IO.OUT)
IO.setup(16,IO.OUT)
IO.setup(12,IO.OUT)
IO.setup(25,IO.OUT)
IO.setup(24,IO.OUT)
IO.setup(23,IO.OUT)
IO.setup(18,IO.OUT)    

def send_a_command (command):               
    PORT(pin);                                                
    IO.output(6,0)                                          
    IO.output(22,1)                                         
    time.sleep(0.05)
    IO.output(22,0)                                        
    pin=0
    PORT(pin);                                                

def send_a_character (character):                
    pin=character
    PORT(pin)
    IO.output(6,1)
    IO.output(22,1)
    time.sleep(0.05)
    IO.output(22,0)
    pin=0
    PORT(pin)

def PORT(pin):                                # assigning PIN by taking PORT value
    if(pin&0x01 == 0x01):
        IO.output(21,1)                        # if  bit0 of 8bit 'pin' is true, pull PIN21 high
    else:
        IO.output(21,0)                        # if  bit0 of 8bit 'pin' is false, pull PIN21 low
    if(pin&0x02 == 0x02):
        IO.output(20,1)                        # if  bit1 of 8bit 'pin' is true, pull PIN20 high
    else:
        IO.output(20,0)                        # if  bit1 of 8bit 'pin' is true, pull PIN20 low
    if(pin&0x04 == 0x04):
        IO.output(16,1)
    else:
        IO.output(16,0)
    if(pin&0x08 == 0x08):
        IO.output(12,1)
    else:
        IO.output(12,0)   
if(pin&0x10 == 0x10):
        IO.output(25,1)
    else:
        IO.output(25,0)
    if(pin&0x20 == 0x20):
        IO.output(24,1)
    else:
        IO.output(24,0)
    if(pin&0x40 == 0x40):
        IO.output(23,1)
    else:
        IO.output(23,0)
    if(pin&0x80 == 0x80):
        IO.output(18,1)                        
    else:
        IO.output(18,0)

p = IO.PWM(4,50)        
p.start(7.5)

try:
    while True:            
        send_a_command(0x01);              
        send_a_command(0x38);                   
        send_a_command(0x0E);                
       
        p.ChangeDutyCycle(7.5)  
        send_a_character(0x30);
        time.sleep(1) 
       
        p.ChangeDutyCycle(12.5)    
        send_a_character(0x31);
        send_a_character(0x38);
        send_a_character(0x30);
        time.sleep(1)
       
        p.ChangeDutyCycle(2.5)   
        send_a_character(0x4E);
        send_a_character(0x45);
        send_a_character(0x55);
        send_a_character(0x54);
        send_a_character(0x52);
        send_a_character(0x41);
        send_a_character(0x4C);              
        time.sleep(1)              
except KeyboardInterrupt:
    pass
p.stop()
IO.cleanup()
