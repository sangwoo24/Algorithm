import hashlib

s = input().encode()
SHA = hashlib.sha256(s).hexdigest()
print(SHA)