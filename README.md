📌 IP Geolocation Finder
A clean, fast IP metadata lookup tool built in Python using the ipinfo.io API.
by @upliftedl

IP Geolocation Finder is a lightweight OSINT utility to fetch details about an IP address—like city, country, ISP, and coordinates.
Perfect for security researchers, analysts, or curious hobbyists.

⚙️ Prerequisites
Python 3.7 or higher

Internet connection (to query the ipinfo.io API)

📦 Installation
bash
Copy
Edit
git clone https://github.com/your-username/ip-geolocation-finder.git
cd ip-geolocation-finder
pip install -r requirements.txt
💻 Usage
bash
Copy
Edit
python ip_finder.py
You will be prompted to:

Enter a public IP address (e.g., 8.8.8.8)

Or leave it blank to fetch info about your own IP

🧪 Output Example
yaml
Copy
Edit
Enter an IP address (or leave blank for your own IP): 8.8.8.8

🌐 IP Address: 8.8.8.8  
📍 Location: Mountain View, California, US  
🗺️ Coordinates: 37.4056, -122.0775  
🏢 Organization: AS15169 Google LLC  
⌛ Timezone: America/Los_Angeles
⚠️ Legal Disclaimer
This tool is intended for educational and ethical OSINT usage only.
Data is fetched from ipinfo.io, which provides publicly accessible metadata.

Please do not use this tool for:

Any activity that violates privacy

Actions breaching terms of service

Any unlawful or malicious purposes

📄 License
This project is licensed under the MIT License.

💡 Powered By
ipinfo.io API — Free for up to 50,000 requests per month.
