"""https://quera.ir/contest/assignments/923/problems/3360"""
n,x,y= int(input("distance from wall: ")),int(input("foot Width: ")),int(input("foot Length: "))

n_per_y= n//y
n_per_x= n//x
remain= n-(n_per_y*y)

#print(n_per_x,n_per_y)
if  remain%x ==0:
    print(n_per_y,remain//x)
else: print(-1)