def input_sets():
    sets = []
    n = int(input("Enter n: "))
    for i in range(n):
        sets.insert(i,input("Enter string: "))
    return sets


def Upper_first_str(s):
    t = ""
    for i in range(len(s)):
        if i == 0 or s[i - 1] == " " or s[i - 1] == "." or s[i - 1] == "?" or s[i - 1] == "!":
            t += s[i].upper()
        elif i != 0 and s[i - 1] != " " and s[i - 1] != "." and s[i - 1] != "?" and s[i - 1] != "!":
            t += s[i]
    return t


sets = input_sets()
for i in range(len(sets)):
    print(f"Test {i + 1}: ")
    print(Upper_first_str(sets[i]))


