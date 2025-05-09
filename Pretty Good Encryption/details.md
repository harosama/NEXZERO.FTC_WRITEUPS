
## What is PGP?

**Pretty Good Privacy (PGP)** is an encryption program that provides cryptographic privacy and authentication for data communication. It is used for signing, encrypting, and decrypting text, emails, files, directories, and even entire disk partitions.

PGP was created by **Phil Zimmermann** in **1991** and is commonly used to increase the security of email communications and digital signatures.

---

### 1. Import the Public Key

We were given a PGP public key file `publickey.asc`. To begin, we imported it using:

`gpg --import publickey.asc`

2. Verify the Signed Message

Then we used GPG to verify the signed message:

`gpg --verify signed_message.asc`

This gave us the date and time when the message was signed:

''
03 Jan 2025 18:56:27

3. Convert Time to UNIX Timestamp

We used a helper script timeTransfer.py to convert the signed message timestamp into a UNIX timestamp in CET timezone:


The result was:
UNIX Timestamp: 1735926987


4. 🔓 Brute-force Around the Timestamp
We knew from the challenge that this was not the exact time the RSA key was generated, but close  within about a ±1000 seconds window.

The RSA primes p and q were generated using Python’s random module with a timestamp as the seed:
random.seed(timestamp)

Since the same seed always produces the same primes, we could brute-force all seeds in the range [1735925987, 1735926987].

Using this interval, we tested each timestamp to regenerate the RSA keys, compute the private key d, and decrypt the message 


After iterating through the timestamps, we found the correct one:

[*] Timestamp: 1735926966
[*] Flag: nexus{PGP_4nd_RSA_are_1337!}

see the code in sol.py





