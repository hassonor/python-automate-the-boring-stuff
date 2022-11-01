import hashlib

statement = "Hello My Name is Or Hasson"
print("Original Message: " + statement)

statement = statement.encode()

# result = hashlib.sha256(statement)
result = hashlib.md5(statement)
print(" The hexadecimal hashed value: " + result.hexdigest())

print("Hardcoded md5 hash of python file from site: e7062b85c3624af82079794729618eca")
filename = "c:\\python64bit.exe"
with open(filename, "rb") as f:
    bytes_of_file = f.read()
    hash_output = hashlib.md5(bytes_of_file).hexdigest();
    print("md5 hash of file python64bit.exe: " + hash_output)
