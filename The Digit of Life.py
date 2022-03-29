a = input("YYYYMMDD:")
print("YYYYMMDD" + str(a))
summ = 0
for num in a:
    summ += int(num)
      
    if summ > 9:
        summ = summ % 10 + summ // 10
print(str(summ))