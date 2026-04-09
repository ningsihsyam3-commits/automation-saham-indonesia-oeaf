import requests

# TEMPEL URL BARU ANDA DI SINI
WEB_APP_URL = "https://script.google.com/macros/s/AKfycbxx1aaTeg2vnKm8COkSvmj1i02ACRSw0P4VyIQ5pkcHdkcW45LGwE39bVsBMF-dTIy0eQ/exec"

def send_to_sheets():
    # Data simulasi untuk mengetes koneksi dari GitHub
    payload = {
        "ticker": "BBRI-GITHUB-TEST",
        "price": "5200",
        "change": "0.5%",
        "timestamp": "Terkirim dari GitHub"
    }
    
    try:
        response = requests.post(WEB_APP_URL, json=payload, timeout=30)
        print(f"Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")
        
        if response.status_code == 200:
            print("✅ Berhasil mengirim data ke Google Sheets!")
        else:
            print("❌ Gagal. Pastikan URL Web App sudah diset ke 'Anyone'.")
    except Exception as e:
        print(f"❌ Error Terjadi: {e}")

if __name__ == "__main__":
    send_to_sheets()
