a = 4
while a < 10:
    print(a)
    a = a + 1

#break on first even number
b = 5
while b > 0:
    if b % 2 == 0:
        print("even number is", b)
        break
    else:
        b = b - 1
