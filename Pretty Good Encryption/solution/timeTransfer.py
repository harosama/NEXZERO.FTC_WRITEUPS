from datetime import datetime
import pytz

# Original French date string
date_str = "03 janv. 2025 18:56:27"

# Map French abbreviated months to English
month_map = {
    "janv.": "Jan", "févr.": "Feb", "mars": "Mar", "avr.": "Apr", "mai": "May", "juin": "Jun",
    "juil.": "Jul", "août": "Aug", "sept.": "Sep", "oct.": "Oct", "nov.": "Nov", "déc.": "Dec"
}

# Replace the French month with English
for fr, en in month_map.items():
    if fr in date_str:
        date_str = date_str.replace(fr, en)
        break

# Parse the corrected date
dt = datetime.strptime(date_str, "%d %b %Y %H:%M:%S")

# Set timezone to CET
cet = pytz.timezone('CET')
localized_dt = cet.localize(dt)

# Get UNIX timestamp
timestamp = int(localized_dt.timestamp())
print(f"UNIX Timestamp: {timestamp}")
