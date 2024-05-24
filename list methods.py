l=[1,2,3,4]
#insertion

l.append(10)
print(l)

l.append("abcd")
print(l)

l.extend("abcd")
print(l)

#in append we cannot send multiple entities whether it is possible in extend

l.insert(2,10)
print(l)

#deletion

l.pop()
print(l)

l.pop(2)  # index
print(l)

l.remove(3) #object
print(l)

l.clear()
print(l)

#sorting
l=[2,4,3,5,6,9,8]
l.sort(reverse=True)
print(l)
print(sorted(l)) #sorted means returning in ascending order

#if strings passed in list they sort according to ascii values but if we want in according to length
l=["afdv","jsjbfe","hfkwe","fg","a"]
l.sort(key=len)

a=[[1,2,3],[2,3,4],[3,4,5],[4,5,65]]
print(sorted(a,key=sum))
#if we want to sort according to the largest second number in each sub list then create function according to requirement by using lambda
print(sorted(a,key=lambda x:x[1]))
