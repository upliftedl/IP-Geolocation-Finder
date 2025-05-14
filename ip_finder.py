import requests

def get_ip_info(ip=None):
    if ip:
        url = f"https://ipinfo.io/{ip}/json"
    else:
        url = "https://ipinfo.io/json"
    
    try:
        response = requests.get(url)
        data = response.json()
        if "bogon" in data:
            print("❌ Error: private range")
            return

        print(f"🌐 IP Address: {data.get('ip', 'N/A')}")
        print(f"📍 Location: {data.get('city', 'N/A')}, {data.get('region', 'N/A')}, {data.get('country', 'N/A')}")
        print(f"🗺️ Coordinates: {data.get('loc', 'N/A')}")
        print(f"🏢 Organization: {data.get('org', 'N/A')}")
        print(f"⌛ Timezone: {data.get('timezone', 'N/A')}")
    except requests.RequestException:
        print("❌ Error: Unable to fetch data")

if __name__ == "__main__":
    ip = input("Enter an IP address (or leave blank for your own IP): ").strip()
    get_ip_info(ip if ip else None)
