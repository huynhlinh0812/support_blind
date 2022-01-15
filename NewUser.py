import cv2
import sqlite3
import os
import time

cam = cv2.VideoCapture(1)

sampleNum = 0

def add_pp(name):
    start = time.time()
    os.mkdir('./train_img/' + str(name))
    save_img= "train_img/{}".format(str(name + '/'))
    while(True):
        global sampleNum
        ret, img = cam.read()
        end = time.time()
        if (end - start >= 1):
            sampleNum = sampleNum + 1
            start = end
            cv2.imwrite(str(save_img + str(sampleNum) + ".jpg"), img)
            print("Ok")

        cv2.imshow('frame', img)
        # Check xem có bấm q hoặc trên 100 ảnh sample thì thoát
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
        elif sampleNum > 20:
            break

    cam.release()
    cv2.destroyAllWindows()
