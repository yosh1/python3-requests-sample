import requests

url = "https://www.yoshi1125hisa.com"    # Url
r = requests.get(url, timeout=5)    # Get and setting timeout (5s) 
# Only url is OK
print(r.text)    # Text
print(r.encoding)    # Encode
print(r.status_code)    # Status code
print(r.headers)    # Header
print(r.content)    # Byte
