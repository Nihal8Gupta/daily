def merge(arr:list)->list:
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge(arr[:mid])
    right = merge(arr[mid:])
    return merging(left,right)

def merging(left,right):
    i = j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
    

arr = [3,1,6,8,3,0,2,7]
print(merge(arr))