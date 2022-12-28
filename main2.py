# 피코 W에 micropython-firebase-auth 라이브러리를 설치하고 테스트 한 코드
# 토큰이 만들어지는 것까지 구현하였으나, 50번째 줄 처럼 토큰 사용을 할 때 인증이 안된 토큰이라는 결과를 내뿜음

import time
import network
from firebase_auth import FirebaseAuth
import urequests
import random

# 와이파이 연결
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    wlan.connect("U+Net454C", "DDAE014478")
    print("Waiting for Wi-Fi connection", end="...")
    while not wlan.isconnected():
        print(".", end="")
        time.sleep(1)
else:
    print(wlan.ifconfig())
    print("WiFi is Connected")

auth = FirebaseAuth("AIzaSyA4JNrHtS9pc6QaW8dtwATWhUhs0Ni8OBI")
auth.sign_in("mtinet7979@gmail.com", "wnstp0517")
print("Hello, " + str(auth.user))

creds = auth.session.credentials
print(creds)
print()
print("refresh_token:" + creds['refresh_token'])
print()
print("access_token:" + creds['access_token'])
print()
print("token_expiry:" + str(creds['token_expiry']))


# RTDB주소
url = "https://smartfarm-f867f-default-rtdb.firebaseio.com/"

# DB 내역 가져오기
response = urequests.get(url+".json").json()
# byte형태의 데이터를 json으로 변경했기 때문에 메모리를 닫아주는 일을 하지 않아도 됨
print(response)
# print(response['smartFarm'])
# print(response['smartFarm']['led'])

# 객체 교체하기, patch는 특정 주소의 데이터가 변경됨
myobj = {'humi': random.randrange(0,100), 'temp': random.randrange(0, 50)}
urequests.patch(url+".json", json = myobj).json()
urequests.patch(str(url+".json" + "?access_token=" + creds['access_token']), json = myobj).json()
