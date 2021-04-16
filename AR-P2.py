"""
https://quera.ir/problemset/contest/10230/%D8%B3%D8%A4%D8%A7%D9%84-%D9%85%D8%B4%D9%82-%D8%A7%D9%85%D8%B4%D8%A8-%D8%A8%D8%A7%D9%82%D8%B1
"""
x,y,z=int(input("x: ")),int(input("y: ")),int(input("z: "))
sum= x+y+z
if x and y and z ==0 :print("No")
else:
    if sum==180: print("Yes")
    else: print("No")