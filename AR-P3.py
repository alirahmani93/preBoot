"""https://quera.ir/contest/assignments/9960/problems/32897
3       2       1
3,1     2,1     1 =5
4       3       1 =8
"""
x= int(input("X is: "))
sum=0
count=0
for j in range(1,x+1):
#    print("J is: ",j)
    for i in range(1,j+1):
        if j % i ==0:
#            print(i)
            sum+=i
            count+=1
print(count , sum)