from .collector import collect
from .normalize import normalize
from .ratios import calculate, save_dashboard_json
def main():
    collect()
    df=calculate(normalize())
    save_dashboard_json(df)
    print("Nongshim DART pipeline completed.")
if __name__=="__main__":
    main()
