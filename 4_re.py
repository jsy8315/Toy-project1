#정규식
#정규식은 책1권이 나올 정도로 복잡하다
#웹스크랩핑에 필요한 것 위주로 할 거임ㅇㅇ

import re
#차량번호판은 4자리 문자로 구성되어 있다고 가정
#뺑소니를 봤는데 그 중 3개만 기억남. ca?e
# care, cafe, case, cave?
#어떻게 검색하지??일일이?

p = re.compile("ca.e") 
#.은 하나의 문자를 의미 ex) care, cafe
#^ 은 하나의 문자, ^은 문자열의 시작을 의미
#^ (de) : desk, destination, fade(x)
#$ (se$ : 문자열의 끝, case, base 같은 것들 face(x)

def print_match(m):

#m = p.match("cafe")
#print(m.group()) #매치되지 않으면 에러가 발생
    if m:
        print(m.group())
    else:
        print("매칭되지 않았습니다.")

m = p.match("case")
print_match(m)