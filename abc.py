import RPi.GPIO as IO           
import time                     
import sys
IO.setwarnings(False)           
IO.setmode (IO.BCM)            

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
    pin=command
    PORT(pin)                
    IO.output(6,0)             
    IO.output(22,1)            
    time.sleep(0.05)
    IO.output(22,0)            
    pin=0
    PORT(pin)                 

def send_a_character (character):               
    pin=character
    PORT(pin)
    IO.output(6,1)
    IO.output(22,1)
    time.sleep(0.05)
    IO.output(22,0)
    pin=0
    PORT(pin)

def PORT(pin):                                
    if(pin&0x01 == 0x01):
        IO.output(21,1)                       
    else:
        IO.output(21,0)                       
    if(pin&0x02 == 0x02):
        IO.output(20,1)                       
    else:
        IO.output(20,0)                       
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
        
while 1:   
    send_a_command(0x01)                    
    send_a_command(0x38)                   
    send_a_command(0x0E)                   
    send_a_character(0x43)                 
    send_a_character(0x49)                 
    send_a_character(0x52)                    
    send_a_character(0x43)                    
    send_a_character(0x55)                     
    send_a_character(0x49)                     
    send_a_character(0x54)                    
    
    
    send_a_character(0x44)                    
    send_a_character(0x49)
    send_a_character(0x47)
    send_a_character(0x45)
    send_a_character(0x53)
    send_a_character(0x54)
    
    time.sleep(1)