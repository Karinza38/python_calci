# file: calci.py
f=open("input.txt","r")
for line in f:
      if '+' in line:
        x=line.split('+')
        print(int(x[0])+int(x[1]))
      if '-' in line:
        x=line.split('-')
        print(int(x[0])-int(x[1]))
      if '*' in line:
        x=line.split('*')
        print(int(x[0])*int(x[1]))
      if '/' in line:
        x=line.split('/')
        print(int(x[0])/int(x[1]))
f.close

