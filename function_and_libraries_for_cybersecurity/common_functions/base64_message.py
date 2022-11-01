import base64

statement = "Hello my name is Or Hasson"
print("Original Message: " + statement)

# Encoding
m_bytes = statement.encode()
base64_bytes = base64.b64encode(m_bytes)
base64_encoded = base64_bytes.decode()
print("base64 Encoded Message: " + base64_encoded)

# Decoding
base64_bytes = base64_encoded.encode()
message_bytes = base64.b64decode(base64_bytes)
statement = message_bytes.decode()
print("base64 Decoded Message: " + statement)
