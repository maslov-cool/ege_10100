with open('17_10100.txt') as f:
    A = [int(i) for i in f]
    max_13 = 0
    for i in sorted(A)[::-1]:
        if str(i)[-2:] == '13' and i > max_13:
            max_13 = i
            break
    B = []
    for i in range(len(A) - 2):
        if ((len(str(A[i])) == 3 and len(str(A[i + 1])) == 3 and len(str(A[i + 2])) != 3)
            or (len(str(A[i])) == 3 and len(str(A[i + 2])) == 3 and len(str(A[i + 1])) != 3)
            or (len(str(A[i + 1])) == 3 and len(str(A[i + 2])) == 3) and len(str(A[i])) != 3)\
                and A[i] + A[i + 1] + A[i + 2] <= max_13:
            B.append(A[i] + A[i + 1] + A[i + 2])
    print(len(B), max(B))





















