#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import print_function  # use python 3 syntax but make it compatible with python 2
from __future__ import division  # ''

# import brickpi3 # import the BrickPi3 drivers
import time  # import the time library for the sleep function
import sys
import numpy as np
import brickpi3 # import the BrickPi3 drivers
import robotics as rb

# tambien se podria utilizar el paquete de threading
from multiprocessing import Process, Value, Array, Lock
from math import cos, sin, atan2, radians, degrees
import cv2
import numpy as np
import calibrarCamara as cc


class Robot:
    def __init__(self, init_position=[0.0, 0.0, 0.0]):
        """
        Initialize basic robot params. \

        Initialize Motors and Sensors according to the set up in your robot
        """

        # Robot construction parameters
        self.r = 2.8
        self.L = 10.7

        self.enc_d = 0.0
        self.enc_i = 0.0

        self.log_file = None

        self.area = 50000

        # Motors and sensors setup

        # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.
        self.BP = brickpi3.BrickPi3()

        # Configure sensors, for example a touch sensor.
        # self.BP.set_sensor_type(self.BP.PORT_1, self.BP.SENSOR_TYPE.TOUCH)

        # reset encoder B and C (or all the motors you are using)
        # self.BP.offset_motor_encoder(self.BP.PORT_B,
        #    self.BP.get_motor_encoder(self.BP.PORT_B))
        # self.BP.offset_motor_encoder(self.BP.PORT_C,
        #    self.BP.get_motor_encoder(self.BP.PORT_C))

        ##################################################
        # odometry shared memory values
        self.x = Value('d', 0.0)
        self.y = Value('d', 0.0)
        self.th = Value('d', 0.0)
        self.finished = Value('b', 1)  # boolean to show if odometry updates are finished

        self.v = Value('d', 0.0)
        self.w = Value('d', 0.0)

        # if we want to block several instructions to be run together, we may want to use an explicit Lock
        self.lock_odometry = Lock()

        # odometry update period
        self.P = 0.07

    def setSpeed(self, v, w):
        """ Stablish the speed of both motors """
        print("setting speed to %.2f %.2f" % (v, w))

        # compute the speed that should be set in each motor ...

        # speedPower = 100
        # BP.set_motor_power(BP.PORT_B + BP.PORT_C, speedPower)
        
        M1 = np.array([[1/self.r, self.L/(2*self.r)],
                      [1/self.r, -self.L/(2*self.r)]])
        
        M2 = np.array([[v],[w]])
        
        result = np.dot(M1,M2)
    

        speedDPS_right = np.rad2deg(result[0][0])
        speedDPS_left = np.rad2deg(result[1][0])

        self.BP.set_motor_dps(self.BP.PORT_D, speedDPS_left)
        self.BP.set_motor_dps(self.BP.PORT_A, speedDPS_right)

    def readSpeed(self):
        """ Returns current value of linear and angular speed"""
        self.lock_odometry.acquire()
        v = self.v.value
        w = self.w.value
        self.lock_odometry.release()
        return v, w

    def readOdometry(self):
        """ Returns current value of odometry estimation """
        self.lock_odometry.acquire()
        x = self.x.value
        y = self.y.value
        th = self.th.value
        self.lock_odometry.release()
        return x,y,th

    def startOdometry(self):
        """ This starts a new process/thread that will be updating the odometry periodically """
        self.log_file = time.strftime("%Y%m%d-%H%M%S") + '.txt'
        fichero = open(self.log_file, 'w')
        fichero.write(str(0)+"\t"+str(self.x.value)+"\t"+str(self.y.value)+"\t"+str(self.th.value)+"\n")
        fichero.close()
        self.x.value = 0
        self.y.value = 0
        self.th.value = 0
        self.finished.value = False
        self.p = Process(target=self.updateOdometry, args=())  # additional_params?))
        self.p.start()
        print("PID: ", self.p.pid)

    # You may want to pass additional shared variables besides the odometry values and stop flag
    def updateOdometry(self):  # , additional_params?):
        """ Updates the position and theta in a continuous loop """

        while not self.finished.value:
            # current processor time in a floating point value, in seconds
            tIni = time.clock()


            try:
                # Each of the following BP.get_motor_encoder functions returns the encoder value
                # (what we want to store).
                #sys.stdout.write("Reading encoder values .... \n")
                [encoder1, encoder2] = [self.BP.get_motor_encoder(self.BP.PORT_A),
                    self.BP.get_motor_encoder(self.BP.PORT_D)]

                wd = (radians(encoder1) - self.enc_d) / self.P
                wi = (radians(encoder2) - self.enc_i) / self.P

                diff_encD = radians(encoder1) - self.enc_d
                diff_encI = radians(encoder2) - self.enc_i
                self.enc_d = radians(encoder1)
                self.enc_i = radians(encoder2)

                v = self.r * (wd + wi) / 2
                w = self.r * (wd - wi) /(self.L)
                
                if w == 0:
                    th = 0
                    s = v * self.P  # o tambien -> (encoder1 + encoder2) / 2
                    #s = (diff_encD + diff_encI) / 2
                else:
                    th = w * self.P  # (encoder1 - encoder2) / self.L
                    #th = (diff_encD - diff_encI) / self.L
                    s = (v / w) * th


                x_ini, y_ini, th_ini = self.readOdometry()

                x = x_ini + s * np.cos(th_ini + th / 2)
                y = y_ini + s * np.sin(th_ini + th / 2)
                theta = rb.norm_pi(th_ini + th)

                fichero = open(self.log_file, 'a')
                fichero.write(str(tIni)+"\t"+str(x)+"\t"+str(y)+"\t"+str(theta)+"\n")
                fichero.close()

                self.lock_odometry.acquire()
                self.x.value = x
                self.y.value = y
                self.th.value = theta
                self.v.value = v
                self.w.value = w
                self.lock_odometry.release()

            except IOError as error:
                sys.stdout.write(error)

            # sys.stdout.write("Encoder (%s) increased (in degrees) B: %6d  C: %6d " %
            #        (type(encoder1), encoder1, encoder2))

            # save LOG
            # Need to decide when to store a log with the updated odometry ...

            ######## UPDATE UNTIL HERE with your code ########

            tEnd = time.clock()
            time.sleep(self.P - (tEnd - tIni))

        # print("Stopping odometry ... X= %d" %(self.x.value))
        sys.stdout.write("Stopping odometry ... X=  %.2f, \
                Y=  %.2f, th=  %.2f \n" % (self.x.value, self.y.value, self.th.value))

    # Stop the odometry thread.
    def stopOdometry(self):
        self.finished.value = True
        self.BP.reset_motor_encoder(self.BP.PORT_A)
        self.BP.reset_motor_encoder(self.BP.PORT_D)
        self.BP.reset_all()


    def trackObject(self, colorRangeMin=[0,0,0], colorRangeMax=[255,255,255]):
        finished = False 
        targetFound = False 
        targetPositionReached = False 
        frame = cv2.VideoCapture(0)
        while not finished: 
        # 1. search the most promising blob 
            # Capturar imagen
            ret, img_BGR = frame.read()

            # calcular blob en la imagen (get_color_blobs)
            img_BGR, im_with_keypoints, keypoints_red, mask_red = cc.detectBlob(img_BGR)

            # Si hay más de un blob, seleccionar el más grande
            if keypoints_red:
                maxDiameter = 0
                kp = keypoints_red[0]
                for kp2 in keypoints_red:
                    if kp2.size > maxDiameter:
                        kp = kp2
                        maxDiameter = kp2.size    
            else:
                kp = None

            # Calcular areas y distancias
            if kp:
                
                distance, diff = cc.computeDistances(img_BGR, self.area, kp)
                
                if abs(distance) >= 70:
                    w_speed = abs(distance) / 1500
                    if distance > 0:
                        w_speed = 0 - w_speed
                    self.setSpeed(0,w_speed)
                    
                elif abs(diff) >= 10000: # que esté centrado
                    v_speed = diff // 2000
                    self.setSpeed(v_speed, 0)
                    
                if abs(distance) < 70 and abs(diff) < 10000: # que esté lo suficientemente cerca
                    self.setSpeed(0, 0)
                    cc.draw_blobs(img_BGR, keypoints_red,im_with_keypoints)
                    finished = True
                
            else:
                # Buscar píxeles rojos a la izquierda o derecha de la imagen
                left_red_pixels = np.sum(mask_red[:, :mask_red.shape[1]//2])
                right_red_pixels = np.sum(mask_red[:, mask_red.shape[1]//2:])

                # if left_red_pixels > 0:
                #     print("Píxeles rojos encontrados a la izquierda de la imagen")
                #     self.setSpeed(0, 0.3)
                # elif right_red_pixels > 0:
                #     print("Píxeles rojos encontrados a la derecha de la imagen")
                #     self.setSpeed(0, -0.3)
                # else:
                print("No hay")
                self.setSpeed(0, 0.3)

        return finished 


    def catch(self): 
        # decide the strategy to catch the ball once you have reached the target position 
        # Avanzar un poco
        # Girar el motor de la cesta
        return True