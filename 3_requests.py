#웹페이지의 정보를 가져오는 라이브러리
import requests
res = requests.get("http://google.com")
res.raise_for_status() #올바르게 가져오지 않았을 경우에는 에러를 내버림

#print("응답코드 :", res.status_code) #200이면 정상

# if res.status_code == requests.codes.ok:
#     print("정상입니다")
# else:
#     print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")

print(len(res.text))
# print(res.text)

with open("mygoogle.html", "w", encoding="utf=8") as f:
    f.write(res.text)