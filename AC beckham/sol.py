import base64

# Original string
s = "n11z01sXq9815LtpN103Tam09Bqg81AyfoX013og9blV6W8jqkV1puw30r1qo5Px9i2B8t11l5Td98a4Tn10gr2F6m8cGl95r1Din1jT0l84Z9tei1Jb8eE40De9mj1Tg1i2D1k701ik8"

# Clean and uppercase, remove invalid chars for base32
import re
cleaned = re.sub(r'[^A-Za-z2-7]', '', s).upper()

# Pad to length multiple of 8
pad_len = (8 - len(cleaned) % 8) % 8
cleaned += '=' * pad_len

try:
    decoded = base64.b32decode(cleaned, casefold=True)
    print(decoded.decode('utf-8', errors='ignore'))
except Exception as e:
    print("Error:", e)