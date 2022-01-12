import os
import cv2
import threading
import playsound
import speech_recognition as sr
import time
import sys
import ctypes
import wikipedia
import datetime
import json
import re
import webbrowser
import smtplib
import requests
import urllib
import urllib.request as urllib2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import strftime
import pyttsx3
from youtube_search import YoutubeSearch
from collections import OrderedDict
from recognition_text import rcg_text #mã nguồn tự xây dựng
from detec_face_image import predict_gender #mã nguồn tự xây dựng
#from recog_text_vgg16 import rcg_text_vgg16
from twilio.rest import Client
import googletrans
from googletrans import Translator
from Detector import *
import process_ob
import NewUser
import TrainModel
import FaceRecognizer
import random

get_name = "Tuấn"
idd = []
Dict_email = {'tuna': "trumsc271@gmail.com", 'linh': "trumsc271@gmail.com", 'tuner': "trumsc271@gmail.com"}
Dict_phone = {'tuna': "+84944982237", 'linh': "+84944982237", 'tuner': "+84944982237"}
Dict_howto = {'cách nấu cơm': "Cho tỉ lệ gạo với nước là 1 1 rồi nấu thôi"}
path = ChromeDriverManager().install()

get_cam = 2
language_combo = ['vi-VN', 'en', 'zh-cn']
id_voices_combo = [2, 0, 1]
#2 tiếng việt, 1 tiếng trung, 0 tiếng anh
dich=Translator()

#Khai báo voice thư viện pyttsx3 tiếng việt
bot = pyttsx3.init()
rate = bot.getProperty('rate')

bot.setProperty('rate', 160)
voices = bot.getProperty("voices")

def speak(text, id_voices):
    if id_voices == 0:
        text = dich.translate(text, src="vi", dest="en")
        text = text.text
    elif id_voices == 1:
        text = dich.translate(text, src="vi", dest="zh-cn")
        text = text.text
    bot.setProperty("voice",voices[id_voices].id)
    print("Bot: " + text)
    bot.say(text)
    bot.runAndWait()

#Chức năng chuyển âm thanh thành văn bản
def get_audio(lang):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Tôi: ", end='')
        audio = r.listen(source, phrase_time_limit=5)
        try:
            text = r.recognize_google(audio, language=lang)
            print(text)
            return text
        except:
            print(". . .")
            return 0

def get_text(lang):
    for i in range(50): #thời gian nói 
        text = get_audio(lang)
        if text:
            return text.lower()
        #elif i < 20:
            #speak("Bot không nghe rõ. Bạn nói lại được không!")
    time.sleep(2)
    stop(id_voices)
    return 0

#Chức năng giao tiếp, chào hỏi
def hello(name, id_voices):
    day_time = int(strftime('%H'))
    if day_time < 12:
        speak("Chào buổi sáng bạn . bot có thể giúp được gì cho bạn ?.", id_voices)
    elif 12 <= day_time < 18:
        speak("Chào buổi chiều bạn . Bạn đã dự định gì cho chiều nay chưa.", id_voices)
    else:
        speak("Chào buổi tối bạn . Bạn đã ăn tối chưa nhỉ.", id_voices)

#Chức năng hiển thị thời gian
def get_time(text, id_voices):
    now = datetime.datetime.now()
    if "giờ" in text:
        speak('Bây giờ là %d giờ %d phút ' % (now.hour, now.minute), id_voices)
    elif "ngày" in text:
        speak("Hôm nay là ngày %d tháng %d năm %d" %
              (now.day, now.month, now.year))
    #elif "hour" in text:
        
    else:
        speak("Bot chưa hiểu ý của bạn. Bạn nói lại được không?", id_voices)


#Chức năng mở ứng dụng hệ thống, website và chức năng tìm kiếm từ khóa trên Google
def open_application(text, id_voices):
    if "google" in text:
        speak("Mở Google Chrome", id_voices)
        os.startfile('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')
    elif "word" in text:
        speak("Mở Microsoft Word", id_voices)
        os.startfile('C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE')
    elif "excel" in text:
        speak("Mở Microsoft Excel", id_voices)
        os.startfile('C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\EXCEL.EXE')
    else:
        speak("Ứng dụng chưa được cài đặt. Bạn hãy thử lại!", id_voices)

