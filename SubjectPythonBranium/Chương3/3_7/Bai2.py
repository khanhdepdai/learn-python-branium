s = input("Enter string: ")
consonant = 0
vowel = 0
for i in range(len(s)):
    if s[i] < "z" and s[i] > "A":
        if s[i] == 'e' or s[i] == 'u' or s[i] == 'o' or s[i] == 'a' or s[i] == 'i':
            consonant += 1
        else:
            vowel += 1


print(f"Consonant: {consonant}")
print(f"Vowel: {vowel}")
