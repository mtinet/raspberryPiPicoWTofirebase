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
response = urequests.get(url+".json")
print(response.content)
response.close()

while True:
    # 객체 교체하기, 특정 주소의 데이터가 변경됨
    myobj = {'humi': random.randrange(1,100)}
    r = urequests.patch(url+"smartFarm.json", json = myobj)
    r
    r.close()
    time.sleep(1)