def open_website(text):
    reg_ex = re.search('mở (.+)', text)
    if reg_ex:
        domain = reg_ex.group(1)
        url = 'https://www.' + domain
        webbrowser.open(url)
        speak("Trang web bạn yêu cầu đã được mở.", id_voices)
        return True
    else:
        return False

def open_google_and_search(text, id_voices):
    search_for = text.split("kiếm", 1)[1]
    speak('Okay!', id_voices)
    driver = webdriver.Chrome(path)
    driver.get("http://www.google.com")
    que = driver.find_element_by_xpath("//input[@name='q']")
    que.send_keys(str(search_for))
    que.send_keys(Keys.RETURN)

#Chức năng gửi mail
def send_email(text, id_voices,lang):
    speak('Bạn gửi email cho ai nhỉ', id_voices)
    lst_name =  Dict_email.keys()
    while True:
        recipient = get_text(lang)
        if recipient in lst_name:
            speak('Nội dung bạn muốn gửi là gì', id_voices)
            emailto = Dict_email[recipient]
            content = get_text(lang)
            mail = smtplib.SMTP('smtp.gmail.com', 587)
            mail.ehlo()
            mail.starttls()
            mail.login('assistantmakebytl@gmail.com', 'tuanlinhiters')
            mail.sendmail('assistantmakebytl@gmail.com',
                          emailto, content.encode('utf-8'))
            mail.close()
            speak('Email của bạn vùa được gửi. Bạn check lại email nhé hihi.', id_voices)
            break
        else:
            speak('Bot không hiểu bạn muốn gửi email cho ai. Bạn nói lại được không?', id_voices)

#Chức năng tin nhắn
def chatting(lang, id_voices):
    account_sid = 'AC0ffe8ffc80fee6604da08d2241c426cf'
    auth_token = 'fed61a4df8b4fc6e62c41d35fbd49bc7'
    speak('Bạn muốn nhắn tin cho ai', id_voices)
    lst_name = Dict_phone.keys()
    while True:
        recipient = get_text(lang)
        if recipient in lst_name:
            speak('Nội dung bạn muốn gửi là gì', id_voices)
            content = get_text(lang)
            client = Client(account_sid, auth_token)
            phoneto = Dict_phone[recipient]
            message = client.messages \
                .create(
                     body= content,
                     from_='+18507908034',
                     to= phoneto
                 )
            speak('tin nhắn của bạn đã được gửi.', id_voices)
            break
        else:
            speak('Danh bạ của bản không có số của người này', id_voices)

#Chức năng dự báo thời tiết
def current_weather(id_voices, lang):
    speak("Bạn muốn xem thời tiết ở đâu ạ.", id_voices)
    ow_url = "http://api.openweathermap.org/data/2.5/weather?"
    city = get_text(lang)
    if not city:
        pass
    api_key = "fe8d8c65cf345889139d8e545f57819a"
    call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
    response = requests.get(call_url)
    data = response.json()
    if data["cod"] != "404":
        city_res = data["main"]
        current_temperature = city_res["temp"]
        current_pressure = city_res["pressure"]
        current_humidity = city_res["humidity"]
        suntime = data["sys"]
        sunrise = datetime.datetime.fromtimestamp(suntime["sunrise"])
        sunset = datetime.datetime.fromtimestamp(suntime["sunset"])
        wthr = data["weather"]
        weather_description = wthr[0]["description"]
        now = datetime.datetime.now()
        content = """
        Hôm nay là ngày {day} tháng {month} năm {year}
        Mặt trời mọc vào {hourrise} giờ {minrise} phút
        Mặt trời lặn vào {hourset} giờ {minset} phút
        Nhiệt độ trung bình là {temp} độ C
        Áp suất không khí là {pressure} héc tơ Pascal
        Độ ẩm là {humidity}%
        Trời hôm nay quang mây. Dự báo mưa rải rác ở một số nơi.""".format(day = now.day,month = now.month, year= now.year, hourrise = sunrise.hour, minrise = sunrise.minute,
                                                                           hourset = sunset.hour, minset = sunset.minute, 
                                                                           temp = current_temperature, pressure = current_pressure, humidity = current_humidity)

        speak(content, id_voices)
        time.sleep(15)
    else:
        speak("Không tìm thấy địa chỉ của bạn", id_voices)

