from machine import Pin, I2C
import network
import time
import urequests

# Connect Internet by WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("와이파이 이름", "와이파이 비번")
print(wlan.isconnected())
print(wlan.ifconfig())

url = "파이어베이스 리얼타임 데이터베이스 주소"

# DB 내역 가져오기
response = urequests.get(url+".json")
print(response.content)

# 객체 교체하기, 특정 주소의 데이터가 변경됨
myobj = {'humi': '70'}
urequests.patch(url+"smartFarm.json", json = myobj)


