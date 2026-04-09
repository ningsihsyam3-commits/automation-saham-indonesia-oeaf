import requests
from datetime import datetime

# URL Web App Anda
WEB_APP_URL = "https://script.google.com/macros/s/AKfycbw8-15rcSs_-h9aSb-rhLBAnWBoYPDhyNCrlAmFz-yeoYyma_yRcQuhmC_MCh1FVlA70g/exec"

def get_multiple_stocks():
    # Daftar saham yang ingin dipantau
    tickers = ["BBRI", "BMRI", "BBNI", "TLKM"]
    all_data = []
    
    for ticker in tickers:
        # Di sini nantinya Anda masukkan kode scraping asli (Playwright/BeautifulSoup)
        # Untuk sekarang, kita gunakan data simulasi agar alur sistem teruji
        stock_info = {
            "ticker": ticker,
            "price": 5000, # Ganti dengan hasil scraping
            "change": "+1.0%",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        all_data.append(stock_info)
    
    return all_data

def send_to_sheets():
    stocks_data = get_multiple_stocks()
    try:
        # Kita kirim seluruh list (all_data) dalam satu kali request POST
        response = requests.post(WEB_APP_URL, json=stocks_data, timeout=30)
        if response.status_code == 200:
            print(f"✅ Berhasil! {len(stocks_data)} data saham terkirim.")
    except Exception as e:
        print(f"❌ Gagal: {e}")

if __name__ == "__main__":
    send_to_sheets()
