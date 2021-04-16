"""# 7
یک عدد n به عنوان ورودی دریافت میکنیم.
بین هر دو عددی در بازه 1 تا n ب.م.م یا همون GCD میگیریم.
بزرگترین ب.م.م بین همه ب.م.م های به دست اومده چه عددی هستش؟
Input : 3
Output: 1
GCD(1,2)=1
GCD(1,3)=1
GCD(2,3)=1
Input: 5
Output:2
"""

#import math
import numpy as np
n = int(input('N is: '))
x = range(1, n + 1)
sq=set()
for i in range(1, n + 1):
    for j in range(1, i):
        c = np.gcd(i, j)
        sq.add(c)
    print('sq:',sq)
print('sq:',sq)
print('max gcd:',max(sq))





