# 📌 IP Geolocation Finder

> A clean, fast IP metadata lookup tool built in Python using the [ipinfo.io](https://ipinfo.io) API.  
> by [@upliftedl](https://github.com/upliftedl)

**IP Geolocation Finder** is a lightweight OSINT utility to fetch details about an IP address—such as city, country, ISP, coordinates, and timezone.  
Useful for security researchers, analysts, and curious hobbyists.

---

## ⚙️ Prerequisites

- Python 3.7 or higher  
---

## 📦 Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/upliftedl/ip-geolocation-finder.git
cd ip-geolocation-finder
pip install -r requirements.txt
```
----
💻 Usage
Run the script using:

```bash
python ip_finder.py
```
You will be prompted to:
```bash
Enter a public IP address (e.g., 8.8.8.8)

Or leave it blank to fetch geolocation data for your own IP
```
----
📊 Project Structure
```bash
ip-geolocation-finder/
├── ip_finder.py
├── requirements.txt
├── LICENSE
└── README.md

```
🧪 Output Example
```bash
Enter an IP address (or leave blank for your own IP): 8.8.8.8

🌐 IP Address   : 8.8.8.8  
📍 Location     : Mountain View, California, US  
🗺️  Coordinates  : 37.4056, -122.0775  
🏢 Organization : AS15169 Google LLC  
⌛ Timezone     : America/Los_Angeles
```
----
⚠️ Legal Disclaimer

```bash
This tool is intended for educational and ethical OSINT usage only.
Information is sourced from ipinfo.io, which provides publicly accessible IP metadata.

Do not use this tool for:

Activities that violate privacy or data protection laws

Breaches of terms of service

Any unlawful, unethical, or malicious purposes
```
----
📄 License
Licensed under the MIT License.
----
💡 Powered By
🌐 ipinfo.io API — Free tier supports up to 50,000 requests/month.
