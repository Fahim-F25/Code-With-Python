t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    neg = arr.count(-1)
    zero = arr.count(0)

    ops = zero  # each zero → 1 operation

    if neg % 2 == 1:
        if zero == 0:
            ops += 2  # need to flip one -1 → 1
        else:
            ops += 1  # need one extra op to fix parity using zero

    print(ops)
