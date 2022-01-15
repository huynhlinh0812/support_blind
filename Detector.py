import cv2
import time
import os
import tensorflow as tf
import numpy as np
from tensorflow.python.keras.utils.data_utils import get_file

np.random.seed(123)
class Detector:
    def __init__(self):
        pass

    def readClasses(self,classesFilePath):
        with open(classesFilePath,'r') as f:
            self.classesList = f.read().splitlines()
            
            # Color list
        self.colorList = np.random.uniform(low=0,high=255,size=(len(self.classesList),3))

    def downloadModel(self,modelURL):
        filename = os.path.basename(modelURL)
        self.modelName = filename[:filename.index('.')]
        self.cacheDir = ".\pretrained_models"
        #os.makedirs(self.cacheDir,exist_ok=True)

        #get_file(fname=filename,
        #         origin=modelURL,cache_dir=self.cacheDir,cache_subdir="checkpoints",extract=True)

    def loadModel(self):
        print("Loading Model "+self.modelName)
        tf.keras.backend.clear_session()
        self.model = tf.saved_model.load(os.path.join(self.cacheDir,"checkpoints",self.modelName,"saved_model"))
        print("Model "+ self.modelName +" load successfully ...")
    def createBoiundingBox(self,image,threshold=0.5):
        inputTensor = cv2.cvtColor(image.copy(),cv2.COLOR_BGR2RGB)
        inputTensor = tf.convert_to_tensor(inputTensor,dtype=tf.uint8)
        inputTensor = inputTensor[tf.newaxis,...]
        detections =self.model(inputTensor)
        bboxs = detections['detection_boxes'][0].numpy()
        classScores = detections['detection_scores'][0].numpy()
        classIndexs = detections['detection_classes'][0].numpy().astype(np.int32)

        W,H,C = image.shape
        bboxIdx = tf.image.non_max_suppression(boxes=bboxs,scores=classScores,max_output_size=500,iou_threshold=threshold,score_threshold=threshold)

        lst_ob = []

        print(bboxIdx)
        if len(bboxIdx!=0):
            for i in bboxIdx:
                #bbox = tuple(bboxs[i].tolist())
                classConfidence = round(100*classScores[i])
                classIndex = classIndexs[i]

                classLabelText = self.classesList[classIndex]
                #classColor = self.colorList[classIndex]

                #displayText = f"{classLabelText},{classConfidence}%"

                lst_ob.append(classLabelText)

                # # xmin,ymin,xmax,ymax = bbox
                # ymin,xmin,ymax,xmax = bbox
                # xmin,xmax,ymin,ymax = (int(xmin*W),int(xmax*H),int(ymin*W),int(ymax*H))
                # cv2.rectangle(image,(xmin,ymin),(xmax,ymax),color=classColor,thickness=1)
                # cv2.putText(image,displayText,(xmin,ymin-10),cv2.FONT_HERSHEY_PLAIN,1,classColor,2)

                # ################################################
                # Linewidth = min(int((xmax-xmin)*0.2),int((ymax-ymin)*0.2))

                # cv2.line(image,(xmin,ymin),(xmin+Linewidth,ymin),classColor,thickness=5)
                # cv2.line(image, (xmin, ymin), (xmin , ymin+ Linewidth), classColor, thickness=5)

                # cv2.line(image, (xmax, ymin), (xmax - Linewidth, ymin), classColor, thickness=5)
                # cv2.line(image, (xmax, ymin), (xmax , ymin+ Linewidth), classColor, thickness=5)

                # cv2.line(image, (xmin, ymax), (xmin + Linewidth, ymax), classColor, thickness=5)
                # cv2.line(image, (xmin, ymax), (xmin , ymax-Linewidth), classColor, thickness=5)

                # cv2.line(image, (xmax, ymax), (xmax - Linewidth, ymax), classColor, thickness=5)
                # cv2.line(image, (xmax, ymax), (xmax , ymax-Linewidth), classColor, thickness=5)


        return lst_ob
    def predictImage(self,imagePath,threshold=None):
        image = imagePath #cv2.imread(imagePath)
        bboxImage = self.createBoiundingBox(image,threshold)
        return bboxImage
        #cv2.imwrite(self.modelName+".jpg",bboxImage)
        #cv2.imshow("Result",bboxImage)
        #cv2.waitKey(0)

    def predictVideo(self,videoPath,threshold=None):
        cap = cv2.VideoCapture(videoPath)
        if (cap.isOpened()==False):
            print("Error openning file...?")

        starttime=0
        while (cap.isOpened()):
            (success, image) = cap.read()
            currenttime = time.time()
            fps = 1/(currenttime- starttime)
            starttime = currenttime

            bboxImage = self.createBoiundingBox(image, threshold)

            cv2.putText(bboxImage,"FPS:"+str(int(fps)),(50,90),cv2.FONT_HERSHEY_PLAIN,2,(0,255,255),3)
            cv2.imshow('frame', bboxImage)
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break
        cap.release()
        cv2.destroyWindow()
