# 1 задача
import math

def area():
    print('Введите стороны треугольника: ')
    a = float(input('Введите а: '))
    b = float(input('Введите b: '))
    c = float(input('Введите c: '))

    if a+b>c and a+c>b and b+c>a:
        p=(a+b+c)/2
        area_value=math.sqrt(p*(p-a)*p-b*p-c)
        print(area_value)
    else:
        print('Такого треугольника не существует')

area()

# 2 задача
s= '''Было просто пасмурно, дуло с севера
А к обеду насчитал сто градаций серого.
Так всегда первого ноль девятого
То ли весь мир сошёл с ума, то ли я - того...'''

def short(text):
    words=text.split()
    result=[]
    for word in words:
        cl=word.strip('.,!?-')
        if len(cl)<5:
            result.append(cl)
    return result
print(short(s))

# 3 задача
def max(arr):
    str_num=[str(num) for num in arr]
    for i in range(len(str_num)):
        for j in range(i+1, len(str_num)):
            if str_num[i]+str_num[j]<str_num[j]+str_num[i]:
                str_num[i],str_num[j]=str_num[j],str_num[i]
    result=''.join(str_num)
    return int(result) if result else 0

print(max([56, 9, 11, 2]))
