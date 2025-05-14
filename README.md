# 📌 IP Geolocation Finder

> A clean, fast IP metadata lookup tool built in Python using the [ipinfo.io](https://ipinfo.io) API.

**IP Geolocation Finder** is a simple OSINT utility to fetch IP address details like city, country, ISP, and coordinates. Useful for security researchers, analysts, and hobbyists.

---

## ⚙️ Prerequisites

- Python 3.7+
- pip (Python package manager)
- Internet connection

---

## 📦 Installation

```bash
git clone https://github.com/your-username/ip-geolocation-finder.git
cd ip-geolocation-finder
pip install -r requirements.txt
💻 Usage
bash
Copy code
python ip_finder.py
You will be prompted to:

Enter a public IP address (e.g., 8.8.8.8)

Or leave it blank to fetch info about your own IP

🧪 Output Example
yaml
Copy code
Enter an IP address (or leave blank for your own IP): 8.8.8.8
🌐 IP Address: 8.8.8.8
📍 Location: Mountain View, California, US
🗺️ Coordinates: 37.4056,-122.0775
🏢 Organization: AS15169 Google LLC
⌛ Timezone: America/Los_Angeles
🚨 Legal Disclaimer
This tool is intended for educational and ethical OSINT usage only.
Data is sourced from ipinfo.io, which provides public information based on IP.
Avoid usage in any activity that violates privacy, terms of service, or the law.

📄 License
Licensed under the MIT License

📦 Powered by the ipinfo.io API, free for 50k requests/month.