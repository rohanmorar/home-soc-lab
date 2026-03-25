import os
import sys
import requests

API_KEY = os.getenv("ABUSEIPDB_API_KEY")

def check_ip(ip: str):
    if not API_KEY:
        print("Error: ABUSEIPDB_API_KEY environment variable is not set.")
        sys.exit(1)

    url = "https://api.abuseipdb.com/api/v2/check"
    headers = {
        "Key": API_KEY,
        "Accept": "application/json"
    }
    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90,
        "verbose": ""
    }

    response = requests.get(url, headers=headers, params=params, timeout=15)
    response.raise_for_status()
    return response.json()

def main():
    if len(sys.argv) != 2:
        print("Usage: python ip_enrich.py <ip>")
        sys.exit(1)

    ip = sys.argv[1]
    data = check_ip(ip)

    result = data.get("data", {})
    print(f"IP: {result.get('ipAddress')}")
    print(f"Abuse Confidence Score: {result.get('abuseConfidenceScore')}")
    print(f"Country: {result.get('countryCode')}")
    print(f"ISP: {result.get('isp')}")
    print(f"Usage Type: {result.get('usageType')}")
    print(f"Total Reports: {result.get('totalReports')}")
    print(f"Last Reported At: {result.get('lastReportedAt')}")

if __name__ == "__main__":
    main()