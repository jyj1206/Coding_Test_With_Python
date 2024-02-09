array = [7, 5, 9, 0, 3, 1, 2, 9, 1, 4, 8, 0, 5, 2]

def merge(left, right):
  i, j = 0, 0
  merged_array = []
  
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      merged_array.append(left[i])
      i += 1
    else:
      merged_array.append(right[j])
      j += 1
  merged_array += left[i:]
  merged_array += right[j:]
  return merged_array

def merge_sort(array):
  if len(array) <= 1:
    return array
  
  mid = len(array)//2
  left = merge_sort(array[:mid])
  right = merge_sort(array[mid:])
  
  return merge(left, right)

print(merge_sort(array))