#Chức năng phát nhạc trên Youtube
def play_song(id_voices, lang):
    speak('Xin mời bạn chọn tên bài hát', id_voices)
    mysong = get_text(lang)
    while True:
        result = YoutubeSearch(mysong, max_results=3). to_dict()
        if result:
            break
    url = 'https://www.youtube.com' + result[0]['url_suffix']
    webbrowser.open(url)
    speak("Bài hát bạn yêu cầu đã được mở.", id_voices)

#Chức năng nghe tin tức
def play_news(id_voices):
    speak('Xin mời bạn chọn tiêu đề')
    mynews = get_text()
    while True:
        result = YoutubeSearch(mynews, max_results=3). to_dict()
        if result:
            break
    url = 'https://www.youtube.com' + result[0]['url_suffix']
    webbrowser.open(url)
    speak("Bài hát bạn yêu cầu đã được mở.", id_voices)

#Chức năng đọc báo ngày hôm nay
def read_news(id_voices):
    speak("Bạn muốn đọc báo về gì", id_voices)
    
    queue = get_text()
    params = {
        'apiKey': '30d02d187f7140faacf9ccd27a1441ad',
        "q": queue,
    }
    api_result = requests.get('http://newsapi.org/v2/top-headlines?', params)
    api_response = api_result.json()
    print("Tin tức")

    for number, result in enumerate(api_response['articles'], start=1):
        print(f"""Tin {number}:\nTiêu đề: {result['title']}\nTrích dẫn: {result['description']}\nLink: {result['url']}
    """)
        if number <= 3:
            webbrowser.open(result['url'])

#Chức năng tìm định nghĩa trên từ điển wikipedia
def tell_me_about(id_voices, lang):
        try:
            speak("Bạn muốn nghe về gì ạ", id_voices)
            text = get_text(lang)
            contents = wikipedia.summary(text).split('\n')
            speak(contents[0], id_voices)
            time.sleep(10)
            # for content in contents[1:]:
            #     speak("Bạn muốn nghe thêm không", id_voices)
            #     ans = get_text()
            #     if "có" not in ans or "yes" not in ans:
            #         break    
            #     speak(content, id_voices)
            #     time.sleep(30)

            speak('Cảm ơn bạn đã lắng nghe!!!', id_voices)
        except:
            speak("Bot không định nghĩa được thuật ngữ của bạn. Xin mời bạn nói lại", id_voices)

#Nhận diện chữ
def show_cam():
    cam = cv2.VideoCapture(get_cam, cv2.CAP_DSHOW)
    global img_rcg_text
    while True:
        ret, frame = cam.read()
        img_rcg_text = frame
        cv2.imshow("ASSISTAN", frame)

        if cv2.waitKey(1) == ord('q'):
            break

        if check == False:
            break
    cam.release()
    cv2.destroyAllWindows()

def recog_text():
    global lang_
    global check
    global img_rcg_text
    check = True
    while True:
        text_of_recognition = get_text(lang_)
        if "hoàn thành" in text_of_recognition or "complete" in text_of_recognition:
            img_rcg_off = img_rcg_text
            check = False
            global text_rcg
            text_rcg = rcg_text(img_rcg_off)
            #text_rcg = rcg_text_vgg16(img_rcg_off)
            break
#----- Nhận dạng nam nữ
def show_cam_face():
    cam = cv2.VideoCapture(get_cam, cv2.CAP_DSHOW)
    global img_rcg_text
    while True:
        ret, frame = cam.read()
        img_rcg_text = frame
        cv2.imshow("ASSISTAN", frame)

        if cv2.waitKey(1) == ord('q'):
            break

        if check_face == False:
            break
    cam.release()
    cv2.destroyAllWindows()

