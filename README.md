# 🕸️ 크롤링 모듈 - quantly-platform-ai

---

## 1. 프로젝트 소개

AI 기반 금융 데이터 분석 플랫폼 **quantly-platform-ai**의 초기 단계 모듈입니다.  
현재는 주식/ETF 등의 자산 데이터를 수집하기 위한 **크롤링 기능**이 우선 구현되어 있습니다.

---

## 2. 핵심 기능 (예정 포함) ✅

- S&P 500 종목 크롤링 (시가총액, 구성 비중 등)
- 자연어 질의 연계용 원천 데이터 확보
- 주식/ETF 자산군의 시계열 데이터 수집 (예정)
- 전처리 및 정규화 (예정)
- 크롤링 결과 저장 (CSV, DB 등)
- 수집 주기 자동화 (예정: 스케줄링 또는 크론 연동)
- 크롤링 예외/오류 핸들링 및 로깅 (예정)

---

## 3. 사용 기술 스택 🛠️

🧩 크롤링 스크립트 (Python 기반)

| 항목         | 버전 / 도구         |
|--------------|----------------------|
| Python       | 3.10 이상            |
| requests     | 웹 요청 처리         |
| BeautifulSoup| HTML 파싱            |
| pandas       | 데이터 프레임 처리   |

---

## 4. 실행 방법 🚀

- 실행 환경: Python 기반 CLI 실행
- 포트 없음 (스크립트 단독 실행)

### 실행 예시

```bash
# 가상환경 설정 (선택)
python -m venv venv
source venv/bin/activate      # macOS/Linux
.\venv\Scripts\activate       # Windows

# 의존성 설치
pip install -r requirements.txt

# 크롤링 실행
python crawling/sp500_scraper.py
5. 실행 화면 (예정)
추후: S&P 500 종목 정보 표, 시가총액 순 정렬된 출력 예시 등 포함 예정

# 6. 프로젝트 구조 📁
bash
quantly-platform-ai/
├── crawling/
│   └── crawling_sp500.py     # 크롤링 메인 모듈
│   └── crawling_nasdaq.py     # 크롤링 메인 모듈
│   └── column_utils.py     # 크롤링 메인 모듈
├── requirements.txt         # 의존성 파일
└── README.md

# 7. 라이선스
MIT License

# 8. 진행 상태 및 TODO
기능 항목	상태
S&P 500 종목 크롤링	✅ 완료
크롤링 결과 CSV 저장	✅ 완료
주기적 수집 자동화	⏳ 예정
오류 예외 처리 및 로깅	⏳ 예정
시계열 수집 (가격/배당 등)	⏳ 예정
분석/시각화 연동	⏳ 예정

# 9. 참고한 오픈소스


10. 진행 현황 🧪
Progress: 🟩⬜⬜⬜⬜⬜⬜⬜⬜ 10%

기능	상태
S&P500 종목 크롤링	✅ 완료
자연어 연동용 분석 기반 확보	✅ 완료
시계열 자산 크롤링	⏳ 예정
자동화 및 에러 핸들링	⏳ 예정
분석 서버 연동	⏳ 예정
시각화 및 대시보드 연동	⏳ 예정

