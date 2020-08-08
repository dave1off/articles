import sys
import ascii
import utf8

string: str = sys.argv[1]
encoding: str = sys.argv[2]

encoded: list = []
decoded: str = ""

if encoding == "ascii":
    encoded = ascii.encode(string)
    decoded = ascii.decode(encoded)
elif encoding == "utf8":
    encoded = utf8.encode(string)
    decoded = utf8.decode(encoded)

print("Encoded:", encoded)
print("Decoded:", decoded)
