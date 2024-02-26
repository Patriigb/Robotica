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
            

        p = input()
        # Instantiate Odometry. Default value will be 0,0,0
        # robot = Robot(init_position=args.pos_ini)
        robot = Robot()
        print("X value at the beginning from main X= %.2f" %(robot.x.value))
        # 1. launch updateOdometry Process()
        robot.startOdometry()

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
#        robot.startOdometry()
#        robot.setSpeed(0, 0.7853981633974483)
#        print("Start : %s" % time.ctime())
#        time.sleep(2)
#        print("X value from main tmp %d" % robot.x.value)
#        robot.lock_odometry.acquire()
#        print("Odom values at main at the END: %.2f, %.2f, %.2f " % (robot.x.value, robot.y.value, robot.th.value))
#        robot.lock_odometry.release()
#        robot.stopOdometry()
        nextStep = False        
        robot.setSpeed(0, -1)
        while not nextStep:
            x,  y, theta = robot.readOdometry()
            if theta > math.pi - 0.1  and theta < math.pi + 0.1:
                nextStep = True
        robot.stopOdometry()

        # ...

#        # 8:
#        p = input()
#        robot.startOdometry()
#        # girar 90º
#        nextStep = False        
#        x,  y, theta_ini = robot.readOdometry()
#        robot.setSpeed(0, -1)
#        while not nextStep:
#            x,  y, theta = robot.readOdometry()
#            if abs(theta_ini - theta) > math.pi - 0.1  and \
#                abs(theta_ini - theta) < math.pi + 0.1:
#                nextStep = True
#                robot.setSpeed(0, 0)
#                
#        # girar medio 8
#        nextStep = False      
#        x_ini,  y_ini, theta_ini = robot.readOdometry()  
#        WxI = np.array([x_ini, y_ini, theta_ini])
#        
#        WxF = np.array([x_ini, y_ini + args.radioD * 2, theta_ini +  math.pi])
#        
#        v = 10.0
#        R = args.radioD
#        w = v / R
#        
#        robot.setSpeed(v, w)
#        while not nextStep:
#            x,  y, theta = robot.readOdometry()
#            if x > WxF[0] - 1.5  and x < WxF[0] + 1.5 and \
#               y > WxF[1] - 1.5  and y < WxF[1] + 1.5 and \
#                theta > WxF[2] - 0.1 and theta < WxF[2] + 0.1 :
#                    nextStep = True
#                    robot.setSpeed(0, 0)
#                    
#        # girar girar un circulo
#        nextStep = False      
#        x_ini,  y_ini, theta_ini = robot.readOdometry()  
#        WxI = np.array([x_ini, y_ini, theta_ini])
#        
#        WxF = np.array([x_ini, y_ini, theta_ini])
#        
#        v = 10.0
#        R = args.radioD
#        w = v / R
#        
#        robot.setSpeed(v, -w)
#        while not nextStep:
#            x,  y, theta = robot.readOdometry()
#            if x > WxF[0] - 1.5  and x < WxF[0] + 1.5 and \
#               y > WxF[1] - 1.5  and y < WxF[1] + 1.5 and \
#                theta > WxF[2] - 0.1 and theta < WxF[2] + 0.1 :
#                    nextStep = True
#                    robot.setSpeed(0, 0)
#                    
#        # girar girar el otro medio 8
#        nextStep = False      
#        x_ini,  y_ini, theta_ini = robot.readOdometry()  
#        WxI = np.array([x_ini, y_ini, theta_ini])
#        
#        WxF = np.array([x_ini, y_ini - args.radioD, theta_ini - math.pi])
#        
#        v = 10.0
#        R = args.radioD
#        w = v / R
#        
#        robot.setSpeed(v, w)
#        while not nextStep:
#            x,  y, theta = robot.readOdometry()
#            if x > WxF[0] - 1.5  and x < WxF[0] + 1.5 and \
#               y > WxF[1] - 1.5  and y < WxF[1] + 1.5 and \
#                theta > WxF[2] - 0.1 and theta < WxF[2] + 0.1 :
#                    nextStep = True
#                    robot.setSpeed(0, 0)
#                    
#        robot.stopOdometry()
#        
#        # 2º recorrido
#        p = input()
#        robot.startOdometry()
#        # girar 90º
#        nextStep = False        
#        x,  y, theta_ini = robot.readOdometry()
#        robot.setSpeed(0, -1)
#        while not nextStep:
#            x,  y, theta = robot.readOdometry()
#            if abs(theta_ini - theta) > math.pi - 0.1  and \
#                abs(theta_ini - theta) < math.pi + 0.1:
#                nextStep = True
#                robot.setSpeed(0, 0)
#                
#        # girar radio por ejemplo 10 hasta 70º
#        nextStep = False      
#        x_ini,  y_ini, theta_ini = robot.readOdometry()          
#        th_f = rb.norm_pi(theta_ini - math.radians(70))      
#        
#        v = 10.0
#        R1 = args.radioA
#        w = v / R1
#        
#        robot.setSpeed(v, -w)
#        while not nextStep:
#            x,  y, theta = robot.readOdometry()
#            if theta > th_f - 0.1 and theta < th_f + 0.1 :
#                    nextStep = True
#                    robot.setSpeed(0, 0)
#                
#        # avanzar hasta llegar al siguiente circulo
#        nextStep = False      
#        x_ini,  y_ini, theta_ini = robot.readOdometry()   
#        
#        v = 10.0
#        
#        R2 = args.radioD
#        y_f = R2 - R2 * (1 - math.cos(math.radians(20)))
#        print(y_f)
#        
#        robot.setSpeed(v, 0)
#        while not nextStep:
#            x,  y, theta = robot.readOdometry()
#            if y > y_f - 1.5  and y < y_f + 1.5 :
#                    nextStep = True
#                    robot.setSpeed(0, 0)
#                    
#        # girar 220º
#        nextStep = False      
#        x_ini,  y_ini, theta_ini = robot.readOdometry()          
#        th_f = rb.norm_pi(theta_ini - math.radians(220))
#        
#        v = 10.0
#        R2 = args.radioD
#        w = v / R2
#        
#        robot.setSpeed(v, -w)
#        while not nextStep:
#            x,  y, theta = robot.readOdometry()
#            if theta > th_f - 0.1 and theta < th_f + 0.1:
#                    nextStep = True
#                    robot.setSpeed(0, 0)
#        
#        # avanzar hasta llegar al siguiente circulo
#        nextStep = False      
#        x_ini,  y_ini, theta_ini = robot.readOdometry()   
#        
#        v = 10.0
#        
#        R1 = args.radioA
#        y_f = - R1 + R1 * (1 - math.cos(math.radians(-20)))
#        print(y_f)
#        
#        robot.setSpeed(v, 0)
#        while not nextStep:
#            x,  y, theta = robot.readOdometry()
#            if y > y_f - 1.5  and y < y_f + 1.5 :
#                    nextStep = True
#                    robot.setSpeed(0, 0)
#                    
#        # girar radio hasta llegar a posicion inicial
#        nextStep = False      
#        x_ini,  y_ini, theta_ini = robot.readOdometry()   
#        
#        v = 10.0
#        R1 = args.radioA
#        w = v / R1
#        y_f = 0
#        
#        robot.setSpeed(v, -w)
#        while not nextStep:
#            x,  y, theta = robot.readOdometry()
#            if  y > y_f - 1.5  and y < y_f + 1.5 :
#                    nextStep = True
#                    robot.setSpeed(0, 0)
                    
                

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
                        type=float, default=40.0)
    parser.add_argument("-a", "--radioA", help="Radio to perform the 8-trajectory (mm)",
                        type=float, default=20.0)
    args = parser.parse_args()

    main(args)



