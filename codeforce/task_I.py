k = int(input())
fir = []
sec = []
sum1, sum2, sum3 = 0, 0, 0
for i in range(k):
    first, second = input().split()
    fir.append(int(first))
    sec.append(int(second))

fir_ = sum(fir)/k
sec_ = sum(sec)/k

for i in range(k):
    sum1 += (fir[i]-fir_)*(sec[i]-sec_)
    sum2 += (fir[i]-fir_)**2
    sum3 += (sec[i]-sec_)**2

if (sum2*sum3 != 0):
    r = sum1/(sum2*sum3)**0.5
else:
    r = 0
print(r)