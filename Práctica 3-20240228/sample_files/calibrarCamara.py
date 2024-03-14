# -*- coding: utf-8 -*-
#!/usr/bin/python

# Standard imports
import cv2
import numpy as np
import os

def detectBlob(img_BGR):

    # HSV image
    img_HSV = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2HSV)

    # Setup default values for SimpleBlobDetector parameters.
    params = cv2.SimpleBlobDetector_Params()

    # Change thresholds
    params.minThreshold = 10
    params.maxThreshold = 500

    # Filter by Area
    params.filterByArea = True
    params.minArea = 200
    params.maxArea = 60000

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
    redMin = (0, 100, 80)
    redMax = (10, 255, 255)

    # Mask for red in the other side of the color space
    redMin2 = (170, 100, 80)
    redMax2 = (180, 255, 255)

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
    """Draws a list of keypoints on an image."""
    
    
    AREA = 50000
    kp = keypoints_red[0]

    # Centro de la imagen
    h, w = img_BGR.shape[:2]
    center = (w // 2 - 50, h // 2 + 100)
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

    return distance, diff
    

# PRUEBA:
# Obtener la lista de archivos en la carpeta
def calibrar():
    archivos = os.listdir("../fotos")
    for archivo in archivos:
        # Read image
        img_BGR = cv2.imread("../fotos/" + archivo)

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

