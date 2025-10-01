# Input
n, m = map(int, input().split())
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

# Calculate happiness
happiness = 0
for x in arr:
    if x in A:
        happiness += 1
    elif x in B:
        happiness -= 1

print(happiness)
