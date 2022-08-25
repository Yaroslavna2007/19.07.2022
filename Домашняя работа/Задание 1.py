sum = 1
sum1 = 0
number = int(input())
for i in range(1, number + 1):
    sum *= i
    sum1 += sum
print(sum1)
