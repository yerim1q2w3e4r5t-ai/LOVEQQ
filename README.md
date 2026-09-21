# Nongshim DART Agent

농심 OpenDART API 데이터를 수집하고 재무비율을 계산한 뒤 GitHub Pages 대시보드로 제공하기 위한 개발 템플릿입니다.

## 실행
1. OpenDART API 키 발급
2. `.env.example`을 `.env`로 복사하고 `DART_API_KEY` 설정
3. `NONGSHIM_CORP_CODE` 설정
4. `pip install -r requirements.txt`
5. `python -m agent.main`

GitHub Actions에서는 Repository Secret `DART_API_KEY`와 Repository Variable `NONGSHIM_CORP_CODE`를 설정합니다.

API 키는 절대로 HTML/JavaScript 또는 Git 저장소에 넣지 마세요.
