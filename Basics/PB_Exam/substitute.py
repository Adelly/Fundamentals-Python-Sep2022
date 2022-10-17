K = int(input())
L = int(input())
M = int(input())
N = int(input())
for a in range(K, 9):
    changes = 0
    for b in range(9, L - 1, -1):
        for c in range(M, 9):
            for d in range(9, N - 1, -1):
                is_valid = a % 2 == 0 and b % 2 != 0 and c % 2 == 0 and d % 2 != 0
                if is_valid:
                    if f"{a}{b}" == f"{c}{d}":
                        print("Cannot change the same player.")
                    else:
                        print(f"{a}{b} - {c}{d}")
                        changes += 1
                    if changes >= 6:
                        break
            if changes >= 6:
                break
        if changes >= 6:
            break
    if changes >= 6:
        break







