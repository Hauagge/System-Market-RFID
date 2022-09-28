from multiprocessing import Event
import serial
import time


stop_event = Event()
TAMANHO_STRING =33
PORT='COM5'


def read_tag():
#  1 Cria um objeto serial
    ser = serial.Serial(
        port = PORT,
        baudrate = 38400,
        parity = serial.PARITY_NONE,
        stopbits = serial.STOPBITS_ONE,
        bytesize = serial.EIGHTBITS,
        #ser.timeout = 1
        timeout=1,
    )

    arrayTags= [""]
    readTags=set()
    try:
        ser.open()
    except serial.SerialException:
        pass

    print('Inicializou a porta sem erros: %s' % ser.portstr)
 
    prevSize=0 
    countReadLazy=0
    while (countReadLazy < 10):
        
        ser.write(serial.to_bytes([0x0A, 0x55, 0x0D]))
        response = ser.read(ser.inWaiting())
        arrayTags = response.decode('utf8').replace('\r',',').replace('\n',',')
        arrayTag =  arrayTags.split(',')
        arrayTag = list(filter(None,arrayTag))
        time.sleep(0.500)
        
        for k in range(len(arrayTag)):
            if len(arrayTag[k]) >= 33:
                print(arrayTag[k]
                )
                readTags.add(arrayTag[k].replace('U',''))

        if(len(readTags) > prevSize):
            prevSize = len(readTags)
            countReadLazy =0
        if(len(readTags)== prevSize):
            print(countReadLazy)
            countReadLazy +=1
       
    ser.close()
    return readTags