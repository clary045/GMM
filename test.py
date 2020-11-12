########################################################################################################
################# Development of an embedded Vision Based Fruit Sorting Machine ########################
#################                  BY: Clary Norman (ID: 2017141960)            ########################
########################################################################################################
import os
from gpiozero import MotionSensor
import cv2 
import matplotlib.pyplot as plt
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import RPi.GPIO as GPIO
# servo motor
GPIO.setmode(GPIO.BOARD)
servoPin= 22
GPIO.setmode(GPIO.BOARD)
servoPin_1 = 24

desiredPosition1 = 0
desiredPosition2 = 75
desiredPosition3 = 180
desired_1 = 0
desired_2 = 75
desired_3 = 180
GPIO.setup(servoPin,GPIO.OUT)
GPIO.setup(servoPin_1,GPIO.OUT)
pwm=GPIO.PWM(servoPin,50)
pwm_1 =GPIO.PWM(servoPin_1,50)

pir = MotionSensor (24)
camera = PiCamera()
print("Developement of an Embeeded Vision Based Fruit Sorting Machine")
print("By: Clary Norman (2017141960)")
time.sleep(4)
os.system('cls')
print("")
print("PLace the fruit")
while True:
        if pir.wait_for_motion(): #object is near
                print("Fruit detected..")
                rawCapture = PiRGBArray(camera)
                time.sleep(1)
                camera.capture(rawCapture,format = 'bgr')
                time.sleep(5)
                I = rawCapture.array
                from detectOrangeFunc import detectOrange
                [y,x,z,r] = detectOrange(I)

                from detectAppleFunc import detectApple
                [y1,x1,z1,t] = detectApple(I)

                ## Classification:
                print("")
                print ("number of pixels for orange: ")
                print (x)
                print ("number of pixels for apple: ")
                print (x1)

                if x > 5:
                    print("")
                    print("Orange")
                    show = cv2.cvtColor(I, cv2.COLOR_BGR2RGB)
                    plt.imshow(show,cmap = 'gray')
                    plt.show()
                    pwm.start(7)
                    DC = 1./15.*(desiredPosition1)+2
                    pwm.ChangeDutyCycle(DC)
                    time.sleep(2)
                    DC = 1./15.*(desiredPosition3)+2
                    pwm.ChangeDutyCycle(DC)
                elif x1 > 5:
                          print("")
                          print("Apple")
                          plt.imshow(I,cmap = 'gray')
                          plt.show()
                          pwm_1.start(7)
                          DC_1 = 1./15.*(desired_1)+2
                          pwm_1.ChangeDutyCycle(DC_1)
                          time.sleep(2)
                          DC_1 = 1./15.*(desired_3)+2
                          pwm_1.ChangeDutyCycle(DC_1)
                else: 
                    print('Unclassified fruit')
        if pir.wait_for_no_motion(): #object is far away
               print("")
               print ('Place the fruit')