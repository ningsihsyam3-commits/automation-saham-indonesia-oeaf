import yfinance as yf
import requests
from datetime import datetime

# URL Web App Google Apps Script Anda
WEB_APP_URL = "https://script.google.com/macros/s/AKfycbw8-15rcSs_-h9aSb-rhLBAnWBoYPDhyNCrlAmFz-yeoYyma_yRcQuhmC_MCh1FVlA70g/exec"

def get_real_stock_data():
    # Daftar ticker (Yahoo Finance menggunakan akhiran .JK untuk saham Indonesia)
    tickers = ["BBRI.JK", "BMRI.JK", "BBNI.JK"]
    all_data = []
    
    for symbol in tickers:
        try:
            # Mengambil data ticker
            stock = yf.Ticker(symbol)
            # 'fast_info' memberikan akses cepat ke harga terakhir dan perubahan
            info = stock.fast_info
            
            # Membersihkan nama ticker untuk tampilan di Sheets (menghapus .JK)
            clean_name = symbol.replace(".JK", "")
            
            data = {
                "ticker": clean_name,
                "price": round(info.last_price, 2),
                "change": f"{round(info.year_change * 100, 2)}%", # Contoh perubahan
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            all_data.append(data)
            print(f"✅ Berhasil mengambil data: {clean_name}")
            
        except Exception as e:
            print(f"❌ Gagal mengambil {symbol}: {e}")
            
    return all_data

def send_to_sheets():
    stocks_data = get_real_stock_data()
    if not stocks_data:
        return

    try:
        response = requests.post(WEB_APP_URL, json=stocks_data, timeout=30)
        if response.status_code == 200:
            print(f"🚀 {len(stocks_data)} data asli berhasil dikirim ke Google Sheets!")
    except Exception as e:
        print(f"❌ Error pengiriman: {e}")

if __name__ == "__main__":
    send_to_sheets()
