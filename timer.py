#!/usr/bin/env python

while True:
    import RPi.GPIO as GPIO
    import time
    import datetime
    import csv
    
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(26, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    flag_low = 0
    add_list = []
    day = str(datetime.date.today())
    flag_end = 0
    pin = 23

    while flag_end==0:
        if GPIO.input(17)>.5 and flag_low == 0:
            category = 'Job'
            pin = 17
            flag_low +=1
            add_list.append(day)
            hora = time.time()
            time.sleep(.3)
    
        if GPIO.input(27)>.5 and flag_low == 0:
            category = 'Admin'
            pin = 27
            flag_low +=1
            add_list.append(day)
            hora = time.time()
            time.sleep(.3)
    
        if GPIO.input(22)>.5 and flag_low == 0:
            category = 'School'
            pin = 22
            flag_low +=1
            add_list.append(day)
            hora = time.time()
            time.sleep(.3)
    
        if GPIO.input(5)>.5 and flag_low == 0:
            category = 'Free Time'
            pin = 5
            flag_low +=1
            add_list.append(day)
            hora = time.time()
            time.sleep(.3)
            
        while GPIO.input(pin)>.5 and flag_low == 1:
            GPIO.output(26, GPIO.LOW)
            time.sleep(1)
            GPIO.output(26, GPIO.HIGH)
            time.sleep(1)

        if GPIO.input(pin)<.5 and flag_low == 1:
            end_time = time.time()
            secs = end_time - hora
            duration = datetime.timedelta(seconds=int(secs))
            add_list.append(category)
            add_list.append(str(duration))
            add_list = str(add_list)
            add_list = add_list[1:-1]
            add_list = add_list.replace('\'','')
            doc = open('timer.csv','a+')
            doc.write(add_list)
            doc.write('\n')
            doc.flush()
            doc.close()
            GPIO.output(26, GPIO.LOW)
            time.sleep(.5)
            flag_low +=1
            flag_end +=1

    GPIO.cleanup()
