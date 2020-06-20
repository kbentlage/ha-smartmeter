import sys
import time
import yaml
import serial
import paho.mqtt.publish

from smartmeter import Smartmeter

def main(args=None):

    # init smartmeter
    smartmeter = Smartmeter()

    # open config file
    with open('config.yaml', 'r') as configFile:
        config = yaml.load(configFile)

    # open serial port
    ser = serial.Serial()
    ser.port        = config['serial']['port']
    ser.baudrate    = config['serial']['baudRate']
    ser.bytesize    = serial.EIGHTBITS
    ser.parity      = serial.PARITY_NONE
    ser.stopbits    = serial.STOPBITS_ONE
    ser.xonxoff     = serial.XON
    ser.rtscts      = 0
    ser.timeout     = config['serial']['timeout']

    # open serial port
    try:
        ser.open()
    except:
        sys.exit('Cannot open serial port %s' % ser.name)

    lineCount = 0

    # start infinite loop
    while True:

        serialLine = ser.readline()
        serialLine = str(serialLine)
        serialLine = serialLine.strip()

        # process transcript line
        smartmeter.processTranscriptLine(serialLine)

        lineCount = lineCount + 1

        # when full transcript is processed, send all messages
        if(lineCount == 36):
            # timestamp
            smartmeter.addMessage(smartmeter.baseTopic + '/timestamp', time.time())

            paho.mqtt.publish.multiple(
                smartmeter.getMessages(),
                hostname=config['mqtt']['host'],
                port=config['mqtt']['port'],
                client_id=config['mqtt']['client'],
    #            auth={
    #               'username': config['mqtt']['auth']['username'],
    #                'password': config['mqtt']['auth']['password']
    #            },
            )

            smartmeter.emptyMessages()
            lineCount = 0

if __name__ == "__main__":
    main()
