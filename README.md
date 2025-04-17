# Satronix - Satellite Signal Decoder and Viewer <br>프로젝트 1일차 소프트웨어 시스템 구성 계획 🚀🛰️


Satronix는 저비용 장비를 이용하여 NOAA 위성의 실시간 신호를 수신하고, 디코딩된 위성 이미지를 웹으로 시각화하는 오픈소스 프로젝트입니다. 이 프로젝트는 SDR(Software Defined Radio)과 Raspberry Pi, Ubuntu 기반 환경에서 구현되며, 수신된 이미지를 서버를 통해 실시간으로 전송 및 열람할 수 있도록 구성됩니다.

---

## 📌 프로젝트 개요
- **📛 프로젝트명**: Satronix
- **🎯 목표**: NOAA 위성의 이미지 실시간 수신 및 웹 시각화
- **🖥️ 기반 OS**: Ubuntu (라즈베리파이 혹은 x86 환경)
- **🛠️ 사용 기술**:
  - 하드웨어: RTL-SDR, Raspberry Pi
  - 수신/디코딩 툴: `rtl_fm`, `sox`, `wxtoimg`
  - 서버: Flask + Apache (또는 간단한 Python HTTP 서버)
  - 프론트엔드: HTML / CSS / JavaScript

---

## 🔧 시스템 구성도
```
[ NOAA 또는 천리안위성 2A호 위성 ]
      ↓ (위성주파수)
[ RTL-SDR + 라즈베리파이 ]
      ↓ (WAV 파일 생성)
[wxtoimg 로 디코딩 → 이미지 생성]
      ↓
[서버 전송 (Flask REST API 등)]
      ↓
[웹페이지에 실시간 표시]
```

---

## 📥 사용 도구 설치 (Ubuntu 기준)
```bash
sudo apt update
sudo apt install rtl-sdr sox wxtoimg python3-flask -y
```

---

## 🎙️ NOAA 위성 수신 및 WAV 변환 예시
```bash
rtl_fm -f 137.62M -s 208k -g 40 | \
sox -t raw -r 208k -es -b 16 -c 1 -V1 - sat_output.wav
```

## 🖼️ WAV 파일 디코딩
```bash
wxtoimg -m -e HVCT sat_output.wav output_image.png
```

---

## 🌐 Flask 서버 예시 코드
```python
from flask import Flask, send_from_directory
app = Flask(__name__)

@app.route("/latest")
def latest_image():
    return send_from_directory("images", "output_image.png")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

## 🧩 웹페이지에 이미지 띄우기 (index.html)
```html
<img src="http://서버주소:5000/latest" alt="실시간 위성 이미지" />
```

---

## 🎧 WAV 포맷 관련
Ubuntu는 기본적으로 WAV 포맷을 완벽히 지원하며, `sox`, `aplay` 등의 도구를 통해 확인하고 재생할 수 있습니다.

```bash
aplay sat_output.wav
soxi sat_output.wav
```

`rtl_fm` → `sox` 파이프라인으로 WAV를 생성할 때는 **16-bit signed little-endian** 형식으로 만드는 것이 중요합니다.

---

## 🔄 향후 추가 예정
- ⏱️ 자동화된 수신 스케줄러 (cron or systemd timer)
- 🌐 웹소켓을 통한 실시간 이미지 업데이트
- ☁️ 자동 이미지 업로드 및 서버 관리
- 🧪 Ai 학습을 통한 이미지 분석

---

## 📜 저작권 & 기여
본 프로젝트는 오픈소스로 자유롭게 복제 및 수정이 가능합니다.

> 문의 및 기여는 GitHub를 통해 환영합니다!
