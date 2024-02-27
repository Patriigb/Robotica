#!/usr/bin/python
# -*- coding: UTF-8 -*-
import argparse
import numpy as np
import time
import math
import robotics as rb
from Robot import Robot




def main(args):
    try:
        print(args.radioD)
        if args.radioD < 0:
            print('d must be a positive value')
            exit(1)


        #p = input()
        # Instantiate Odometry. Default value will be 0,0,0
        # robot = Robot(init_position=args.pos_ini)
        robot = Robot()
        print("X value at the beginning from main X= %.2f" %(robot.x.value))
        # 1. launch updateOdometry Process()
        #robot.startOdometry()

        # 2. perform trajectory


        # Linea recta
#        robot.setSpeed(10,0)
#        print("Start : %s" % time.ctime())
#        time.sleep(4)
#        print("X value from main tmp %d" % robot.x.value)
#        robot.lock_odometry.acquire()
#        print("Odom values at main at the END: %.2f, %.2f, %.2f " % (robot.x.value, robot.y.value, robot.th.value))
#        robot.lock_odometry.release()
#
#        robot.stopOdometry()

        # p = input()
        # # Solo w (circulo)
        # robot.startOdometry()
        # robot.setSpeed(0, 4)
        # print("Start : %s" % time.ctime())
        # time.sleep(4)
        # print("X value from main tmp %d" % robot.x.value)
        # robot.lock_odometry.acquire()
        # print("Odom values at main at the END: %.2f, %.2f, %.2f " % (robot.x.value, robot.y.value, robot.th.value))
        # robot.lock_odometry.release()
        # time.sleep(4)
        # print("End : %s" % time.ctime())

        # robot.lock_odometry.acquire()
        # print("Odom values at main at the END: %.2f, %.2f, %.2f " % (robot.x.value, robot.y.value, robot.th.value))
        # robot.lock_odometry.release()

        # robot.stopOdometry()

#        p = input()
#        # 90º
        # robot.startOdometry()
        # robot.setSpeed(0, math.pi/2)
        # print("Start : %s" % time.ctime())
        # time.sleep(1)
        # print("X value from main tmp %d" % robot.x.value)
        # robot.lock_odometry.acquire()
#        print("Odom values at main at the END: %.2f, %.2f, %.2f " % (robot.x.value, robot.y.value, robot.th.value))
#        robot.lock_odometry.release()
#        robot.stopOdometry()
#        nextStep = False
#        robot.setSpeed(0, -1)
#        while not nextStep:
#            x,  y, theta = robot.readOdometry()
#            if rb.norm_pi(theta) > math.pi/2 - 0.1  and rb.norm_pi(theta) < math.pi/2 + 0.1:
#                nextStep = True
#        robot.stopOdometry()
        # robot.stopOdometry()

        # ...

#        # 8:
        
#         p = input()
#         robot.startOdometry()
        eps = 2.5
#         # girar 90º
#         nextStep = False
#         x,  y, theta_ini = robot.readOdometry()
#         robot.setSpeed(0, -1)
#         while not nextStep:
#             x,  y, theta = robot.readOdometry()
#             # print("th", rb.norm_pi(theta - theta_ini), "min", -math.pi/2 - 0.05, "max", -math.pi/2 + 0.05)
#             if theta != 0:
#                 if rb.norm_pi(theta - theta_ini) > -math.pi/2 - 0.05  and \
#                     rb.norm_pi(theta - theta_ini) < -math.pi/2 + 0.05:
#                     nextStep = True
                    


# #
# #        # girar medio 8
#         nextStep = False
#         x_ini,  y_ini, theta_ini = robot.readOdometry()
#         WxI = np.array([x_ini, y_ini, theta_ini])

#         WxF = np.array([(x_ini + args.radioD * 2), y_ini, rb.norm_pi(theta_ini +  math.pi)])

#         v = 10.0
#         R = args.radioD
#         w = v / R

#         robot.setSpeed(v, w)
#         while not nextStep:
#             x,  y, theta = robot.readOdometry()
#             if x > (WxF[0] - eps)  and x < (WxF[0] + eps) and \
#                y > WxF[1] - eps  and y < WxF[1] + eps :
#                 #rb.norm_pi(theta) > WxF[2] - 0.07 and rb.norm_pi(theta) < WxF[2] + 0.07 :
#                     nextStep = True
# # # #
# # #
# # #        # girar girar un circulo
#         nextStep = False
#         x_ini,  y_ini, theta_ini = robot.readOdometry()
#         WxI = np.array([x_ini, y_ini, theta_ini])

#         WxF = np.array([x_ini, y_ini, theta_ini])

#         v = 10.0
#         R = args.radioD
#         w = v / R
#         robot.setSpeed(v, -w)
#         time.sleep(0.5)
#         while not nextStep:
#             x,  y, theta = robot.readOdometry()
#             if x > WxF[0] - eps  and x < WxF[0] + eps and \
#                 y > WxF[1] - eps  and y < WxF[1] + eps :
#                 # theta > WxF[2] - 0.1 and theta < WxF[2] + 0.1 :
#                     nextStep = True
# #
#         #robot.stopOdometry()
# # #        # girar girar el otro medio 8
#         nextStep = False
#         x_ini,  y_ini, theta_ini = robot.readOdometry()
#         WxI = np.array([x_ini, y_ini, theta_ini])

