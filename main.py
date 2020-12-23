import pyscreenshot as ss
import numpy as np
import cv2
import pytesseract
import serial

print("idk wot im diong")                                                             #program starts
data = serial.Serial('com1', 9600)                                                    #define baudrate
pytesseract.pytesseract.tesseract_cmd = r'D:\New folder (2)\Tesseract-OCR\tesseract'  #location of ocr file
currentHealth = 100                                                                   #max health
captureArea = (40, 80, 100, 150)                          #cordinates of the area to capture (x1,y1,x2,y2)

while True:                                               #infinite loop
    capture = ss.grab(bbox=captureArea)                   #grab scrn shot
    capture = np.array(capture)                           #convert to numpy array
    capture2 = cv2.cvtColor(capture, cv2.COLOR_BGR2GRAY)  #convert to grayscale

    cv2.imshow('1', capture2)                             #shows the captured area in a window
    cv2.waitKey(1)
    valRead = pytesseract.image_to_string(capture2)       #extracts text as string
    print(valRead)                                        #print the text

    try:
        health = float(valRead)                           #convert the string to float
        if health < currentHealth:
            anything = "1"                                #data to be sent through usb to the arduino
            print("nooooooooob hahah")
            data.write(anything.encode('utf-8'))          #encode to utf8 and send
        currentHealth = health                            #update current health

    except ValueError:
        if valRead.find('a') != -1:                       #sometimes this idiot reads 0 as a
            health = 0
        else:
            print("told yaa idk wot im doing")
