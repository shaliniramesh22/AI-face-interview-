
import numpy as np
from keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense
from keras.models import Sequential
# from keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing.image import ImageDataGenerator

import ar_master
from exam_data import exam_demo

mm= ar_master.master_flask_code()



import os
import speech_recognition as sr
import cv2
import threading
import sentiment_classification
train_dir = 'data/train'
val_dir = 'data/test'
num_train = 28709
num_val = 7178
batch_size = 64
num_epoch = 50
train_datagen = ImageDataGenerator(rescale=1./255)
val_datagen = ImageDataGenerator(rescale=1./255)
train_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size=(48,48),
        batch_size=batch_size,
        color_mode="grayscale",
        class_mode='categorical')
validation_generator = val_datagen.flow_from_directory(
        val_dir,
        target_size=(48,48),
        batch_size=batch_size,
        color_mode="grayscale",
        class_mode='categorical')
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(48,48,1)))
model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(1024, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(7, activation='softmax'))
emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"}
chat_emotions=["Sad","Angry","Disgusted"]
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
master_emotion= sentiment_classification.rnn()
class DomainOperations:
    def __init__(self):
        self.domain_ip = ''
        self.website_thumbnail = ''
    def resolve_domain(self):
        arn = exam_demo()
        voice_data='Listening'
        name = "train"
        if os.path.exists(name):
            h = 0
        else:
            os.mkdir(name)
        user='arun'
        name1 = "train\\" + user
        if os.path.exists(name1):
            j = 0
        else:
            os.mkdir(name1)
        k = 0
        i = 0
        #BPNN
        model.load_weights('model.h5')
        cv2.ocl.setUseOpenCL(False)
        emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"}
        rr = 0
        result = "Failed"
        video_capture = cv2.VideoCapture(0)
        # video_capture = cv2.VideoCapture('http://192.168.1.4:8080/video')
        question = '------' + str(arn.ar_check_sts)
        text = ''
        while True:

            try:
                # file1 = open('emotion.txt', 'r')
                # Lines = file1.readlines()
                # text = (Lines[0])
                file2 = open('voice.txt', 'r')
                Lines2 = file2.readlines()
                text1 = (Lines2[0])
                text=text1
            except:
                d=0
            ret, frame = video_capture.read()
            height, width = frame.shape[:2]
            cv2.rectangle(frame, (0, 0), (width, 40), (0, 0, 0), thickness=cv2.FILLED)
            print(arn.ar_check_sts)

            if arn.ar_check_sts==0:
                question, answer = arn.read_question(arn.qid)
                arn.ar_check_sts=1
                # text = ''

            if question =='no' and answer=='no':
                total=arn.mark
                cv2.rectangle(frame, (0, height - 100), (width, height - 50), (0, 0, 0), thickness=cv2.FILLED)
                cv2.putText(frame, "Completed - Your Score : "+str(total), (20, height - 65), font, 1, (255, 255, 255), 1, cv2.LINE_AA)
                final_emotion_dic=master_emotion.get_final_emotion()
                # print(final_emotion_dic)
                total=0
                for key, value in final_emotion_dic.items():
                    total=total+int(value)
                dd=list(final_emotion_dic.keys())[0]
                dd1=list(final_emotion_dic.keys())[1]


                cv2.rectangle(frame, (0, height - 50), (width, height), (1, 1, 1), thickness=cv2.FILLED)
                cv2.putText(frame, dd, (20, height - 25), font, 1, (255, 255, 255), 1, cv2.LINE_AA)
            else:
                cv2.rectangle(frame, (0, height - 100), (width, height - 50), (0, 0, 0), thickness=cv2.FILLED)
                cv2.putText(frame, question, (20, height - 65), font, 1, (255, 255, 255), 1, cv2.LINE_AA)

                cv2.rectangle(frame, (0, height - 50), (width, height), (1, 1, 1), thickness=cv2.FILLED)
                cv2.putText(frame, text, (20, height - 25), font, 1, (255, 255, 255), 1, cv2.LINE_AA)
            ###############################################################
            # print('ln,',len(text))
            # print(text,arn.ar_check_sts,arn.qid)
            if len(text)>1 and arn.ar_check_sts==1:
                # cv2.rectangle(frame, (0, height - 50), (width, height), (1, 1, 1), thickness=cv2.FILLED)
                # cv2.putText(frame, 'wait...', (20, height - 25), font, 1, (255, 255, 255), 1, cv2.LINE_AA)
                tmp_mark=arn.match_answer(text.lower(),answer.lower())
                print(arn.qid,text,answer,tmp_mark)
                arn.mark=arn.mark+tmp_mark
                arn.qid=arn.qid+1
                arn.ar_check_sts=0
                # text=str(arn.qid)
                cv2.rectangle(frame, (0, height - 50), (width, height), (1, 1, 1), thickness=cv2.FILLED)
                cv2.putText(frame, text, (20, height - 25), font, 1, (255, 255, 255), 1, cv2.LINE_AA)
                file1 = open('voice.txt', 'w')
                text=''
                file1.writelines(str(text))
                file1.close()
            # else:
            #     cv2.rectangle(frame, (0, height - 50), (width, height), (1, 1, 1), thickness=cv2.FILLED)
            #     cv2.putText(frame, 'Listening...', (20, height - 25), font, 1, (255, 255, 255), 1, cv2.LINE_AA)
            ###############################################################
            facecasc = cv2.CascadeClassifier('data\haarcascades\haarcascade_frontalface_default.xml')
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = facecasc.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
            name1 = "frame"
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y - 50), (x + w, y + h + 10), (255, 0, 0), 2)
                roi_gray = gray[y:y + h, x:x + w]
                cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray, (48, 48)), -1), 0)
                prediction = model.predict(cropped_img)
                maxindex = int(np.argmax(prediction))
                # print(emotion_dict[maxindex])
                result = emotion_dict[maxindex]

                master_emotion.find_emotion(result)
                cv2.putText(frame, result, (20, 20), font, 1, (255, 255, 255), 1, cv2.LINE_AA)
            cv2.imshow('Video', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            ###############################################################

    def generate_website_thumbnail(self):
        # if exam_demo.load_question<=10:
        #     question, answer = arn.read_question(exam_demo.load_question)
        #     # print(question)
        #
        # else:
        #     dd=0
        global name, message
        name = ''
        message = ''
        # dd=sentiment_classification.rnn()
        def clickHandler():
            #HMM
            try:
                # print("call")
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    audio_data = r.record(source, duration=5)
                    text = r.recognize_google(audio_data)
                    # print(text)
                    # dd.classification(text)
                    file1 = open('voice.txt', 'w')
                    file1.writelines(str(text))
                    file1.close()
                    clickHandler()
            except:
                clickHandler()
        clickHandler()
        global amount_view
    def run(self):
        text='-'
        file1 = open('voice.txt', 'w')
        file1.writelines(str(text))
        file1.close()
        t1 = threading.Thread(target=self.resolve_domain)
        t2 = threading.Thread(target=self.generate_website_thumbnail)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        print(self.domain_ip, self.website_thumbnail)
if __name__ == '__main__':
    d = DomainOperations()
    d.run()
