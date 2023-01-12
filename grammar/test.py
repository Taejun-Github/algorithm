array = [ i * i for i in range(1, 10)]
print(array)

n=3 
m=4
a=1
array2 = [[a + i] * m for i in range(n)]
print(array2)
# 언더바를 사용하는 경우? 반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할 때 사용한다.
print(array[1:3])

array3 = [i for i in range(20) if i % 2 == 1]
print(array3)

print(array[1:4])
a=[1,2,3,4,5,6]
remove_set={3,5}
result = [i for i in a if i not in remove_set]
print(result)

string = 'a '
print(string * 10)

dict = dict()
dict['사과'] = 'Apple'
print(dict)

test_value = lambda a, b: a + b
test_value2 = lambda a, b: a - b

def testFunc(func):
    print(func(10,40))

testFunc(test_value)
testFunc(test_value2)



import sys

data = sys.stdin.readline().strip()
print(data)
