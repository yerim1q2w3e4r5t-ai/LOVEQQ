import requests
from .config import DART_API_KEY, DART_BASE_URL
class DartClient:
    def __init__(self):
        if not DART_API_KEY:
            raise RuntimeError("DART_API_KEY가 설정되지 않았습니다.")
        self.session = requests.Session()
    def get(self, endpoint, params):
        r = self.session.get(
            f"{DART_BASE_URL}/{endpoint}",
            params={"crtfc_key": DART_API_KEY, **params},
            timeout=30,
        )
        r.raise_for_status()
        data = r.json()
        if data.get("status") != "000":
            raise RuntimeError(f"DART API 오류: {data.get('status')} / {data.get('message')}")
        return data
