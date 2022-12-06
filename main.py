from machine import Pin, I2C
import network
import time
import urequests
import random

# 제어할 핀 번호 설정
from machine import Pin
led = Pin(27, Pin.OUT)

# 와이파이 연결하기
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets.SSID, secrets.PASSWORD)
print(wlan.isconnected())
print(wlan.ifconfig())

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
    request = urequests.patch(url+"smartFarm.json", json = myobj)
    request
    request.close()
    time.sleep(1)

