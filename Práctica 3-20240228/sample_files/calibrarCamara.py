# -*- coding: utf-8 -*-
#!/usr/bin/python

# Standard imports
import cv2
import numpy as np
import os

def detectBlob(img_BGR, cmin1, cmax1, cmin2, cmax2):
    """ 
        Detects a blob in an image using the given color range.
        
        Parameters:
            img_BGR: The input BGR image to be processed.
            cmin1, cmax1: Minimum and maximum HSV values for the first channel of the color range
            cmin2, cmax2: Minimum and maximum HSV values for the second channel of the color range 
 
    """


    # HSV image
    img_HSV = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2HSV)

    # Setup default values for SimpleBlobDetector parameters.
    params = cv2.SimpleBlobDetector_Params()

    # Change thresholds
    params.minThreshold = 10
    params.maxThreshold = 500

    # Filter by Area
    params.filterByArea = True
    params.minArea = 100
    params.maxArea = 30000

    params.filterByCircularity = False
    params.filterByColor = False
    params.filterByConvexity = False
    params.filterByInertia = False

    # Create a detector with the parameters
    ver = (cv2.__version__).split('.')
    if int(ver[0]) < 3 :
        detector = cv2.SimpleBlobDetector(params)
    else :
        detector = cv2.SimpleBlobDetector_create(params)

    # Mask for red 
    redMin = cmin1
    redMax = cmax1

    # Mask for red in the other side of the color space
    redMin2 = cmin2
    redMax2 = cmax2

    mask_red=cv2.inRange(img_HSV, redMin, redMax)
    mask_red2=cv2.inRange(img_HSV, redMin2, redMax2)
    mask_red3 = mask_red + mask_red2

    # apply the mask
    red = cv2.bitwise_and(img_HSV, img_HSV, mask = mask_red3)
  
    img_BGR = cv2.cvtColor(img_HSV, cv2.COLOR_HSV2BGR)

    # detector finds "dark" blobs by default, so invert image for results with same detector
    keypoints_red = detector.detect(255-red)

    # documentation of SimpleBlobDetector is not clear on what kp.size is exactly, but it looks like the diameter of the blob.
    for kp in keypoints_red:
        print (kp.pt[0], kp.pt[1], kp.size)

    # Draw detected blobs as red circles.
    # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
    # the size of the circle corresponds to the size of blob
    im_with_keypoints = cv2.drawKeypoints(img_BGR, keypoints_red, np.array([]),
        (255,255,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    
    if keypoints_red:
        return img_BGR, im_with_keypoints, keypoints_red, mask_red3
    else:
        return img_BGR, im_with_keypoints, None, mask_red3


def  draw_blobs(img_BGR, keypoints_red, im_with_keypoints):
    """
        Draws a list of keypoints on an image.
        Parameters:
            img_BGR : The original BGR image.
            keypoints_red : A list of keypoint objects.
            im_with_keypoints : An image with drawn keypoints.
    
    """
    
    
    AREA = 12000
    kp = keypoints_red[0]

    # Centro de la imagen
    h, w = img_BGR.shape[:2]
    center = (w // 2 - 20, h // 2 + 50)
    print("Centro de la imagen", center)
    # Dibujar el centro
    cv2.circle(im_with_keypoints, center, 2, (0, 0, 0), -1)

    # Centro del blob
    x, y = int(kp.pt[0]), int(kp.pt[1])
    print("Centro del blob", x, y)
    # Dibujarlo
    cv2.circle(im_with_keypoints, (x, y), 2, (0, 0, 0), -1)

    # Calcular distancia entre centro de la imagen y centro del blob
    #distance = np.sqrt((center[0] - x)**2 + (center[1] - y)**2)
    distance = x - center[0]
    print("Distancia entre los centros",distance)

    # Calcular area del blob
    area = np.pi * (kp.size/2)**2
    print("Area del blob", area)

    # Dibujar circulo con AREA
    cv2.circle(im_with_keypoints, center, int(np.sqrt(AREA/np.pi)), (0, 255, 0), 1)

    # Diferencia de areas
    diff = AREA - area
    print("Diferencia de areas", diff)
    
# Show mask and blobs found 
    cv2.imshow("Keypoints on RED", im_with_keypoints)
    cv2.waitKey(0)
    
    
    return distance, diff

def computeDistances(img_BGR, r_area, kp):
    """
        Computes distances between the centroid of the red blob
        and the center of the camera

        Parameters:
            img_BGR : BGR image to process
            r_area : Area of the red object
            kp : Keypoints

    """
    # Centro de la imagen
    h, w = img_BGR.shape[:2]
    center = (w // 2 - 50, h // 2 + 100)
    print("Centro de la imagen", center)

    # Centro del blob
    x, y = int(kp.pt[0]), int(kp.pt[1])
    print("Centro del blob", x, y)

    # Calcular distancia entre centro de la imagen y centro del blob
    distance = x - center[0]
    print("Distancia entre los centros",distance)

    # Calcular area del blob
    area = np.pi * (kp.size/2)**2
    print("Area del blob", area)

    # Diferencia de areas
    diff = r_area - area
    print("Diferencia de areas", diff)

    return distance, diff, x, w
    

# PRUEBA:
# Obtener la lista de archivos en la carpeta
def calibrar():
    """
        Test function to detect blobs in all the photos
        in a folder and compute their distance from the camera's center.
    """
    archivos = os.listdir("../fotos")
    for archivo in archivos:
        # Read image
        img_BGR = cv2.imread("../fotos/" + archivo)

        img_BGR = cv2.resize(img_BGR, (352, 240))

        # Detect blobs
        img_BGR, im_with_keypoints, keypoints_red, mask_red = detectBlob(img_BGR)
        

        if keypoints_red:
            distancia, area = draw_blobs(img_BGR, keypoints_red, im_with_keypoints)
            if distancia < 0: 
                print("direccion izquierda")
            else:
                print("direccion derecha")
        else:
            # Buscar píxeles rojos a la izquierda o derecha de la imagen
            left_red_pixels = np.sum(mask_red[:, :mask_red.shape[1]//2])
            right_red_pixels = np.sum(mask_red[:, mask_red.shape[1]//2:])

            if left_red_pixels > 0:
                print("Píxeles rojos encontrados a la izquierda de la imagen")
            elif right_red_pixels > 0:
                print("Píxeles rojos encontrados a la derecha de la imagen")
            else:
                print("No hay")

        # Show mask and blobs found 
        cv2.imshow("Keypoints on RED", im_with_keypoints)
        cv2.waitKey(delay=1)

# PRUEBA:
# Obtener la lista de archivos en la carpeta
def calibrarFoto():
    """
        Test function to detect blobs in a specific
        photo and detect red pixels at the bottom of it
    """
    # Read image
    img_BGR = cv2.imread("prueba.jpg")

    img_BGR = cv2.resize(img_BGR, (352, 240))

    # Detect blobs
    img_BGR, im_with_keypoints, keypoints_red, mask_red = detectBlob(img_BGR)
    

    if keypoints_red:
        distancia, area = draw_blobs(img_BGR, keypoints_red, im_with_keypoints)
        if distancia < 0: 
            print("direccion izquierda")
        else:
            print("direccion derecha")
    else:
        # Buscar píxeles rojos a la izquierda o derecha de la imagen
        left_red_pixels = np.sum(mask_red[:, :mask_red.shape[1]//2])
        right_red_pixels = np.sum(mask_red[:, mask_red.shape[1]//2:])

        if left_red_pixels > 0:
            print("Píxeles rojos encontrados a la izquierda de la imagen")
        elif right_red_pixels > 0:
            print("Píxeles rojos encontrados a la derecha de la imagen")
        else:
            print("No hay")

    # Obtén las dimensiones de la imagen
    alto, ancho, _ = img_BGR.shape

    # Definir la región de interés (ROI) como la mitad inferior de la imagen
    mitad_inferior = img_BGR[alto//2:alto, :]

    # Convertir la imagen a espacio de color HSV
    hsv = cv2.cvtColor(mitad_inferior, cv2.COLOR_BGR2HSV)

    # Mask for red 
    redMin = (0, 80, 50)
    redMax = (10, 255, 255)

    # Mask for red in the other side of the color space
    redMin2 = (170, 80, 50)
    redMax2 = (180, 255, 255)

    mask_red=cv2.inRange(hsv, redMin, redMax)
    mask_red2=cv2.inRange(hsv, redMin2, redMax2)
    mask_red3 = mask_red + mask_red2

    # Contar el número de píxeles rojos en la mitad inferior
    cantidad_pixeles_rojos = cv2.countNonZero(mask_red3)

    # Mostrar la cantidad de píxeles rojos
    print("Cantidad de píxeles rojos en la mitad inferior:", cantidad_pixeles_rojos)
    print("Shape mitad_inf", mitad_inferior.shape)

    # Show mask and blobs found 
    cv2.imshow("Keypoints on RED", im_with_keypoints)
    cv2.waitKey(delay=1)

#calibrarFoto()