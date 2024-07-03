a= int(input("Enter a Number: "))
count = 0
for i in range(2,a):
    if a%i==0:
        count = count + 1
if count > 0:
    print(a,"is ot Prime")
else:
    print(a,"is Prime")