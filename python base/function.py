def average(number, *args):
    sum = number
    count = 1
    for numbers in args:
        sum += number
        count += numbers
    return sum/count
    

print(f'average of 1,2,3,4,5 is {average(1,2,3,4,5)}')
"""
args 前面加*可以加入无限多的argument 但是要注意有可能会出错
"""


def kwargs(name,email):
    return name+" "+email
​
print(f'my name and email is {kwargs(name = "bene",email = "86663350@qq.com")}')
print(f'my name and email is {kwargs(email = "86663350@qq.com", name = "bene")}')
​
"""
!!!                                     point here                                  !!!
1, 在叫方法的时候给args命名可以不用管当初做method的时候，定下来的argument的排列顺序
"""


def kwargs_v2(name,**kwargs):
    kwargs['name'] = name
    for (keys, values) in kwargs.items():
        print(f'{keys} --> {values}')

kwargs_v2("bene",exam1 = 1213 , exam2 = 145, exam3 = 1245)

#错误：忘了加items（）