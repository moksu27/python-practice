import re

m = re.search(r'[^abc]aron','#aron')
print(m.group())

a= 'abcdef\n'
print(a)

b= r'abcdef\n'
print(b)