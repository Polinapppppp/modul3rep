# 1 задача
x=int(input('Введите начальную сумму вклада: '))
y=int(input('Введите желаемую сумму: '))
p=int(input('Введите процент: '))

yrs=0

while x<y:
    x += x*p//100
    yrs+=1

print(yrs)

# 2 задача
n=int(input('Введите кол-во повторений: '))
count=0

while count < n:
    print('for - частный случай цикла while')
    count += 1

# 3 задача
number=input('введите целое число: ')
sum=0

for d in number:
    sum += int(d)

print(sum)
