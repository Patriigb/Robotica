import numpy as np
AREA = 6000

def trackObject(self, colorRangeMin=[0,0,0], colorRangeMax=[255,255,255]):
    finished = False 
    targetFound = False 
    targetPositionReached = False 
    while not finished: 
    # 1. search the most promising blob 
        # calcular blob en la imagen (get_color_blobs) y devolver img_BGR, kp
        
        # si no hay blob, girar el robot
        # si hay blob, calcular distancia y area (targetFound = True)

        # Centro de la imagen
        h, w = img_BGR.shape[:2]
        center = (w // 2, h // 2)
        print("Centro de la imagen", center)

        # Centro del blob
        x, y = int(kp.pt[0]), int(kp.pt[1])
        print("Centro del blob", x, y)

        # Calcular distancia entre centro de la imagen y centro del blob
        distance = np.sqrt((center[0] - x)**2 + (center[1] - y)**2)
        print("Distancia entre los centros",distance)

        # Calcular area del blob
        area = np.pi * (kp.size/2)**2
        print("Area del blob", area)

        # Diferencia de areas
        diff = AREA - area
        print("Diferencia de areas", diff)


        while not targetPositionReached: 
        # 2. decide v and w for the robot to get closer to target position 
            # Si la distancia es negativa?, girar a la derecha (w < 0)
            # Si es positiva?, girar a la izquierda (w > 0)

            # Si la diferencia de areas es muy grande, acercarse más rápido con v mayor
            # Si es muy pequeña, acercarse más lento con v menor
            # Si es negativa, alejarse (v < 0)

            if distance > 10 and diff > 10: # cambiar valores
                targetPositionReached  = True 
                finished = True 
    return finished 


def catch(self): 
    # decide the strategy to catch the ball once you have reached the target position 
    # Avanzar un poco
    # Girar el motor de la cesta
    

