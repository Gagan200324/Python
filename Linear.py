arr = [10, 20, 30, 40, 50]
target = int(input("Enter the number to search: "))
for i in range(len(arr)):
    if arr[i] == target:
        found = True
        print("Element found at index", i)
        break
    else:
        print("Element not found")
