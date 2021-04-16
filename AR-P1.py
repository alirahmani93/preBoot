#target= int(input("Target is: "))
target = '654' # 6+5+4 =15 ==> 1+5 = 6
T=list(target)
print(T)
while len(T)>1:
    x=T
    if len(list(str(x))) > 1:
        for i in T:
            x+=int(i)
    else:
        print(x)