'''
예제 1
'''
def number_generator(n):
    print("Function Start")
    while n < 6:
        yield n
        n += 1
    print("Function End")

'''
    결과 :
    Function Start
    0
    1
    2
    3
    4
    5
    Function End
    '''
for i in number_generator(0):
    print(i)


'''
예제 2
'''
import time


def sleep_function(x):
    print("sleep...")
    time.sleep(1)
    return x


# list 생성
list = [sleep_function(x) for x in range(5)]

# generator 생성
generator = (sleep_function(y) for y in range(5))

for i in list:
    print(i)

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=")

for j in generator:
    print(j)