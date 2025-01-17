arr = [10, 20, 30, 40, 50]
target = 30
low = 0
high = len(arr) - 1
found = False
while low <= high:
    mid = (low + high) // 2
    if arr[mid] == target:
        found = True
        print("Element found at index", mid)
        break
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
if not found:
    print("Element not found")
