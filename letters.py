a = input("Enter a String: ")
vowels = 0 
consonants = 0
vow_list = ['a','e','i','o','u','A','E','I','O','U']
for i in range(len(a)):
    if a[i] in vow_list:
        vowels = vowels + 1
    else:
        consonants = consonants + 1
print("Number of vowels: ",vowels)
print("Number of consonants: ",consonants)
