# Positional argument function
def data(name,age,city):
    return f"my name is {name},my age is {age} and i live in {city}"

print(data('Ashish',28,'Mumbai'))
print(data('Shreyansh',10,'Badlapur'))


# Key word argument function
def data(name,age,city):
    return f"my name is {name},my age is {age} and i live in {city}"
print(data(age=28,city='Mumbai',name='Ashish'))


 