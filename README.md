# moviepy
moviepy 라이브러리를 이용한 음성 합성

1. webm + mp3
webm 비디오 파일과 mp3 음성 파일의 합성.
mp3 파일이 들어갈 시점(초)을 입력으로 받고 합성된 mp4 파일을 결과로 출력.


2. webm2mp4
webm 비디오 파일을 mp4 비디오 파일로 변환.
변환할 webm 파일 경로와 변환 후 저장할 mp4 파일 경로를 각각 input과 output으로 받음.
추가로, 입력 파일 경로와 출력 파일 경로, 시작 시간과 종료 시간을 로그로 남김.

3. json_check_mp4
mp4 영상(20분)에 대해 10초 분량마다 시작시간, 종료시간, 예측 클래스, 정답 클래스, 통과율 등이 들어있는 json 파일을 읽음.
여러 feature 중 통과율이 0.7 이상인 구간 영상만 추출하여 이를 이어붙인 mp4 파일 저장.
   moviepy와 opencv 두 가지 라이브러리를 사용.
   * moviepy - 소요 시간 : 460초
   * opencv - 소요 시간 : 141초

4. 
