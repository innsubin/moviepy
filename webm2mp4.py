import cv2
import time
import multiprocessing as mp
import argparse
import logging

obj_parser = argparse.ArgumentParser()
obj_parser.add_argument('--webm_input_path') 
obj_parser.add_argument('--mp4_output_path') 
args = obj_parser.parse_args()

input = args.webm_input_path
output = args.mp4_output_path

# 시작 시간 기록
start_time = time.time()

# 원본 동영상 파일 열기
cap = cv2.VideoCapture(input)

# 동영상 크기 및 프레임 정보 가져오기
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = int(cap.get(5))

# MP4 코덱 설정 fourcc
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

# VideoWriter 객체 생성
out = cv2.VideoWriter(output, fourcc, fps, (frame_width, frame_height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # 동영상 프레임을 MP4 파일에 쓰기
    out.write(frame)

# 객체 및 창 닫기
cap.release()
out.release()

# 종료 시간 기록
end_time = time.time()

# print(f'Input path: {input}')
# print(f'Output path: {output}')
# print(f"Start time: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))}")
# print(f"End time: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))}")
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info(f"Input file: {input}")
logging.info(f"Output file: {output}")
logging.info(f"Start time: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))}")
logging.info(f"End time: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))}")