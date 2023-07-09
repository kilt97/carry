# 문자열을 뒤집는 함수를 작성, 입력값은 문자 배열이고 리턴없이 리스트 내부를 직접 조작 


# 풀이1. 투 포인터를 이용한 스왑

def reverseString(s: list[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:    # left와 right가 교차할 때까지 반복
        s[left], s[right] = s[right], s[left]   # s[l  



def reverseString2(s: list[str]) -> None:
    s.reverse()



reverseString(["h","e","l","l","o"])