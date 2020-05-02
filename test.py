import sys

import requests

print(sys.executable)
r = requests.get("https://www.google.com")
print(r.status_code)

d = input("Your Name: ")
test = "Test"
print("Hello", d)
print(r.ok)
