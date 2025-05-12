import random
from Crypto.Util.number import isPrime, long_to_bytes

# Encrypted flag and public key parameters
encrypted_flag = 74853691332836114322800517229156499048613454535610386971003097205742759876251090140905263359090728981373776584178902054210201249669100212238690032243086280755581059101008578139594809312713240761528256204631623830071930938346030753506265690147693386767699310604314708081927261896385917037161023323539415124969
e = 65537

# Correct timestamp range: 1735926987 - 1000 to 1735926987
start = 1735926987 - 1000
end = 1735926987

def generate_prime(bits, seed):
    random.seed(seed)
    while True:
        num = random.getrandbits(bits)
        num |= (1 << (bits - 1)) | 1  # Ensure it's odd and correct bit length
        if isPrime(num):
            return num

for timestamp in range(start, end + 1):
    try:
        p = generate_prime(512, timestamp)
        q = generate_prime(512, timestamp + 1)
        n = p * q
        phi = (p - 1) * (q - 1)
        d = pow(e, -1, phi)
        m = pow(encrypted_flag, d, n)
        flag = long_to_bytes(m)

        # Check if the flag starts with "nexus{"
        if flag.startswith(b"nexus{"):
            print(f"[*] Timestamp: {timestamp}")
            print(f"[*] Flag: {flag.decode('utf-8')}")
            break

    except Exception:
        continue