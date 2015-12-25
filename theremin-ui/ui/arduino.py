"""
Listen to serial and gether the data in buffer
"""

from threading import Thread
import time
import serial

sensor = []
pitch = []
running = False
def receiving(ser):
    global sensor
    global pitch
    global running
    previousSensor = -1
    previousPitch = -1
    while running:
        raw = ser.readline()
        if raw:
            data = raw.decode().strip()
            value = data.split(":")
            if value[0] == "S":
                previousSensor = value[1]
                sensor.append(previousSensor)
                pitch.append(previousPitch)
            else:
                previousPitch = value[1]
                sensor.append(previousSensor)
                pitch.append(previousPitch)

class SerialData(object):
    def __init__(self, init=50):
        try:
            self.ser = ser = serial.Serial(
                port='/dev/tty.usbmodem1421',
                baudrate=19200,
                bytesize=serial.EIGHTBITS,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                timeout=0.1,
                xonxoff=0,
                rtscts=0,
                interCharTimeout=None
            )
        except serial.serialutil.SerialException:
            #no serial connection
            self.ser = None
        else:
            Thread(target=receiving, args=(self.ser,)).start()

    def next(self):
        if not self.ser:
            return (-1, -1)
        if sensor.__len__() > 0:
            return (sensor.pop(0), pitch.pop(0))
        #if pitch.__len__() > 0:
        #    sValue = sensor.pop(0)
        return None

    def __del__(self):
        if self.ser:
            self.ser.close()

if __name__=='__main__':
    running = True
    s = SerialData()
    for i in range(500):
        time.sleep(.005)
        value = s.next()
        if(value):
            print('Buffer size: ' + str(sensor.__len__()) + ' sensor: ' + str(float(value[0])) + " pitch: " + str(float(value[1])))

    running = False