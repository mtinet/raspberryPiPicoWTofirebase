from machine import Pin, I2C
import network
import time
import urequests
import random

# 와이파이 정보 
SSID = 'U+Net03CC'
password = 'J6FDFE#490'

# 와이파이 연결하기
def wifiConnect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        # 와이파이 연결하기
        wlan.connect(SSID, password)  # 5, 6번 줄에 입력한 SSID와 password가 입력됨
        print("Waiting for Wi-Fi connection", end="...")
        print()
        while not wlan.isconnected():
            print(".", end="")
            time.sleep(1)
    else:
        print(wlan.ifconfig())
        print("WiFi is Connected")
        print()

# 와이파이 함수 실행
wifiConnect()

controlPin = Pin(22, Pin.OUT)

url = "https://iot-project-3c0b1-default-rtdb.firebaseio.com/"

# DB 내역 가져오기
response = urequests.get(url+".json").json()

# byte형태의 데이터를 json으로 변경했기 때문에 메모리를 닫아주는 일을 하지 않아도 됨 
print(response)

# led(22번핀)에 LOW값을 인가함
controlPin.value(0)

# 객체 초기화, 'led'를 '0'으로 설정함.
myobj = {'controlPin': 0}
urequests.patch(url+".json", json = myobj)


while True:
    # 현재 DB의 정보를 가져옴
    response = urequests.get(url+".json").json()
    # 현재 DB의 led 키 값의 상태에 따라 led 27번을 제어
    if (response['controlPin'] == 0) :
        controlPin.value(0)
        # print("Control Pin is Off.")
    else :
        controlPin.value(1)
        # print("Control Pin is On.")
