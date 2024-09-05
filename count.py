def counting_sort(arr):
    if not arr:
        return arr
    min_val = min(arr)
    max_val = max(arr)
    count = [0] * (max_val - min_val + 1)
    for num in arr:
        count[num - min_val] += 1
    sorted_arr = []
    for i, cnt in enumerate(count):
        sorted_arr.extend([i + min_val] * cnt)

    return sorted_arr
arr = list(map(int,input("enter array").split() ))
sorted_arr = counting_sort(arr)
print("Sorted array:", sorted_arr)