def detec_face():
    global check_face
    check_face = True
    while True:
        text_face = get_text(lang_)
        if "hoàn thành" or "complete" in text_face:
            img_face_off = img_rcg_text
            check_face = False
            lst_face = predict_gender(img_face_off)
            global text_face_rcg
            text_face_rcg  = "có {} nam và {} nữ ở phía trước".format(lst_face[0], lst_face[1])
            break

#----- Nhận dạng đối tượng
def show_cam_ob():
    cam = cv2.VideoCapture(get_cam, cv2.CAP_DSHOW)
    global imgg
    while True:
        ret, frame = cam.read()
        imgg = frame
        cv2.imshow("result", frame)

        if cv2.waitKey(1) == ord('q'):
            break

        if checkpoint == False:
            break
    cam.release()
    cv2.destroyAllWindows()

def detec_ob():
    global checkpoint
    checkpoint = True
    while True:
        check_detec_ob = get_text(lang_)
        if "hoàn thành" in check_detec_ob:
            img = imgg
            checkpoint = False
            threshold = 0.3
            lst_detec_ob = detector.predictImage(img,threshold)
            global text_detec_ob
            text_detec_ob = process_ob.process(lst_detec_ob, lang_)
            break

#Xác định người quen
# def check__():
#     global checkpoint
#     checkpoint = True
#     while True:
#         get_text_pp = get_text(lang_)
#         if "hoàn thành" in get_text_pp:
#             checkpoint = False
#             break

def recog_pp(lang, id_voices):
    text_recog_pp = "Đằng trước là"
    namepp = FaceRecognizer.rcg()
    for i in range(len(namepp)):
        if len(namepp) == 1:
            text_recog_pp += ' ' + namepp[i]
        else:
            if i == len(lst_count) - 1:
                text_recog_pp += ' ' + "và" + ' ' + namepp[i]
            elif i == len(lst_count) - 2:
                text_recog_pp += ' ' + namepp[i]
            else:
                text_recog_pp += ' ' + namepp[i] + ','

    speak(text_recog_pp, id_voices)

#Thêm người quen
def add_train_pp(lang, id_voices):
    speak("Bạn muốn thêm ai vào danh sách người quen", id_voices)
    text_add_pp = get_text(lang)
    f_pp = open('./info/id.txt', 'a')
    while True:
        id_inp = random.randrange(1,1000000)
        if id_inp not in idd:
            idd.append(str(id_inp))
            inputt = str(str(id_inp) + '\n')
            f_pp.write(inputt)
            f_pp.close()
            break
        else:
            id_inp = random.randrange(1,1000000)

    NewUser.add_pp(str(id_inp), text_add_pp)
    print("Thêm ảnh xong")
    TrainModel.train_face(True)
    print("Done Train")


def stop(id_voices):
    speak("Hẹn gặp lại bạn sau!", id_voices)
# def end_speak(id_voices):
#     speak("bạn cần bot giúp gì nữa không ", id_voices)

def load_model_ob():
    modelURL = "http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_mobilenet_v2_fpnlite_640x640_coco17_tpu-8.tar.gz"
    classesFile = "coco.names.txt"
    global detector
    detector = Detector()
    detector.readClasses(classesFile)
    detector.downloadModel(modelURL)
    detector.loadModel()

def add_phone(lang, id_voices):
    #hỏi xem cần thêm ai, phone như thế nào ---> lưu vào dict à file
    #đọc dữ liệu từ file ---> lưu vào Dict
    speak("Mời bạn đọc tên người muốn thêm", id_voices)
    text_phone_n = get_text(lang)
    speak("Số điện thoại là", id_voices)
    text_phone = get_text(lang)
    text_phone = "+84" + text_phone[1:]
    Dict_phone[text_phone_n] = text_phone

    f_phone = open('./info/phone.txt', 'a')
    inputt = str(text_phone_n + '-' + text_phone + '\n')
    f_phone.write(inputt)
    f_phone.close()

