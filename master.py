import smbus
import time


channel = 1
address = 0x10

#setup the bus
bus = smbus.SMBus(channel)

#Reads the byte
def ReadByte():
        reading = bus.read_byte_data(address, 1)
        return reading

while True:    
        randomNumber = ReadByte()

        if (randomNumber >= 75):
            print("In the Upper Portion: " + str(randomNumber))
        elif (randomNumber <= 25):
            print("In the Lower Portion: " + str(randomNumber))
        else:      #this returns the value as a byte between 0 and 255. 
            print("Around the Middle: " + str(randomNumber))
        time.sleep(1)