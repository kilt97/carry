# 팬드리롬
# pop() 함수에서 인덱스 지정 가능 -> 0을 지정하면 맨 앞의 갚 가져올 수 있음
# 맨 뒷부분의 pop() 결과와 ㅁ채ㅣㅇ해 나가면서 일치하지 않는 경우 False를 리턴
# 전체 일치 시 True 리턴

#def isPalindrome(self, s: str) -> bool:   # 해당 메서드가 bool 타입의 값을 반환한다는 것을 의미합니다. 따라서 isPalindrome 메서드는 True 또는 False 중 하나를 반환

import re


def isPalindrome(s: str) -> bool:   # 해당 메서드가 bool 타입의 값을 반환한다는 것을 의미합니다. 따라서 isPalindrome 메서드는 True 또는 False 중 하나를 반환
    strs = []
    for char in s:
        if char.isalnum():    # isalnum()은 파이썬 문자열 메서드로, 해당 문자열이 알파벳(a-z, A-Z) 또는 숫자(0-9)로만 구성되어 있는지를 판별하는 기능을 제공
            strs.append(char.lower())    #  
    
    while len(strs) > 1:    # strs의 길이가 1보다 클 때까지 반복
        if strs.pop(0) != strs.pop():    
            return False 
  
    return True 



## strs.pop(0)은 리스트 strs에서 첫 번째 요소를 제거하고 반환하는 메서드
## strs.pop()은 리스트 strs에서 마지막 요소를 제거하고 반환하는 메서드




'''
def isPalindrome2(s: str) -> bool:
    s = s.lower()
    s = re.sub('[^a-z0-9]','',s)    # s = re.sub('[^a-z0-9]','',s): 정규 표현식 패턴 '[^a-z0-9]'를 사용하여 s에서 알파벳과 숫자 이외의 모든 문자를 제거합니다. re.sub() 함수는 패턴에 일치하는 문자열을 두 번째 인자로 대체하며, 세 번째 인자는 대상 문자열입니다. 따라서 이 코드는 알파벳과 숫자 이외의 문자를 빈 문자열로 대체하여 제거하는 역할을 합니다.
    return s == s[::-1]


result = isPalindrome2("a@(*)#(*i@#a")
print(result)  # True
'''