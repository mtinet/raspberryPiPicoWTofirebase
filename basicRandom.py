from machine import Pin, I2C
import network
import time
import urequests
import random

# Connect Internet by WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("U+Net454C", "DDAE014478")
print(wlan.isconnected())
print(wlan.ifconfig())

url = "https://smartfarm-f867f-default-rtdb.firebaseio.com/"

# DB 내역 가져오기
response = urequests.get(url+".json").json()
# print(response)
# print(response['smartFarm'])
# print(response['smartFarm']['led'])

while True:
    response = urequests.get(url+".json")
    response.close()
    # 객체 교체하기, 특정 주소의 데이터가 변경됨
    myobj = {'humi': random.randrange(0,100), 'temp': random.randrange(0, 50)}
    request = urequests.patch(url+"smartFarm.json", json = myobj)
    request
    request.close()
    time.sleep(1)
