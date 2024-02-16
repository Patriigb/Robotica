#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import print_function  # use python 3 syntax but make it compatible with python 2
from __future__ import division  # ''

# import brickpi3 # import the BrickPi3 drivers
import time  # import the time library for the sleep function
import sys
import numpy as np
import brickpi3 # import the BrickPi3 drivers

# tambien se podria utilizar el paquete de threading
from multiprocessing import Process, Value, Array, Lock
from math import cos, sin, atan2, radians, degrees


class Robot:
    def __init__(self, init_position=[0.0, 0.0, 0.0]):
        """
        Initialize basic robot params. \

        Initialize Motors and Sensors according to the set up in your robot
        """

        ######## UNCOMMENT and FILL UP all you think is necessary (following the suggested scheme) ########

        # Robot construction parameters
        # self.R = ??
        # self.L = ??
        # self. ...
        self.r =
        self.L =

        ##################################################
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

        self.enc_d = None
        self.enc_i = None
        # if we want to block several instructions to be run together, we may want to use an explicit Lock
        self.lock_odometry = Lock()
        # self.lock_odometry.acquire()
        # print('hello world', i)
        # self.lock_odometry.release()

        # odometry update period --> UPDATE value!
        self.P = 0.1

    def setSpeed(self, v, w):
        """ To be filled - These is all dummy sample code """
        print("setting speed to %.2f %.2f" % (v, w))

        # compute the speed that should be set in each motor ...

        # speedPower = 100
        # BP.set_motor_power(BP.PORT_B + BP.PORT_C, speedPower)

        speedDPS_left = degrees(v / self.r - (self.L * w) / (2 * self.r))
        speedDPS_right = degrees(v / self.r + (self.L * w) / (2 * self.r))

        self.BP.set_motor_dps(self.BP.PORT_B, speedDPS_left)
        self.BP.set_motor_dps(self.BP.PORT_C, speedDPS_right)

    def readSpeed(self):
        """ To be filled"""
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
        self.finished.value = False
        self.p = Process(target=self.updateOdometry, args=())  # additional_params?))
        self.p.start()
        print("PID: ", self.p.pid)

    # You may want to pass additional shared variables besides the odometry values and stop flag
    def updateOdometry(self):  # , additional_params?):
        """ To be filled ...  """

        while not self.finished.value:
            # current processor time in a floating point value, in seconds
            tIni = time.clock()

            # compute updates

            ######## UPDATE FROM HERE with your code (following the suggested scheme) ########
            sys.stdout.write("Dummy update of odometry ...., X=  %d, \
                Y=  %d, th=  %d \n" % (self.x.value, self.y.value, self.th.value))
            # print("Dummy update of odometry ...., X=  %.2f" %(self.x.value) )

            # update odometry uses values that require mutex
            # (they are declared as value, so lock is implicitly done for atomic operations, BUT =+ is NOT atomic)

            # Operations like += which involve a read and write are not atomic.
            # with self.x.get_lock():
            #    self.x.value+=1

            # to "lock" a whole set of operations, we can use a "mutex"
            # self.lock_odometry.acquire()
            # self.x.value+=1
            # self.y.value+=1
            # self.th.value+=1
            # self.lock_odometry.release()

            try:
                # Each of the following BP.get_motor_encoder functions returns the encoder value
                # (what we want to store).
                sys.stdout.write("Reading encoder values .... \n")
                [encoder1, encoder2] = [self.BP.get_motor_encoder(self.BP.PORT_B),
                    self.BP.get_motor_encoder(self.BP.PORT_C)]

                wd = radians(encoder1 - self.enc_d) / self.P
                wi = radians(encoder2 - self.enc_i) / self.P
                self.enc_d = wd
                self.enc_i = wi

                v = self.r * (wd + wi) / 2
                w = self.r * (wd - wi) / self.L

                if w == 0:
                    th = 0
                    s = v * self.P  # o tambien -> (encoder1 + encoder2) / 2
                else:
                    th = w * self.P  # (encoder1 - encoder2) / self.L
                    s = (v / w) * th

                x = s * np.cos(self.th.value + th / 2)
                y = s * np.sin(self.th.value + th / 2)
                theta = th

                self.lock_odometry.acquire()
                self.x.value = x
                self.y.value = y
                self.th.value = theta
                self.v.value = v
                self.w.value = w
                self.lock_odometry.release()

            except IOError as error:
                # print(error)
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
        # self.BP.reset_all()
