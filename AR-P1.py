"""
https://quera.ir/problemset/contest/3539/%D8%B3%D8%A4%D8%A7%D9%84-%D8%AA%DA%A9%D8%B1%D9%82%D9%85%DB%8C
"""
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