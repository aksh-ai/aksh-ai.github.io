

w, b = 0, 0

a = [17, 28, 30]
b = [99, 16, 8]

for i in range(3):
    if a[i] > b[i]:
        w = w + 1
    elif a[i] < b[i]:
        b = b + 1

# result = compareTriplets(a, b)
print(w, b)