import json
from .config import RAW_DIR, NONGSHIM_CORP_CODE, YEARS, REPORT_CODE, FS_DIV
from .dart_client import DartClient
def collect():
    if not NONGSHIM_CORP_CODE:
        raise RuntimeError("NONGSHIM_CORP_CODE가 설정되지 않았습니다.")
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    client = DartClient()
    for year in YEARS:
        data = client.get("fnlttSinglAcntAll.json", {
            "corp_code": NONGSHIM_CORP_CODE,
            "bsns_year": str(year),
            "reprt_code": REPORT_CODE,
            "fs_div": FS_DIV,
        })
        (RAW_DIR / f"{year}_CFS.json").write_text(
            json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
        )
if __name__ == "__main__":
    collect()
