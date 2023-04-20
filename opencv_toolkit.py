import cv2
import time

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

# 웹캠 설정
cap = cv2.VideoCapture(0)
cap.set(3, 1920)
cap.set(4, 1080)
cap.set(cv2.CAP_PROP_FPS,30)

# def setup():
    

# 웹캠 fps
fps = cap.get(cv2.CAP_PROP_FPS)
print('fps', fps)

# 웹캠 fps가 0이면 30으로 설정
if fps == 0.0:
    fps = 30.0

# 웹캠 fps에 따른 sleep time 계산
time_per_frame_video = 1/fps
last_time = time.perf_counter()
