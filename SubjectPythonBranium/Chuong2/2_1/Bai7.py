import  math
a_str, b_str, c_str = input().split()
a = int(a_str)
b = int(b_str)
c = int(c_str)
#giai pt bac 1
if a == 0:
    if b == 0 and c == 0:
        print("COUNTERLESS SOLUTION")
    elif b == 0 and c != 0:
        print("NO SOLUTION")
    else:
        print(-c / b)
if a != 0: #giai pt bac 2
    delta = b * b - 4 * a * c
    if delta < 0:
        print("NO SOLUTION")
    elif delta == 0:
        print(-b / (2 * a))
    else:
        print(f"{(-b - math.sqrt(delta)) / (2 * a)} {(-b + math.sqrt(delta)) / (2 * a)}")
