import cv2
import time
import calibrarCamara as cc
print(cv2.__version__)
cap = cv2.VideoCapture(0)

if not (cap.isOpened()):
    print("Could not open video device")

# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT,800)

# Capture frame-by-frame
ret, frame = cap.read()
img_BGR = cv2.resize(frame, (352, 240))
# Display the resulting frame
# cv2.imshow('preview',frame)

#gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
#cv2.imshow('frame', gray)

img_BGR, im_with_keypoints, keypoints_red, mask_red = cc.detectBlob(img_BGR)
distancia, area = cc.draw_blobs(img_BGR, keypoints_red, im_with_keypoints)
cv2.waitKey(0)
print(distancia, area)

cv2.imshow('frame', frame)

#guardar imagen generando un nombre que sea el timestamp
cv2.imwrite(str(time.time()) + '.jpg', frame)

cap.release()