import numpy as np
from math import cos, radians, sin, atan2, degrees
import matplotlib.pyplot as plt

# Function for homogeneous transformation
def hom(x):
    rad = x[2]
    T = np.array([[cos(rad), -sin(rad), x[0]],
         [sin(rad),  cos(rad), x[1]],
         [0, 0, 1]])
    
    return T

# Function to calculate location and orientation
def loc(T):
    dx = T[0][2]
    dy = T[1][2]
    th = atan2(T[1][0], T[0][0])
    
    
    return np.array([dx, dy, th])

# Normalize angle to -pi to pi
def norm_pi(angle):
    while abs(angle) > np.pi:
        if angle < 0:
            angle += np.pi * 2
        else:
            angle -= np.pi * 2
            
    return angle

# Simula movimiento del robot con vc=[v,w] en T seg. desde xWR
def simubot(vc,xWR,T):
  if vc[1]==0:   # w=0
      xRk=np.array([vc[0]*T, 0, 0])
  else:
      R=vc[0]/vc[1]
      dtitak=vc[1]*T
      titak=norm_pi(dtitak);
      xRk=np.array([R* sin(titak), R*(1- cos(titak)), titak])  

  xWRp=loc(np.dot(hom(xWR),hom(xRk)))   # nueva localizaci�n xWR
  return xWRp

# Dibuja robot en location_eje con color (c) y tamano (p/g)
def dibrobot(loc_eje,c,tamano):
  if tamano=='p':
    largo=0.1
    corto=0.05
    descentre=0.01
  else:
    largo=0.5
    corto=0.25
    descentre=0.05

  trasera_dcha=np.array([-largo,-corto,1])
  trasera_izda=np.array([-largo,corto,1])
  delantera_dcha=np.array([largo,-corto,1])
  delantera_izda=np.array([largo,corto,1])
  frontal_robot=np.array([largo,0,1])
  tita=loc_eje[2]
  Hwe=np.array([[np.cos(tita), -np.sin(tita), loc_eje[0]],
             [np.sin(tita), np.cos(tita), loc_eje[1]],
              [0,        0 ,        1]])
  Hec=np.array([[1,0,descentre],
              [0,1,0],
              [0,0,1]])
  extremos=np.array([trasera_izda, delantera_izda, delantera_dcha, trasera_dcha, trasera_izda, frontal_robot, trasera_dcha])
  robot=np.dot(Hwe,np.dot(Hec,np.transpose(extremos)))
  plt.plot(robot[0,:], robot[1,:], c)
  
  