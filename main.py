import cv2
import cvzone
import time
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os


cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(cv2.CAP_PROP_FPS, 60)


segmentor = SelfiSegmentation(1)
prev_time = time.time()


imgList = []
listImg = os.listdir("images")

for imgPath in listImg:
    img = cv2.imread(f'images/{imgPath}')
    img = cv2.resize(img, (640, 480))
    imgList.append(img)

indexImg = 0

while True:
    success, img = cap.read()

    if not success:
        break


    imgOut = segmentor.removeBG(img, imgList[indexImg], cutThreshold=0.8)
    imgStacked = cvzone.stackImages([img, imgOut], 2, 1)


    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time


    cv2.putText(imgStacked, f"FPS: {int(fps)}", (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Image", imgStacked)

    key = cv2.waitKey(1)

    if key == ord('a'):
        indexImg = (indexImg - 1) % len(imgList)
    elif key == ord('d'):
        indexImg = (indexImg + 1) % len(imgList)
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
