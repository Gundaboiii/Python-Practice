import math

lst1 = [3,4,2]
lst2 = [5,6,4]
first_number = 0
second_number = 0
for i in range(0,len(lst1)):
    first_number += lst1[i] * math.pow(10,i)
for i in range(0,len(lst2)):
    second_number += lst2[i] * math.pow(10,i)
final_number = first_number + second_number
print(final_number)
lst = []
while(final_number>= 1):
    digit = int(final_number%10)
    lst.append(digit)
    final_number = final_number /10
lst = lst[::-1]
print(lst)