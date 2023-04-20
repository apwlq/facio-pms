# 디버그 모드(웹캠 켜짐)
debug = True
"""
메인테이너 : 방주원
작성일 : 2023-04-19
프로그램 설명 : 물품관리 프로그램
"""

import cv2
import time
import pyzbar.pyzbar as pyzbar
from playsound import playsound

used_codes = []
data_list = []

# 웹캠 텍스트 출력 함수
def draw_text(img, text, x, y):
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_thickness = 2
    text_color=(255, 0, 0)
    text_color_bg=(0, 0, 0)

    text_size, _ = cv2.getTextSize(text, font, font_scale, font_thickness)
    text_w, text_h = text_size
    offset = 5

    cv2.rectangle(img, (x - offset, y - offset), (x + text_w + offset, y + text_h + offset), text_color_bg, -1)
    cv2.putText(img, text, (x, y + text_h + font_scale - 1), font, font_scale, text_color, font_thickness)

# QR 데이터 열기
try:
    f = open("qrbarcode_data.txt", "r", encoding="utf8")
    data_list = f.readlines()
except FileNotFoundError:
    pass
else:
    f.close()

# 웹캠 설정
cap = cv2.VideoCapture(0)
cap.set(3, 1920)
cap.set(4, 1080)
cap.set(cv2.CAP_PROP_FPS,30)

# 웹캠 fps
fps = cap.get(cv2.CAP_PROP_FPS)
print('fps', fps)

# 웹캠 fps가 0이면 30으로 설정
if fps == 0.0:
    fps = 30.0

# 웹캠 fps에 따른 sleep time 계산
time_per_frame_video = 1/fps
last_time = time.perf_counter()

# 이미 인식된 코드 리스트에 추가
for i in data_list:
    used_codes.append(i.rstrip('\n'))

# 웹캠 실행
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
        cv2.imwrite('qrbarcode_image.png', frame)
        my_code = code.data.decode('utf-8')
        if my_code not in used_codes:
            print("인식 성공 : ", my_code)
            playsound("./qrbarcode_beep.mp3")
            used_codes.append(my_code)

            f2 = open("qrbarcode_data.txt", "a", encoding="utf8")
            f2.write(my_code+'\n')
            f2.close()
        elif my_code in used_codes:
            print("이미 인식된 코드 입니다.!!!")
            playsound("./qrbarcode_beep.mp3")
        else:
            pass
    if cv2.waitKey(1)&0xFF == 27:
        break
    if debug:
        cv2.imshow('QRcode Barcode Scan', frame)
    cv2.waitKey(1)