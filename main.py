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

url = "자신의 파이어베이스 리얼타임 데이터베이스 주소를 넣을 것"

# DB 내역 가져오기
response = urequests.get(url+".json").json()
# byte형태의 데이터를 json으로 변경했기 때문에 메모리를 닫아주는 일을 하지 않아도 됨 
# print(response)
# print(response['smartFarm'])
# print(response['smartFarm']['led'])

while True:
    # 현재 DB의 정보를 가져옴
    response = urequests.get(url+".json").json()
    # 현재 DB의 led 키 값의 상태에 따라 led 27번을 제어
    if (response['smartFarm']['led'] == 0) :
        led.value(0)
    else :
        led.value(1)
        
    # 객체 교체하기, 특정 주소의 데이터가 변경됨
    myobj = {'humi': random.randrange(0,100), 'temp': random.randrange(0, 50)}
    urequests.patch(url+"smartFarm.json", json = myobj).json()
