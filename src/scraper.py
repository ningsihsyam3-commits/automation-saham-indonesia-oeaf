import requests
from datetime import datetime
from playwright.sync_api import sync_playwright

# Masukkan URL Web App Google Apps Script Anda di sini
WEB_APP_URL = "https://script.google.com/macros/s/AKfycbxx1aaTeg2vnKm8COkSvmj1i02ACRSw0P4VyIQ5pkcHdkcW45LGwE39bVsBMF-dTIy0eQ/exec"

def scrape_saham():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Mengambil data BBRI dari Yahoo Finance
        url = "https://finance.yahoo.com/quote/BBRI.JK"
        page.goto(url)
        
        # Menunggu elemen harga muncul
        page.wait_for_selector('fin-streamer[data-field="regularMarketPrice"]')
        
        # Mengambil harga dan perubahan persen
        price = page.query_selector('fin-streamer[data-field="regularMarketPrice"]').inner_text()
        change = page.query_selector('fin-streamer[data-field="regularMarketChangePercent"]').inner_text()
        
        browser.close()
        return price, change

def send_to_sheets(price, change):
    data = {
        "ticker": "BBRI.JK",
        "price": price,
        "change": change,
        "timestamp": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }
    
    # Mengirim data ke Google Sheets melalui Apps Script
    response = requests.post(WEB_APP_URL, json=data)
    if response.status_code == 200:
        print(f"✅ Berhasil! Harga BBRI: {price} dikirim ke Sheets.")
    else:
        print(f"❌ Gagal mengirim. Status: {response.status_code}")

if __name__ == "__main__":
    try:
        harga, perubahan = scrape_saham()
        send_to_sheets(harga, perubahan)
    except Exception as e:
        print(f"⚠️ Terjadi error: {e}")
