


def encpt(content,key):
    cipher=''
    for x in content:
      a=ord(x)
      if a>=97 and a<=122:
        a=(a-97+int(key))%26+97
        cipher=cipher+chr(a)
      else:
        cipher=cipher+x
    print(cipher)

def decpt(cipher,key):
    content=''
    for x in cipher:
      a=ord(x)
      if a>=97 and a<=122:
        a=(a-97-int(key))%26+97
        content=content+chr(a)
      else:
        content=content+x
    print(content)


print('encrypt type e,decrypt type d')
mode=input()
if mode=='e':
  print('please input letters')
  content = input()
  print('key please')
  key=input()
  if key=='':
    key='3'
  encpt(content,key)
elif mode=='d':
  print('please input letters')
  content = input()
  print('key please')
  key=input()
  if key=='':
    key='3'
  decpt(content,key)
else:
  print('please set the mode')