def add_email(lang, id_voices):
    #hỏi xem cần thêm ai, email như thế nào ---> lưu vào dict à file
    speak("Mời bạn đọc tên người muốn thêm", id_voices)
    text_email_n = get_text(lang)
    speak("Địa chỉ email là ", id_voices)
    text_email = get_text(lang)
    Dict_email[text_email_n] = text_email

    f_email = open('./info/email.txt', 'a')
    inputt = str(text_email_n + '-' + text_email + '\n')
    f_email.write(inputt)
    f_email.close()

def learn(lang, id_voices):
    #hỏi xem cần học thêm cái gì ---> tạo file lưu cách thực hiện ---> Lưu giá trị Dict để kiểm tra --->
    speak("Bạn muốn cho tôi học về vấn đề gì", id_voices)
    text_learn = get_text(lang)
    speak("Okay bạn hướng dẫn mình với nhé", id_voices)
    text_how_lear = get_text(lang)
    Dict_howto[text_learn] = text_how_lear

    f_email = open('./info/learnhowto.txt', 'a')
    inputt = str(text_learn + '-' + text_how_lear + '\n')
    f_email.write(inputt)
    f_email.close()

# def post_sever():
#     #lưu ảnh về ---> gửi lên sever ---> xóa tại local

def Init():
    #lấy thong tin từ file ra
    f_email = open('./info/email.txt', 'r')
    for line in f_email:
        index = line.find('-')
        email_n = line[:index]
        emaill = line[index + 1:]
        Dict_email[email_n] = emaill

    f_phone = open('./info/phone.txt', 'r')
    for line in f_phone:
        index = line.find('-')
        phone_n = line[:index]
        phonee = line[index + 1:]
        Dict_phone[email_n] = phonee

    f_pp = open('./info/id.txt', 'r')
    for line in f_pp:
        idd.append(str(line))

    print("Init finish")

