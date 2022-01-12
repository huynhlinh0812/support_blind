from PIL import Image
import pytesseract
import argparse
import cv2
import os

def rcg_text(img):
	pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
	# Xây dựng hệ thống tham số đầu vào
	# -i file ảnh cần nhận dạng
	# -p tham số tiền xử lý ảnh (có thể bỏ qua nếu không cần). Nếu dùng: blur : Làm mờ ảnh để giảm noise, thresh: Phân tách đen trắng
	ap = argparse.ArgumentParser()
	# ap.add_argument("-i", "--image", required=True,
	# 	help="Đường dẫn đến ảnh muốn nhận dạng")
	ap.add_argument("-p", "--preprocess", type=str, default="thresh",
		help="Bước tiền xử lý ảnh")
	args = vars(ap.parse_args())

	#img = cv2.imread('1.png')
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	if args["preprocess"] == "thresh":
		gray = cv2.threshold(gray, 0, 255,
			cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

	if args["preprocess"] == "blur":
		gray = cv2.medianBlur(gray, 3)

	filename = "{}.png".format(os.getpid())
	cv2.imwrite(filename, gray)
	text = pytesseract.image_to_string(Image.open(filename),lang='vie')
	os.remove(filename)

	return text
