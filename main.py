# 디버그 모드 설정
debug = True

"""
메인테이너 : 방주원
작성일 : 2023-04-19
프로그램 설명 : 물품관리 프로그램
"""

# QR코드 인식 라이브러리
import cv2
import time
import pyzbar.pyzbar as pyzbar
from playsound import playsound
from datetime import datetime

# 데이터베이스 라이브러리
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json

# 자체 제작 라이브러리
import opencv_toolkit as otk
import firebase_realtimedb as frdb
device_id = []

cap = otk.cap
last_time = otk.last_time
time_per_frame_video = otk.time_per_frame_video
draw_text = otk.draw_text

대여목록 = []


while True:
    success, frame = cap.read()

    # fsp 계산
    time_per_frame = time.perf_counter() - last_time
    time_sleep_frame = max(0, time_per_frame_video - time_per_frame)
    time.sleep(time_sleep_frame)

    # 실제 fps 계산
    real_fps = 1/(time.perf_counter()-last_time)
    last_time = time.perf_counter()
    x = 30
    y = 50
    text = '%.2f fps' % real_fps

    # 이미지의 (x, y)에 텍스트 출력
    draw_text(frame, text, x, y)

    # QR코드 인식
    for code in pyzbar.decode(frame):
        try:
            my_code = code.data.decode('utf-8')
        except:
            try:
                my_code = code.data.decode('cp949')
            except:
                my_code = "error"

        playsound("./qrbarcode_beep.mp3")
        print("인식 성공 :", my_code)
        
        cv2.imwrite(f'./QR_IMG/{datetime.now().strftime("%y-%m-%d-%H-%M-%S")}.png', frame)
        f2 = open("qrLogs.txt", "a", encoding="utf8")
        f2.write(f'[{datetime.now().strftime("%Y년 %m월 %d일 %H시 %M분 %S초")}] 인식된 값 : {my_code}\n')
        f2.close()

        if my_code.startswith('C'):
            print("학생증, 대여 품목 = ", end="")
            print(대여목록)
        else:
            device_data = frdb.get_device()
            for n in device_data:
                if n == my_code:
                    print("마즘", n, my_code)
                    대여목록.append(n)

            time.sleep(1)
            print(대여목록)
    if cv2.waitKey(1)&0xFF == 27:
        break
    if debug:
        cv2.imshow('QRcode Barcode Scan', frame)
    cv2.waitKey(1)

