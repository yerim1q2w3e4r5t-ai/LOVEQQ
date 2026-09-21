import os
from pathlib import Path
from dotenv import load_dotenv
ROOT = Path(__file__).resolve().parents[1]
load_dotenv(ROOT / ".env")
DART_API_KEY = os.getenv("DART_API_KEY")
NONGSHIM_CORP_CODE = os.getenv("NONGSHIM_CORP_CODE")
DART_BASE_URL = "https://opendart.fss.or.kr/api"
YEARS = [2021, 2022, 2023, 2024, 2025]
REPORT_CODE = "11011"
FS_DIV = "CFS"
RAW_DIR = ROOT / "data" / "raw" / "dart"
PROCESSED_DIR = ROOT / "data" / "processed"
