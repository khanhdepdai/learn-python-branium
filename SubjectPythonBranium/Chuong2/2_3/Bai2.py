n = int(input("Enter the total number of test:"))
for i in range( 1, n + 1, 1):
    str_n,str_k = input(f"Enter n, k of test {i}:").split()
    n = int(str_n)
    k = int(str_k)
    if n < k:
        print("No result")
    else:
        for j in range(k, n + 1, 1):
            if j % 2 == 1:
                print(j, end=' ')
        print()