#------------MAIN
def assistant_VN(lang, id_voices):
    langwiki = 'vi'
    if id_voices == 0:
        langwiki = "en"
    wikipedia.set_lang(langwiki)
    language = langwiki
    name = get_name
    if name:
        speak("Chào bạn {}".format(name), id_voices)
        #speak("Tôi tên là {}. {} có thể giúp gì cho bạn.".format(name_bot, name_bot))
        while True:
            text = get_text(lang)
            if "dừng" in text or "tạm biệt" in text or "bye" in text or "stop" in text:
                stop(id_voices)
                break
            # elif "xin chào trợ lý ảo" or "hello assistance" in text:
            #     hello(name, id_voices)
            elif "mấy giờ" in text or "what time" in text:
                get_time(text, id_voices)
                time.sleep(1)
                speak("Bạn cần giúp gì nữa ạ?", id_voices)
            # elif "mở" in text:
            #     if 'mở google và tìm kiếm' in text:
            #         open_google_and_search(text, id_voices)
            #         time.sleep(1)
            #         speak("Bạn cần giúp gì nữa ạ?", id_voices)
            #     elif "." in text:
            #         open_website(text, id_voices)
            #         time.sleep(1)
            #         speak("Bạn cần giúp gì nữa ạ?", id_voices)
            #     else:
            #         open_application(text, id_voices)
            #         time.sleep(1)
            #         speak("Bạn cần giúp gì nữa ạ?", id_voices)
            elif "thêm email" in text or "add mail" in text:
                add_email()
            elif "email" in text or "mail" in text or "gmail" in text:
                send_email(text, id_voices, lang)
                time.sleep(1)
                speak("Bạn cần giúp gì nữa ạ?", id_voices)
                time.sleep(1)
                speak("Bạn cần giúp gì nữa ạ?", id_voices)
            elif "thời tiết" in text or "weather" in text:
                current_weather(id_voices, lang)
                time.sleep(1)
                speak("Bạn cần giúp gì nữa ạ?", id_voices)
            elif "nghe nhạc" in text or "music" in text:
                play_song(id_voices, lang)
                time.sleep(1)
                speak("Bạn cần giúp gì nữa ạ?", id_voices)
            elif "nghe tin tức" in text:
                play_news(id_voices)
                time.sleep(1)
                speak("Bạn cần giúp gì nữa ạ?", id_voices)
            elif "tin nhắn" in text or "message" in text:
                chatting(lang,id_voices)
                time.sleep(1)
                speak("Bạn cần giúp gì nữa ạ?", id_voices)
            elif "thêm số điện thoại" in text or "add phone" in text:
                add_phone(lang, id_voices)
                time.sleep(1)
                speak("Bạn cần giúp gì nữa ạ?", id_voices)
            elif "đọc báo" in text or "read news" in text:
                read_news(id_voices)
                time.sleep(1)
                speak("Bạn cần giúp gì nữa ạ?", id_voices)
            elif "tra từ điển" in text or "define" in text:
                tell_me_about(id_voices, lang)
                time.sleep(1)
                speak("Bạn cần giúp gì nữa ạ?", id_voices)
            elif "đọc tài liệu" in text or "document" in text:
                speak("Hãy nói hoàn thành khi sẳn sàng", id_voices)
                x = threading.Thread(target=show_cam, args=())
                y = threading.Thread(target=recog_text, args=())
                x.start()
                y.start()
                x.join()
                y.join()
                text_new = text_rcg[0:-1]
                speak(text_new, id_voices)
                time.sleep(1)
                speak("Bạn cần giúp gì nữa ạ?", id_voices)
            elif "bao nhiêu nam và bao nhiêu nữ" in text or "how many people are there"in text:
                speak("Hãy nói hoàn thành khi sẵn sàng", id_voices)
                x = threading.Thread(target=show_cam_face, args=())
                y = threading.Thread(target=detec_face, args=())
                x.start()
                y.start()
                x.join()
                y.join()
                speak(text_face_rcg, id_voices)
                time.sleep(1)
                speak("Bạn cần giúp gì nữa ạ?", id_voices)
            elif "có gì" in text:
                speak("Hãy nói hoàn thành khi sẵn sàng", id_voices)
                x = threading.Thread(target = show_cam_ob, args = ())
                y = threading.Thread(target = detec_ob, args = ())
                x.start()
                y.start()
                x.join()
                y.join()
                speak(text_detec_ob, id_voices)
                time.sleep(1)
                speak("Bạn cần giúp gì nữa ạ?", id_voices)
            elif "thêm người liên hệ" in text:
                add_train_pp(lang, id_voices)
                time.sleep(1)
                speak("Thêm hoàn thành", id_voices)
                speak("Bạn cần giúp gì nữa ạ?", id_voices)
                time.sleep(1)
                speak("Bạn cần giúp gì nữa ạ?", id_voices)
            elif "phía trước là ai" in text:
                recog_pp(lang, id_voices)
                time.sleep(1)
                speak("Bạn cần giúp gì nữa ạ?", id_voices)
            elif "thêm hướng dẫn" in text or "tutorial" in text:
                learn(lang, id_voices)
                time.sleep(1)
                speak("Bạn cần giúp gì nữa ạ?", id_voices)
            elif "hướng dẫn" in text or "more tutorial" in text:
                lst_howto = Dict_howto.keys()
                speak("Bạn cần hướng dẫn về vấn đề gì", id_voices)
                get_help = get_text(lang)
                if get_help in lst_howto:
                    speak(Dict_howto[get_help], id_voices)

                time.sleep(1)
                speak("Bạn cần giúp gì nữa ạ?", id_voices)
            else:
                speak("Bạn cần giúp gì ạ?", id_voices)

if __name__ == '__main__':
    load_model_ob()
    Init()
    global lang_
    speak("Xin mời bạn chọn ngôn ngữ:", id_voices_combo[0])
    choose_lang =  get_text("vi-VN")
    if 'tiếng việt' in choose_lang:
        lang_ = language_combo[0]
        assistant_VN(language_combo[0], id_voices_combo[0])
    elif 'tiếng anh' in choose_lang:
        lang_ = language_combo[1]
        assistant_VN(language_combo[1], id_voices_combo[1])
    elif 'tiếng trung' in choose_lang:
        lang_ = language_combo[2]
        assistant_VN(language_combo[2], id_voices_combo[2])
    else:
        speak("Không tìm thấy ngôn ngữ bạn yêu cầu", id_voices_combo[0])