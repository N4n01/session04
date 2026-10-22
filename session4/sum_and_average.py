numbers = int(input("How many numbers? "))
total = float(0)
for i in range(0, numbers) :
    num = float(input(f"Number {i+1}: "))
    total += num
print(f"Sum: {total}")
print(f"Average: {total/numbers}")