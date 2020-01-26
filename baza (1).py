import pyodbc
import RPi.GPIO as GPIO
import sys
import Adafruit_DHT
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.OUT)

humidity, temperature = Adafruit_DHT.read_retry(11, 4)

server = 'rskalecki-cdv.database.windows.net'
database = 'rskalecki_cdv'
username = 'rskalecki'
password = 'Rafi25081996'
driver = '{FreeTDS}'
tds_version = '7.0'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password+';TDS_VERSION='+tds_version)

try:
    while True:
         button_state = GPIO.input(17)
         if button_state == False:
             cursor = cnxn.cursor()
             cursor.execute("insert into dbo.tabela values ({0:0.1f},{1:0.1f});".format(temperature, humidity))
             cnxn.commit()
             cursor.execute("select * from dbo.tabela")

             row = cursor.fetchone()
             GPIO.output(27, True)
             print('1 rekord dodany. ')
             time.sleep(0.2)
         else:
             GPIO.output(27, False)
                         
except:
    GPIO.cleanup()
    
    while row:
            print (str(row[0]) + " " + str(row[1]) + " " + str(row[2]))
            row = cursor.fetchone()
