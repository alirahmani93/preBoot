"""
به عنوان ورودی ابتدا یک عدد n میگیرید سپس در خط بعدی n تا عدد دیگر دریافت میکنید.

به یک عدد T-Prime میگوییم اگر دقیقا ۳ تا مقسوم علیه داشته باشد.
به ازای n تا عدد دریافت شده بگویید T-Prime هستن یا خیر
Input
4
2 4 5 6
Output
No
Yes
No
No"""
n= int(input('n: '))
nums=[]
for i in range(n): nums.append(int(input('number is: ')))
###############
for i in nums:
    T=0
    for j in range(1,i+1):
        if i%j==0:
            T=T+1

    if T==3: 	print('Yes')
    else: 		 print('No')