#         WxF = np.array([x_ini - args.radioD * 2, y_ini, theta_ini - math.pi])

#         v = 10.0
#         R = args.radioD
#         w = v / R

#         robot.setSpeed(v, w)
#         while not nextStep:
#             x,  y, theta = robot.readOdometry()
#             if  x > (WxF[0] - eps)  and x < (WxF[0] + eps) and \
#                y > WxF[1] - eps  and y < WxF[1] + eps:
#                 # theta > WxF[2] - 0.1 and theta < WxF[2] + 0.1 :
#                     nextStep = True

#         robot.stopOdometry()
#
#        # 2º recorrido
        p = input()
        robot.startOdometry()
        dc = 50.0 
        # girar 90º
        nextStep = False
        x,  y, theta_ini = robot.readOdometry()
        robot.setSpeed(0, 0.7)
        while not nextStep:
            x,  y, theta = robot.readOdometry()
            if theta != 0:
                if rb.norm_pi(theta - theta_ini) > math.pi/2 - 0.05  and \
                    rb.norm_pi(theta - theta_ini) < math.pi/2 + 0.05:
                    nextStep = True
#
#        # girar radio por ejemplo 10 hasta beta
        nextStep = False
        x_ini,  y_ini, theta_ini = robot.readOdometry()

        B = math.asin((args.radioD - args.radioA) / dc)

        print("B", B)
        th_f = rb.norm_pi(math.pi/2 + B - theta_ini)
        print("th_f", th_f)
        v = 7.0
        R1 = args.radioA
        w = v / R1

        robot.setSpeed(v, -w)
        while not nextStep:
            x,  y, theta = robot.readOdometry()
            if theta > th_f - 0.05 and theta < th_f + 0.05 :
                    nextStep = True
                    
        
#
        # avanzar hasta llegar al siguiente circulo
        nextStep = False
        x_ini,  y_ini, theta_ini = robot.readOdometry()

        v = 10.0
        r2 = math.sqrt((dc**2) - (args.radioD - args.radioA)**2)
        
        x2 = x_ini + r2 * math.cos(B)
        y2 = y_ini + r2 * math.sin(B)

        print("x2", x2, "y2", y2)

        robot.setSpeed(v, 0)
        while not nextStep:
            x,  y, theta = robot.readOdometry()
            if x > x2 - eps  and x < x2 + eps and \
                 y > y2- eps  and y < y2 + eps:
                    nextStep = True

        
#
       # girar pi + B + B
        nextStep = False
        x_ini,  y_ini, theta_ini = robot.readOdometry()
        
        th_f = rb.norm_pi(theta_ini - 2*B - math.pi)
        print("th_f2", th_f)
        v = 10.0
        R2 = args.radioD
        w = v / R2
        
        print("ang2", th_f)
        print("ang2", 2*B + math.pi)

        robot.setSpeed(v, -w)
        while not nextStep:
            x,  y, theta = robot.readOdometry()
            print("th", theta, "th_min", th_f - 0.1, "th_max", th_f + 0.1)
            if theta > th_f - 0.15 and theta < th_f + 0.15:
                    nextStep = True
                   
#
#        # avanzar hasta llegar al siguiente circulo
        nextStep = False
        x_ini,  y_ini, theta_ini = robot.readOdometry()

        v = 10.0
        
        r2 = math.sqrt((dc**2) - (args.radioD - args.radioA)**2)
        
        x2 = x_ini - r2 * math.cos(B)
        y2 = y_ini + r2 * math.sin(B)
        
        print("x222", x2, "y222", y2)


        robot.setSpeed(v, 0)
        while not nextStep:
            x,  y, theta = robot.readOdometry()
            if x > x2 - eps -1   and x < x2 + eps + 1:
                    nextStep = True
#
        
#        # girar radio hasta llegar a posicion inicial
        nextStep = False
        x_ini,  y_ini, theta_ini = robot.readOdometry()

        v = 7.0
        R1 = args.radioA
        w = v / R1
        y2 = 0
        x2 = 0

        robot.setSpeed(v, -w)
        while not nextStep:
            x,  y, theta = robot.readOdometry()
            if x > x2 - eps  and x < x2 + eps and \
                y > y2 - eps  and y < y2 + eps :
                    nextStep = True

        robot.stopOdometry()


        # 3. wrap up and close stuff ...
        # This currently unconfigure the sensors, disable the motors,
        # and restore the LED to the control of the BrickPi3 firmware.
        # robot.stopOdometry()


    except KeyboardInterrupt:
    # except the program gets interrupted by Ctrl+C on the keyboard.
    # THIS IS IMPORTANT if we want that motors STOP when we Ctrl+C ...
        robot.stopOdometry()

if __name__ == "__main__":

    # get and parse arguments passed to main
    # Add as many args as you need ...
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--radioD", help="Radio to perform the 8-trajectory (mm)",
                        type=float)
    parser.add_argument("-a", "--radioA", help="Radio to perform the 8-trajectory (mm)",
                        type=float)
    args = parser.parse_args()

    main(args)





