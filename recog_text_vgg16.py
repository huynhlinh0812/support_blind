import matplotlib.pyplot as plt
import cv2
import easyocr
from pylab import rcParams
from IPython.display import Image


def rcg_text_vgg16(file_name):
	rcParams['figure.figsize'] = 8, 16
	reader = easyocr.Reader(['vi'])
	#file_name = "1.jpg"
	#Image(file_name)
	output = reader.readtext(file_name, add_margin=0.55, width_ths=0.7, link_threshold=0.8, decoder='beamsearch',blocklist='=-', detail=0)

	string=" "

	text = string.join(output)

	return text
