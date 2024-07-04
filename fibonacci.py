first_number = 0
second_number = 1
sum = 0
n = int(input("Enter a Number :"))
for i in range(n):
    print(sum)
    sum = first_number + second_number
    first_number = second_number
    second_number = sum