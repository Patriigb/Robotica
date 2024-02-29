# Fichero python que contiene las funciones correspondientes a los movimientos del robot

# Importamos las librerias necesarias
import argparse
import numpy as np
import time
import math
import robotics as rb
from Robot import Robot

def movimento_8(robot, eps, D):
    """Realiza la primera trayectoria (8) del proyecto

    Args:
        robot
        eps: error principal en las distancias
        D: radio D
    """
    #8:    
    #girar 90º
    p = input()
    time.sleep(3)
        
    robot.startOdometry()
    nextStep = False
    x,  y, theta_ini = robot.readOdometry()
    robot.setSpeed(0, -1.5)
    while not nextStep:
        x,  y, theta = robot.readOdometry()
        if theta != 0:
            if rb.norm_pi(theta - theta_ini) > -math.pi/2 - 0.05  and \
                rb.norm_pi(theta - theta_ini) < -math.pi/2 + 0.05:
                nextStep = True
                



    #girar medio 8
    nextStep = False
    x_ini,  y_ini, theta_ini = robot.readOdometry()
    WxI = np.array([x_ini, y_ini, theta_ini])

    WxF = np.array([(x_ini + D * 2), y_ini, rb.norm_pi(theta_ini +  math.pi)])

    v = 15.0
    R = D
    w = v / R

    robot.setSpeed(v, w)
    while not nextStep:
        x,  y, theta = robot.readOdometry()
        if x > (WxF[0] - eps)  and x < (WxF[0] + eps) and \
            y > WxF[1] - eps  and y < WxF[1] + eps and \
                theta > math.pi/2 - 0.2 and theta < math.pi/2 + 0.2:
                nextStep = True
#

    # girar girar un circulo
    nextStep = False
    x_ini,  y_ini, theta_ini = robot.readOdometry()
    WxI = np.array([x_ini, y_ini, theta_ini])

    WxF = np.array([x_ini, y_ini, theta_ini])

    v = 15.0
    R = D
    w = v / R
    robot.setSpeed(v, -w)
    time.sleep(0.5)
    while not nextStep:
        x,  y, theta = robot.readOdometry()
        if x > WxF[0] - eps  and x < WxF[0] + eps and \
            y > WxF[1] - eps  and y < WxF[1] + eps and \
            theta > math.pi/2 - 0.2 and theta < math.pi/2 + 0.2:
                nextStep = True
                
    # girar girar el otro medio 8
    nextStep = False
    x_ini,  y_ini, theta_ini = robot.readOdometry()
    WxI = np.array([x_ini, y_ini, theta_ini])

    WxF = np.array([x_ini - D * 2, y_ini, theta_ini - math.pi])

    v = 15.0
    R = D
    w = v / R

    robot.setSpeed(v, w)
    while not nextStep:
        x,  y, theta = robot.readOdometry()
        if  x > (WxF[0] - eps)  and x < (WxF[0] + eps) and \
            y > WxF[1] - eps  and y < WxF[1] + eps and\
            theta > -math.pi/2 - 0.2 and theta < -math.pi/2 + 0.2:
                nextStep = True

    robot.stopOdometry()
#


def movimiento_cadena(robot, D, A, eps):
    """Realiza la segunda trayectoria (cadena) del proyecto

    Args:
        robot
        D: radio D
        A: radio A
        eps (_type_): error principal para las distancias
    """
    # 2º recorrido
    dc = 50.0 
    # girar 90º
    p = input()
    time.sleep(3)
        
    robot.startOdometry()
    nextStep = False
    x_ini,  y_ini, theta_ini = robot.readOdometry()
    robot.setSpeed(0, 1.5)
    while not nextStep:
        x,  y, theta = robot.readOdometry()
        if theta != 0:
            if x > x_ini - eps and x < x_ini + eps and \
                y > y_ini - eps and y < y_ini + eps and \
                rb.norm_pi(theta - theta_ini) > math.pi/2 - 0.05  and \
                rb.norm_pi(theta - theta_ini) < math.pi/2 + 0.05:
                nextStep = True
#
#        # girar radio por ejemplo 10 hasta beta
    nextStep = False
    x_ini,  y_ini, theta_ini = robot.readOdometry()

    B = math.asin((D - A) / dc)

    th_f = rb.norm_pi(math.pi/2 + B - theta_ini)
    v = 10.0
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

    v = 15.0
    r2 = math.sqrt((dc**2) - (D - A)**2)
    
    x2 = x_ini + r2 * math.cos(B)
    y2 = y_ini + r2 * math.sin(B)

    robot.setSpeed(v, 0)
    while not nextStep:
        x,  y, theta = robot.readOdometry()
        if x > x2 - eps  and x < x2 + eps and \
            y > y2 - 6  and y < y2 + 6 and \
            theta > theta_ini - 0.3 and theta < theta_ini + 0.3:
                nextStep = True

    
#
    # girar pi + B + B
    nextStep = False
    x_ini,  y_ini, theta_ini = robot.readOdometry()
    
    th_f = rb.norm_pi(theta_ini - 2*B - math.pi)
    v = 15.0
    R2 = D
    w = v / R2

    robot.setSpeed(v, -w)
    while not nextStep:
        x,  y, theta = robot.readOdometry()
        if theta > th_f - 0.15 and theta < th_f + 0.15:
                nextStep = True
                
#
#        # avanzar hasta llegar al siguiente circulo
    nextStep = False
    x_ini,  y_ini, theta_ini = robot.readOdometry()

    v = 15.0
    
    r2 = math.sqrt((dc**2) - (D - A)**2)
    
    x2 = x_ini - r2 * math.cos(B)
    y2 = y_ini + r2 * math.sin(B)


    robot.setSpeed(v, 0)
    while not nextStep:
        x,  y, theta = robot.readOdometry()
        if x > x2 - eps - 1  and x < x2 + eps +1 and \
            y > y2 - 6  and y < y2 + 6 and \
            theta > theta_ini - 0.3 and theta < theta_ini + 0.3:
                nextStep = True
#
    
#        # girar radio hasta llegar a posicion inicial
    nextStep = False
    x_ini,  y_ini, theta_ini = robot.readOdometry()

    v = 10.0
    R1 = A
    w = v / R1
    y2 = 0
    x2 = 0

    robot.setSpeed(v, -w)
    while not nextStep:
        x,  y, theta = robot.readOdometry()
        if x > x2 - eps - 1  and x < x2 + eps +1 and \
            y > y2 - 6  and y < y2 + 6 and \
            theta > math.pi/2 - 0.1  and theta < math.pi/2 + 0.1:
                nextStep = True

    robot.stopOdometry()

