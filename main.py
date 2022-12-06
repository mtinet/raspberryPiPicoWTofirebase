from machine import Pin, I2C
import network
import time
import urequests
import random

from machine import Pin
led = Pin(27, Pin.OUT)

# Connect Internet by WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("U+Net454C", "DDAE014478")
print(wlan.isconnected())
print(wlan.ifconfig())

url = "https://smartfarm-f867f-default-rtdb.firebaseio.com/"

# DB 내역 가져오기
response = urequests.get(url+".json").json()
# byte형태의 데이터를 json으로 변경했기 때문에 메모리를 닫아주는 일을 하지 않아도 됨 
# print(response)
# print(response['smartFarm'])
# print(response['smartFarm']['led'])

while True:
    response = urequests.get(url+".json").json()
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

