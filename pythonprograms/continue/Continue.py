#sum of all odd numbers
sum = 0
for i in range(1, 10):
    if i % 2 == 0:
        continue
    print("i = ", i)

    sum = sum + i
    print("sum = ", sum)

print('Total:', sum)
