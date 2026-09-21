import json
import pandas as pd
from .config import RAW_DIR, PROCESSED_DIR, YEARS
ACCOUNT_MAP = {
    "sales": ["매출액", "수익(매출액)", "영업수익"],
    "operating_profit": ["영업이익", "영업이익(손실)"],
    "net_income": ["당기순이익", "당기순이익(손실)"],
    "assets": ["자산총계"],
    "liabilities": ["부채총계"],
    "equity": ["자본총계"],
    "cfo": ["영업활동 현금흐름", "영업활동으로 인한 현금흐름"],
    "capex": ["유형자산의 취득", "유형자산 취득"],
}
def num(v):
    try:
        return float(str(v).replace(",", "").strip())
    except (ValueError, TypeError):
        return None
def find(rows, names):
    for row in rows:
        if row.get("account_nm") in names:
            return num(row.get("thstrm_amount"))
    return None
def normalize():
    records=[]
    for year in YEARS:
        data=json.loads((RAW_DIR/f"{year}_CFS.json").read_text(encoding="utf-8"))
        rows=data.get("list", [])
        rec={"year":year}
        for key,names in ACCOUNT_MAP.items():
            rec[key]=find(rows,names)
        records.append(rec)
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    df=pd.DataFrame(records)
    df.to_csv(PROCESSED_DIR/"nongshim_financials.csv", index=False, encoding="utf-8-sig")
    return df
