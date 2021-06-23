from sense_hat import SenseHat  
import time #Time functions 
import sys #Import 
from ISStreamer.Streamer import Streamer #Required for data logging
from Mail import Emailer #Create an object from the emailer.

#Key for IInitial State data bucket.
accessKEY       = "ist_t9nJ6MlA-EU7eKxRiMjVJ3XZT2_Z8KvV"
dataName        = "Smart Monitor"
dataKey         = "Rasberry"
currentLocation = "Living Room"

#Create Sense Hat object
SenseHat = SenseHat()

dataStream = Streamer(bucket_name=dataName, bucket_key=dataKey, access_key=accessKEY)

email = Emailer()

timer   = 300 
timeNow = 0

while True:
 
    #Measure climate units
    tempC = SenseHat.get_temperature()
    hum = SenseHat.get_humidity() 
    prMb = SenseHat.get_pressure()
              
    # Format data from sensor readings
    tempC = float("{:.2f}".format(tempC))
    hum   = float("{:.2f}".format(hum))
    prMb  = float("{:.2f}".format(prMb))
              
    # Print data in console 
    print (currentLocation  + " " + str(tempC) +  " C")
    print (currentLocation  + " " + str(hum)   +  " %")
    print (currentLocation  + " " + str(prMb)  +  " Mb")
    
    if tempC < 15 and ((time.time() - timeNow) > timer):
        timeNow = time.time()
        email.sendMail()
        print("Email sent.")
        continue
    
    if hum > 50 and ((time.time() - timeNow) > timer):
        timeNow = time.time()
        email.sendMail()
        print("Email sent.")
        continue
    
    #Log the data 
    dataStream.log(":sunny: "       + " C", tempC)
    dataStream.log(":sweat_drops: " + " %",   hum)
    dataStream.log(":cloud: "       + " Mb",  prMb)    
            
    dataStream.flush()
    time.sleep(1)
          

