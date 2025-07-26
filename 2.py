# 1 задача
l=[1,2,1,'dub',3,'dub','aaa',4,4]
dub=[]
for item in l:
    if l.count(item) >1 and item not in dub:
        dub.append(item)

print(dub)

# 3 задача
d={'name1': 'id1', 'name2': 'id2'}
sl={}

for key, value in d.items():
    sl[value]=key

print('Первоначальный словарь: ', d)
print('Новый словарь:', sl)
