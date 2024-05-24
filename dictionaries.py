# #taking input
# n=int(input())
# d={}
# for i in range(n):
#     key,val=map(int,input().split())
#     d[key]=val
# print(d)

#dictionaries functions
d={3333:4,4:5,6:7}
# print(d.keys())
# print(d.values())
# print(d.items())
print(d.pop(4)) #it must take arguments
print(d.get(3333)) 
print(d.setdefault(7,8),d)

#set default adds a key value pair and it does not override
#get gives the value ,if it is uninitialised it gives what we give the input