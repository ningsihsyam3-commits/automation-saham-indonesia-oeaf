import requests
from datetime import datetime

# Pastikan URL ini adalah URL Web App yang berakhiran /exec
WEB_APP_URL = "https://script.google.com/macros/s/AKfycbxx1aaTeg2vnKm8COkSvmj1i02ACRSw0P4VyIQ5pkcHdkcW45LGwE39bVsBMF-dTIy0eQ/exec"

def get_stock_data():
    # Simulasi pengambilan data (Nanti bisa dikembangkan dengan Playwright)
    # Untuk sekarang kita pastikan alur datanya benar dulu
    return {
        "ticker": "BBRI",
        "price": 5250,
        "change": "+1.2%",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

def send_to_sheets():
    data = get_stock_data()
    try:
        response = requests.post(WEB_APP_URL, json=data, timeout=30)
        if response.status_code == 200:
            print(f"✅ Berhasil! Data {data['ticker']} terkirim.")
    except Exception as e:
        print(f"❌ Gagal: {e}")

if __name__ == "__main__":
    send_to_sheets()
