# try:
#     print(10/0) #work like if
# except IndexError:
#     print("you are not dividing with zero")  #if try block satisfies it will print
# except:
#     print("you are dividing with zero")
# finally:                                     #print whatever it may be
#     print("vhjgb")
def fun(l):
    try:
        n=len(l)
        o=l[0//l[n]]
    except ZeroDivisionError:
        print("zero division error")
    except NameError:
        print("name error")
    finally:
        print("end")

try:
    l=[1,2,3,4,5]
    fun(l)
except IndexError:
    print("index error")
finally:
    print("end of finally")

#raise
    raise indexerror("ghcfdtfhf")