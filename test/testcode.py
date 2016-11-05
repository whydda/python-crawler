# set으로 값 체크 하기
set_1 = set()
set_1.add("a")
print('b' in set_1)
print('b' not in set_1)
print(set_1)

# indexof 와 같은 find
find_1 = "hihi nice";
find_2 = "1";
find_3 = "hi";

print(find_1.find(find_2))
print(find_1.find(find_2))

# 대문자로 변환
upper_1 = 'aBc'
upper_2 = upper_1.upper()
print (upper_2)

# 모든 알파벳을 소문자로 변환
lower_1 = 'AbC'
lower_2 = lower_1.lower()
print(lower_2)

#함수 문법
def returnTure():
    return 0

print(returnTure())

def returnFalse():
    return 1

print(returnFalse())

#키보드 입력 받기 input
print("키보드로 아무거나 입력하세요...")
input = input()
print(input)

#setter getter
class users(object):
    def __init__(self):
        self.id = None

    @id.getter
    def getId(self):
        print(self.id)
        return self.id

    @id.setter
    def setId(self, value):
        self.id = value

    # @id.deleter
    # def x(self):
    #     print "deleter of x called"
    #     del self._x