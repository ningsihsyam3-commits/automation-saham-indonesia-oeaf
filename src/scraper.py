import yfinance as yf
import requests
from datetime import datetime

# URL Web App Google Apps Script Anda
WEB_APP_URL = "https://script.google.com/macros/s/AKfycbxOUZ5SNQDY4el8cHaMUyhSACDXMn2D5GjyWDRKZkyBMlAYEs_-ydmcJ-Jv-eX85cQHDw/exec"

def get_real_stock_data():
    tickers = ["BBRI.JK", "BMRI.JK", "BBNI.JK", "TLKM.JK", "ASII.JK"]
    all_data = []
    
    print(f"Memulai pengambilan data untuk {len(tickers)} saham...")
    
    for symbol in tickers:
        try:
            stock = yf.Ticker(symbol)
            info = stock.fast_info
            clean_name = symbol.replace(".JK", "")
            
            # Ambil harga terakhir
            price = info.last_price
            
            # Jika harga valid (bukan None atau 0)
            if price:
                data = {
                    "ticker": clean_name,
                    "price": round(price, 2),
                    "change": "0%", # Placeholder
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                all_data.append(data)
                print(f"✅ Berhasil: {clean_name} - Rp{price}")
            else:
                print(f"⚠️ Peringatan: {clean_name} memberikan harga kosong.")
                
        except Exception as e:
            print(f"❌ Gagal pada {symbol}: {e}")
            
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
