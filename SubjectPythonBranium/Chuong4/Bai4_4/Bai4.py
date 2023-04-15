str1 = input("Enter string 1: ").split()
str2 = input("Enter string 2: ").split()
common = set(str1).intersection(set(str2))
str3 = str1 + str2
result = []
for i in str3:
    if i in common:
        continue
    else:
        result.append(i)


print(result)
