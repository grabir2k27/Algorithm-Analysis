arr = list(map(int, input("Enter elements: ").split()))
key = int(input("Enter key to search: "))

# 
# found = -1
# for i in range(len(arr)):
    # if arr[i] == key:
        # found = i
        # break

# print("Linear Search Index:", found)

# Binary 
arr.sort()
low, high = 0, len(arr) - 1
found = -1

while low <= high:
    mid = (low + high) // 2
    if arr[mid] == key:
        found = mid
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

print("Binary Search Index:", found)
               
