import random
import string
 
# print(string.ascii_letters)
# print(string.digits)                    # just for reference
# print(string.punctuation)

pass_len = 8
charValues  = string.ascii_letters + string.digits + string.punctuation


# List comprehension [function for i in range(n)]       # syntax

password = "".join([random.choice(charValues) for i in range(pass_len)])   # using list comprehension


# password = ""
# for i in range(pass_len):                         #  this is normal method
#     password += (random.choice(charValues)) 

print("Your random password is:",password)