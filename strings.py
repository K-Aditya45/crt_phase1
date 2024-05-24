#s='gvuhg7yfyrdgfchgcy'
# print(s.capitalize())
# print(s.title())
# print(s.lower())
# print(s.swapcase())

# print(s.istitle())
# print(s.islower())
# print(s.isupper())

# print(s.index('h',5,15))
# print(s.rindex('g'))
# print(s.count('h'))
# print(s.find('h'))

# print(s.startswith('gv'))
# print(s.startswith('fy',7))
# print(s.endswith('gfy'))
#print(s.replace('a','b'))

# var1 = "geeks"
# var2 = "for"
# var3 = "geek"
 
# max_val = max(var1, var2, var3,
#             key=len)
# print(max_val)

s="hgf hGF abdh"
print(s.split()) #returns list and breaks given index
print(s.split('h',maxsplit=1))
print(s.split('h',maxsplit=2))
print(s.partition('h')) #returns tuple breaks before the index and the given index also printed