ar = [64, 34, 25, 12, 22, 11, 90]
for i in range(len(ar)):
    for j in range(0, len(ar)-i-1):
        if ar[j] > ar[j+1]:
            ar[j], ar[j+1] = ar[j+1], ar[j]

print("Sorted array:", ar)
