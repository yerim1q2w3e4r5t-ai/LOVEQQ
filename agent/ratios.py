import json
from .config import PROCESSED_DIR
def calculate(df):
    df=df.sort_values("year").copy()
    df["sales_growth_pct"]=df["sales"].pct_change()*100
    df["operating_margin_pct"]=df["operating_profit"]/df["sales"]*100
    df["net_margin_pct"]=df["net_income"]/df["sales"]*100
    df["debt_ratio_pct"]=df["liabilities"]/df["equity"]*100
    df["equity_ratio_pct"]=df["equity"]/df["assets"]*100
    df["cfo_to_net_income_pct"]=df["cfo"]/df["net_income"]*100
    df["avg_assets"]=(df["assets"]+df["assets"].shift(1))/2
    df["avg_equity"]=(df["equity"]+df["equity"].shift(1))/2
    df["roa_pct"]=df["net_income"]/df["avg_assets"]*100
    df["roe_pct"]=df["net_income"]/df["avg_equity"]*100
    df["fcf"]=df["cfo"]-df["capex"].abs()
    return df
def save_dashboard_json(df):
    rows=df.where(df.notna(), None).to_dict(orient="records")
    (PROCESSED_DIR/"nongshim_dashboard.json").write_text(
        json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8"
    )
