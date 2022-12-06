# raspberryPiPicoWTofirebase

## Raspberry Pi Pico W to firebase 
### 1. firebase.google.com에 들어가서 로그인 하고 우측 상단의 '콘솔로 이동' 버튼을 누름. '프로젝트 추가'버튼을 눌러 자신의 프로젝트를 만듬  
<img width="863" alt="firebase" src="https://user-images.githubusercontent.com/13882302/205473085-8a1656dc-c96a-462f-a681-85ae4f668cc4.png">

### 2. 프로젝트가 생성되면 realtime database를 클릭해서 생성함  
<img width="683" alt="realtime check" src="https://user-images.githubusercontent.com/13882302/205473088-ba87fa56-148a-4e04-9e81-959a8813a524.png">

### 3. '데이터' 탭에서 보여지는 주소가 여러분의 리얼타임 데이터베이스를 사용하기 위한 주소임  
<img width="749" alt="1" src="https://user-images.githubusercontent.com/13882302/205473090-29d787b6-e11f-41b3-841c-88a1e18a6962.png">  

### 4. '규칙' 탭에 가서 규칙을 아무나 쓰고 지울 수 있게 세팅을 해야 DB의 json파일에 GET, POST, PUT, PATCH, DELETE 할 수 있음, 따라서 주소에 대한 보안 유의 철저 필요  
<img width="779" alt="2" src="https://user-images.githubusercontent.com/13882302/205473092-d51ab39e-aee2-453f-ba26-7c354953f1af.png">

### 5. 파이썬 코드(micropython on raspberry pi pico w)
### 리얼타임 데이터베이스의 주소 위치
<img width="877" alt="firebase realtime db" src="https://user-images.githubusercontent.com/13882302/205472925-88301bd7-5b7a-427b-bb56-d9d06c549229.png">

#### usage.py
```python 
from machine import Pin, I2C
import network
import utime
# 이 파일과 같은 폴더에 secrets.py파일을 만들고, SSID, Password 파일을 넣어놓을 것
import secrets
import urequests

# Connect Internet by WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets.SSID, secrets.PASSWORD)
print(wlan.isconnected())
print(wlan.ifconfig())

url = "자신의 파이어베이스 리얼타임 데이터베이스 주소를 넣을 것"

# get: 리스트 가져오기
# get+데이터 주소: 단일 데이터 가져오기
# post: 객체 등록하기
# put: 업데이트(객체 교체하기)
# patch: 업데이트(일부 값만 업데이트)
# delete: 객체 삭제

# 전체 json파일 가져오기
response = urequests.get(url+".json")
print(response.content)

# json파일 중 일부 가져오기, 아래의 .json 앞쪽은 이전에 자동으로 올린 자료의 ID라고 보면됨. 따라서 자신의 리얼타임 DB에 없을 수 있음
response = urequests.get(url+"-NIPukhnX6qkPVb-P6Eh.json")
print(response.content)

# 데이터 추가하기, 자동으로 주소가 붙고, 그 아래에 데이터를 추가함
myobj = {'somekey': 'somevalue'}
urequests.post(url+".json", json = myobj)

# 객체 교체하기, 특정 주소의 데이터가 변경됨
myobj = {'ahha': 'jaja'}
urequests.put(url+"test.json", json = myobj)

# 객체 교체하기, 특정 주소의 데이터가 변경됨
myobj = {'hhhggfggff': 'ssssssss'}
urequests.patch(url+"test.json", json = myobj)

# 객체 삭제
urequests.delete(url+"test.json")

response = urequests.get(url+".json")
print(response.content)

```

## boot.py, main.py, secrets.py
- Blink 수준의 파일은 main.py만으로도 전원을 연결하면 자동으로 실행됨
- 와이파이를 사용하는 경우 boot.py 파일을 따로 만들어서 사용해야 자동 실행이 됨
- boot.py 파일 안에는 main파일을 임포트 하는 코드가 필요함
- secrets.py 파일에는 와이파이 SSID, Password가 들어 있음

#### boot.py
```python 
from machine import Pin
from utime import sleep

# 전원이 들어온지에 대한 모니터링용 코드
led = Pin(27, Pin.OUT)

led.on()
sleep(0.2)
led.off()
sleep(0.2)
led.on()
sleep(0.2)
led.off()
sleep(0.2)
led.on()
sleep(0.2)
led.off()
sleep(0.2)

# main.py 파일 임포트
import main
```

#### main.py
```python
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
    urequests.patch(url+"smartFarm.json", json = myobj).json()
```

#### secrets.py
```python
SSID = "U+Net454C"
PASSWORD = "DDAE014478"
```

---
## firebase to Node-RED
참고. [https://nodered.org/docs/getting-started/windows#running-on-windows](https://nodered.org/docs/getting-started/windows#running-on-windows)

### 1. Node 설치
홈페이지에서 자신의 OS에 맞는 Node LTS버전을 다운로드 받아 설치(https://nodejs.org/en/)

### 2. Node, npm 버전 확인
cmd를 열고 아래 명령어를 입력
```
node --version && npm --version
```

### 3. Node-RED 설치
cmd를 열고 아래 명령어를 입력
```
npm install -g --unsafe-perm node-red
```

### 4. Node-RED 실행
cmd를 열고 아래 명령어를 입력
```
node-red
```

### 5. Node-RED에 접속
브라우저를 열고 아래 주소로 접속한다.
http://127.0.0.1:1880/
