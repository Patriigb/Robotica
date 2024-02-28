# Fichero python que contiene las funciones correspondientes a los movimientos del robot

# Importamos las librerias necesarias
import argparse
import numpy as np
import time
import math
import robotics as rb
from Robot import Robot

def movimento_8(robot, eps, D):
    #8:
        
    p = input()
    robot.startOdometry()
    
    #girar 90º
    nextStep = False
    x,  y, theta_ini = robot.readOdometry()
    robot.setSpeed(0, -1)
    while not nextStep:
        x,  y, theta = robot.readOdometry()
        print("th", rb.norm_pi(theta - theta_ini), "min", -math.pi/2 - 0.05, "max", -math.pi/2 + 0.05)
        if theta != 0:
            if rb.norm_pi(theta - theta_ini) > -math.pi/2 - 0.05  and \
                rb.norm_pi(theta - theta_ini) < -math.pi/2 + 0.05:
                nextStep = True
                



    #girar medio 8
    nextStep = False
    x_ini,  y_ini, theta_ini = robot.readOdometry()
    WxI = np.array([x_ini, y_ini, theta_ini])

    WxF = np.array([(x_ini + D * 2), y_ini, rb.norm_pi(theta_ini +  math.pi)])

    v = 10.0
    R = D
    w = v / R

    robot.setSpeed(v, w)
    while not nextStep:
        x,  y, theta = robot.readOdometry()
        if x > (WxF[0] - eps)  and x < (WxF[0] + eps) and \
            y > WxF[1] - eps  and y < WxF[1] + eps :
                nextStep = True
#

    # girar girar un circulo
    nextStep = False
    x_ini,  y_ini, theta_ini = robot.readOdometry()
    WxI = np.array([x_ini, y_ini, theta_ini])

    WxF = np.array([x_ini, y_ini, theta_ini])

    v = 10.0
    R = D
    w = v / R
    robot.setSpeed(v, -w)
    time.sleep(0.5)
    while not nextStep:
        x,  y, theta = robot.readOdometry()
        if x > WxF[0] - eps  and x < WxF[0] + eps and \
            y > WxF[1] - eps  and y < WxF[1] + eps :
                nextStep = True
                
    # girar girar el otro medio 8
    nextStep = False
    x_ini,  y_ini, theta_ini = robot.readOdometry()
    WxI = np.array([x_ini, y_ini, theta_ini])

    WxF = np.array([x_ini - D * 2, y_ini, theta_ini - math.pi])

    v = 10.0
    R = D
    w = v / R

    robot.setSpeed(v, w)
    while not nextStep:
        x,  y, theta = robot.readOdometry()
        if  x > (WxF[0] - eps)  and x < (WxF[0] + eps) and \
            y > WxF[1] - eps  and y < WxF[1] + eps:
                nextStep = True

    robot.stopOdometry()
#


def movimiento_cadena(robot, D, A, eps):
    # 2º recorrido
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

    B = math.asin((D - A) / dc)

    print("B", B)
    th_f = rb.norm_pi(math.pi/2 + B - theta_ini)
    print("th_f", th_f)
    v = 7.0
    R1 = A
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
    r2 = math.sqrt((dc**2) - (D - A)**2)
    
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
    R2 = D
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
    
    r2 = math.sqrt((dc**2) - (D - A)**2)
    
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
    R1 = A
    w = v / R1
    y2 = 0
    x2 = 0

    robot.setSpeed(v, -w)
    while not nextStep:
        x,  y, theta = robot.readOdometry()
        if theta > math.pi/2 - 0.1  and theta < math.pi/2 + 0.1:
                nextStep = True

    robot.stopOdometry()

