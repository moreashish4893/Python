a={'name':'abc','age':40,'city':'kalyan'}
print(a['name'])
print(a.get('name'))
print(a.get('age'))

a['phone']=234145
a.update({'tel':675328})


a.pop('name')
a.popitem()
#a.clear()
del a['age']
print(a)