# e-safe clicker 활용법
[기능]
매우 단순하다. 1분마다 다음 버튼을 자동으로 누르는 시도를 한다.
멍청하게 퀴즈에 대한 대응은 하지 못한다.(만들기 귀찮아~) 

[설치]
pip install pyautogui

[소스코드 수정]
1. 우선 다음 버튼과 실패시 눌러야할 OK 버튼의 위치를 알기 위해서 Found_pos를 False로 설정한다.
2. 실행하면 현재 마우스 위치의 좌표가 찍힌다. 
3. 다음 버튼의 위치를 기록한다. (x, y 좌표)
4. 다음 버튼을 눌러보며 "정해진 학습시간을 학습해야 한다"고 메세지가 뜨고 OK 버튼이 뜬다.
5. OK 버튼의 위치를 기록한다.
6. Found_pos를 True로 바꾸고 실행.

[실행 방법]
python e-safe-clicker.py
