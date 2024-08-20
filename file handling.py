# file handling which is used to store data or information in file with the help of program.

# f=open('file1.txt','w')
# f.write('FS developer')
# f.close()




# f=open('file2.txt','r')
# print(f.read())
# f.close()




f=open('file2.txt','w')

students=[]

for i in range(3):
    roll_no=input('Enter your roll no:')
    name=input('Enter your name:')
    contact=input('Enter your contact:')
    email=input('Enter your email:')

    t=(roll_no,name,contact,email)

    students.append(t)

for i in students:
    f.write(i[0]+'\t'+i[1]+'\t'+i[2]+'\t'+i[3]+'\n')
f.close()





































