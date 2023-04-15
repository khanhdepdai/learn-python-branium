grade = float(input("Enter grade: "))
if grade >= 9.0:
    print("A")
elif grade >= 7 and grade < 9:
    print("B")
elif grade >= 5 and grade < 7:
    print("C")
elif grade >= 4 and grade < 5:
    print("D")
elif grade < 4:
    print("F")