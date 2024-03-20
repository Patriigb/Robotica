Para detectar la pelota roja en la escena hemos creado el archivo calibrarCamara.py
En este se encuentran las funciones que se llaman desde Robot.py:
    - detectBlob: detecta los blobs de la escena dados un rango de colores
    - computeDistances: calcula la distancia y area entre el blob y la posicion final
            que se busca