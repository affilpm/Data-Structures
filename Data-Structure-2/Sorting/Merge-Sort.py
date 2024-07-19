def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left,right)

def merge(left,right):
    sorted_arr = []
    i = j = 0
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[i]) 
            j += 1  
            
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr         

arr = [38, 27, 43, 3, 9, 82, 10]
print("Sorted array:", merge_sort(arr))
    