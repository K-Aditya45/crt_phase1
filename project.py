# a=list(input())
# b=list(input())
# s="flames"
# for i in a:
#     if i in b:
#         a.remove(i)
#         b.remove(i)
# print(a,b)




s1=input("Enter name1").strip()
s2=input("Enter name2").strip()
flames=['Family','lust','affection','marriage','enmity','sister']
s1=list(s1)
s2=list(s2)
count=0
for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i]==s2[j]:
            s1[i]='0'
            s2[i]='0'
            break
l=s1+s2
for i in l:
    if i!='0':
        count+=1
while len(flames)>1:
    n=len(flames)
    r=(count%n)-1
    if r>=0:
        right=flames[r+1:]
        left=flames[:r]
        flames=right+left
    else:
        flames=flames[:len(flames)-1]

      