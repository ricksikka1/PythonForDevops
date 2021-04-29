import hashlib

secret = "This is the password"

bsecret = secret.encode()

m = hashlib.md5()
m.update(bsecret)

print(m.digest())