array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
  if len(array) <= 1:
    return array
  
  pivot = array[0]
  tail = array[1:]
  
  left_side = []
  right_side = []
  for x in tail:
    if x <= pivot:
      left_side.append(x)
    else:
      right_side.append(x)
  
  return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))