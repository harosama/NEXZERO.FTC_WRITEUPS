def xor_all_lines(filename):
    from binascii import unhexlify

    result = None

    with open(filename, 'r') as f:
        for line in f:
            hex_str = line.strip()
            if not hex_str:
                continue  # Skip empty lines

            try:
                data = unhexlify(hex_str)
            except Exception as e:
                print(f"Invalid hex on line: {hex_str}")
                continue

            if result is None:
                result = bytearray(data)
            else:
                # XOR current line's data with the result
                for i in range(min(len(result), len(data))):
                    result[i] ^= data[i]

    return bytes(result) if result else b''

# Example usage
filename = '/content/cList'  # Replace with your actual file
flag_bytes = xor_all_lines(filename)

try:
    print("Flag:", flag_bytes.decode('utf-8'))
except UnicodeDecodeError:
    print("Flag (raw bytes):", flag_bytes)
    print("Flag (hex):", flag_bytes.hex())