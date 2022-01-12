from Detector import *
# modelURL = "http://download.tensorflow.org/models/object_detection/tf2/20200711/efficientdet_d4_coco17_tpu-32.tar.gz"
modelURL = "http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_mobilenet_v2_fpnlite_640x640_coco17_tpu-8.tar.gz"
# modelURL = "http://download.tensorflow.org/models/object_detection/tf2/20200711/faster_rcnn_resnet152_v1_1024x1024_coco17_tpu-8.tar.gz"
classesFile = "coco.names.txt"
imagePath = "linh.jpg"
threshold = 0.3
detector = Detector()
detector.readClasses(classesFile)
detector.downloadModel(modelURL)
detector.loadModel()
#detector.predictImage(imagePath,threshold)
detector.predictVideo(0,threshold)