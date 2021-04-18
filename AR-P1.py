"""
https://quera.ir/problemset/contest/3539/%D8%B3%D8%A4%D8%A7%D9%84-%D8%AA%DA%A9%D8%B1%D9%82%D9%85%DB%8C
"""
#target = '654' # 6+5+4 =15 ==> 1+5 = 6
target=input('target: ')
addd=list(target)
number=0
for x in range(len(addd)): number += int(addd[x])
print(number)
try:
    while not (number<10):
        y=0
        addd=list(str(number))
        for i in range(len(addd)+1):
            #print("I:",i)
            y += int(addd[i])
            number =y
            print(y)
       
except: None
