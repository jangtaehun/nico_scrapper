from requests import *

results ={}

websites = (
"google.com",
"facebook.com",
"https://naver.com",
"daum.net"
)

for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    print(website) # 모든 website에서 작동

    response = get(website) # get = response를 return한다
    if response.status_code == 200:
        results[website] = "OK"
    else:
        results[website] = "FAILED"


for i in range(len(websites)):
    if not websites[i].startswith("https://"):
        websites[i] = f"https://{websites[i]}"
print(websites)

print(results)