# Day 2: Read 10 numbers and find sum and average

sum = 0
print("Enter 10 numbers:")

for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    sum += num

average = sum / 10
print("Sum =", sum)
print("Average =", average)