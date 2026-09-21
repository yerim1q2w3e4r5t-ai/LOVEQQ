# Nongshim DART Agent — GitHub Ready

농심(고유번호 `00108241`)의 OpenDART 정기보고서 재무정보를 수집하고,
재무비율을 계산하여 GitHub Pages 대시보드로 제공하는 Agent 템플릿입니다.

## 데이터 흐름

OpenDART API → Agent → raw JSON → 정규화 CSV → 재무비율 → Dashboard JSON → GitHub Pages

OpenDART의 `fnlttSinglAcntAll.json` 전체 재무제표 API를 사용합니다.
- `corp_code`: 00108241
- `reprt_code`: 11011 (사업보고서)
- `fs_div`: CFS (연결재무제표)
- 대상연도: 2021~2025

## GitHub 설정

Repository Settings → Secrets and variables → Actions

### Secret
`DART_API_KEY` = 본인의 OpenDART API 인증키

### Variable
`NONGSHIM_CORP_CODE` = `00108241`

API Key는 절대 코드, HTML, JavaScript, README에 저장하지 않습니다.

## 실행

```bash
pip install -r requirements.txt
python -m agent.main
```

GitHub에서는 Actions의 `Update DART data and deploy Pages`를 수동 실행할 수 있습니다.

## 생성 파일

- `data/raw/dart/YYYY_CFS.json`
- `data/processed/nongshim_financials.csv`
- `data/processed/nongshim_dashboard.json`

## 주의

계정명은 공시 데이터의 `account_nm`에 따라 달라질 수 있으므로,
실제 API 응답을 확인하면서 normalize 계정 매핑을 보완해야 합니다.
