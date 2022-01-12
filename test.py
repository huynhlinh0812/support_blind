# import cv2

# cam = cv2.VideoCapture(1, cv2.CAP_DSHOW)

# while True:
# 	ret, frame = cam.read()
# 	iii = frame
# 	cv2.imshow('sf', iii)
# 	#cv2.imshow('image', img_cp)
# 	print(frame)

# 	if cv2.waitKey(2) == ord('q'):
# 		break

# cam.release()
# cv2.destroyAllWindows()


# import threading
# import time

# class CPUPainter:

# 	def paintwall(self):
# 		time.sleep(2)
# 		print("Threading")

# 	def __init__(self):
# 		t = threading.Thread(target=self.paintwall)
# 		t.start()

# class CPUPainter1:

# 	def paintwall(self):
# 		time.sleep(2)
# 		print("ALOOO")

# 	def __init__(self):
# 		t = threading.Thread(target=self.paintwall)
# 		t.start()

# CPUPainter()
# CPUPainter1()
# #CPUPainter()
# #CPUPainter1()h

# from Detector import *
# import threading
# import time
# import cv2

# def load_mo():
# 	modelURL = "http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_mobilenet_v2_fpnlite_640x640_coco17_tpu-8.tar.gz"
# 	classesFile = "coco.names.txt"
# 	global detector
# 	detector = Detector()
# 	detector.readClasses(classesFile)
# 	detector.downloadModel(modelURL)
# 	detector.loadModel()
# 	global check
# 	check = True
# 	print(check)


# def show_cam():
# 	cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# 	global imgg
# 	while True:
# 		ret, frame = cam.read()
# 		imgg = frame
# 		cv2.imshow("result", frame)

# 		if cv2.waitKey(1) == ord('q'):
# 			break

# 		if checkpoint == False:
# 			break
# 	cam.release()
# 	cv2.destroyAllWindows()

# def cp_image():
# 	global checkpoint
# 	checkpoint = True
# 	n = int(input())
# 	if n == 1:
# 		img = imgg
# 		checkpoint = False
# 		threshold = 0.3
# 		detector.predictImage(img,threshold)
	
# if __name__ == '__main__':
# 	load_mo()
# 	x = threading.Thread(target=show_cam, args=())
# 	y = threading.Thread(target=cp_image, args=())
# 	x.start()
# 	y.start()
# 	x.join()
# 	y.join()


# print("Hoàn thànhhhhhhhhhhh")


# st = "abc"
# stt = st[0:-1]
# print(stt)

# from Detector import *
# import threading
# import cv2

# def load_mo():
# 	modelURL = "http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_mobilenet_v2_fpnlite_640x640_coco17_tpu-8.tar.gz"
# 	classesFile = "coco.names.txt"
# 	global detector
# 	detector = Detector()
# 	detector.readClasses(classesFile)
# 	detector.downloadModel(modelURL)
# 	detector.loadModel()
# 	global check
# 	check = True
# 	print(check)

# def openn():
# 	cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# 	global frame_ob
# 	while True:
# 		ret, frame = cam.read()
# 		frame_ob = frame
# 		cv2.imshow("ans", frame)

# 		if cv2.waitKey(1) == ord('q'):
# 			break

# 		if check == False:
# 			break

# 	cam.release()
# 	cv2.destroyAllWindows()

# def detec_ob():
# 	global check
# 	check = True
# 	while True:
# 		n = input()
# 		if (n == 1):
# 			check = False
# 			threshold = 0.3
# 			#detector.predictImage(frame_ob,threshold)
# 			break

# def testt():
# 	global frame_ob
# 	for i in range(10):
# 		print("as")
# 	print(frame_ob)

# def alo():
# 	x = threading.Thread(target = openn, args=())
# 	y = threading.Thread(target = testt, args = ())
# 	x.start()
# 	y.start()
# 	x.join()
# 	y.join()

# if __name__ == '__main__':
# 	#load_mo()
# 	alo()


# lst = ['a', 'b', 'a']
# lst_name = []
# lst_count = []
# text_ob_of = "Có"

# while len(lst) != 0:
# 	# for i in range(len(lst)):
# 	# 	print(lst[i])
# 	Count = lst.count(lst[0])
# 	lst_name.append(lst[0])
# 	lst_count.append(Count)
# 	delet = lst[0]
# 	for i in range(Count):
# 		lst.remove(delet)



# for i in range(len(lst_count)):
# 	if i == len(lst_count) - 1:
# 		text_ob_of += ' ' + "và" + ' ' + str(lst_count[i]) +' ' + lst_name[i]
# 	elif i == len(lst_count) - 2:
# 		text_ob_of += ' ' + str(lst_count[i]) +' ' + lst_name[i]
# 	else:
# 		text_ob_of += ' ' + str(lst_count[i]) +' ' + lst_name[i] + ','

# print(text_ob_of)

# import time

# print("abc")
# time.sleep(2)
# print("àdafasf")





# import threading
# import time
# import cv2


# def test1():
# 	for i in range(20): #luoongf noi hoan thanh
# 		print(1)

# def test2():
# 	for i in range(30): #luong xu li
# 		print(2)

# def main2():

# 	m = int(input())
# 	if m == 1:
# 		x = threading.Thread(target=test1, args=())
# 		y = threading.Thread(target=test2, args=())
# 		x.start()
# 		y.start()
# 		x.join()
# 		y.join()

# def mainn():
	
# 	cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# 	global img
# 	n = 1
# 	while True:
# 		ret, frame = cam.read()
# 		img = frame
# 		cv2.imshow("result", frame)

# 		if n == 1:
# 			z = threading.Thread(target = main2, args = ())
# 			z.start()
# 			n = 2

# 		if cv2.waitKey(1) == ord('q'):
# 			break

# 	cam.release()
# 	cv2.destroyAllWindows()

# if __name__ == '__main__':
# 	mainn()


# Dict_email = {}

# f_email = open('./info/email.txt', 'r')
# f_email = open('./info/email.txt', 'r')
# for line in f_email:
#     index = line.find('-')
#     email_n = line[:index]
#     emaill = line[index + 1:]
#     Dict_email[email_n] = emaill

# phone_text = "0867168163"
# phone_text = "+84" + phone_text[1:]

# f_phone = open('./info/phone.txt', 'a')
# f_phone.write("123\n")
# f_phone.write("234\n")

# f_phone.close()


# lst = ['as', 're', 'gnv']
# check = "as"
# if check in lst:
# 	print('ok')
#ct_email = f_email.read()
#print(ct_email)

#list(Dict_name.keys())

# import random

# print(random.randrange(1,10))

# import random
# import NewUser
# import TrainModel
# idd = []

# f_pp = open('./info/id.txt', 'r')
# for line in f_pp:
#     idd.append(str(line))

# print(idd[0])


# id=input('Nhập mã nhân viên:')
# name=input('Nhập tên nhân viên:')
# print("Bắt đầu chụp ảnh nhân viên, nhấn q để thoát!")

# f_pp = open('./info/id.txt', 'a')
# while True:
#     id_inp = random.randrange(1,1000000)
#     if id_inp not in idd:
#         idd.append(str(id_inp))
#         inputt = str(str(id_inp) + '\n')
#         f_pp.write(inputt)
#         f_pp.close()
#         break
#     else:
#     	id_inp = random.randrange(1,1000000)

# NewUser.add_pp(str(id_inp), name)
# print("Thêm ảnh xong")
# TrainModel.train_face(True)
# print("Done Train")

import FaceRecognizer

lst = []
lst = FaceRecognizer.rcg()
print(lst)