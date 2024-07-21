lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
	ele = int(input())
	lst.append(ele) 
print(lst)
target = int(input("Enter Target number to check if two numbers from list add up to this number: "))
target_lst = []
for i in range(0,n-1):
	for j in range(i+1,n):
		if lst[i] + lst[j] == target:
			target_lst.append(lst[i])
			target_lst.append(lst[j])
			break
		else:
			continue
if target_lst == []:
	print("No two numbers from list add up to this number")
else:
	print(target_lst)
