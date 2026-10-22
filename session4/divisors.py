num = int(input("Number: "))
div = []
for i in range(1, num+1):
    if num % i == 0 :
        div.append(str(i))
div = ' '.join(div)
print(f"Divisors of {num}: {div}")