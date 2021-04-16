n = int(input('n:'))
k = int(input('k:'))

res1=[]
res2=[]

for i in range(1,n+1):
	if i % 2==0:
		res1.append(i)
	if not (i%2==0):
		res2.append(i)

res1 = res1[::-1]
answer=res2+res1

print(answer , answer[k-1])

'''
1 3 5 7 9 10 8 6 4 2
0 1 2 3 4 5  6 7 8 9
'''
