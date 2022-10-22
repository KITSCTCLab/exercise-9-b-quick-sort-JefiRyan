from typing import List

def quick_sort(data, low, high) -> List[int]:
    if low<high:
        j = partition(data,low,high)
        quick_sort(data,low,j-1)
        quick_sort(data,j+1,high)
    return data

def partition(data, low, high):
    i = low
    j = high
    pivot = data[i]
    while i<j:
        while i+1 <= high and data[i] <= pivot:
            i+=1
        while j-1 >= low and data[j] > pivot:
            j-=1
        if i<j:
            data[i],data[j] = data[j],data[i]
    data[low],data[j] = data[j],data[low]
    return j


input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(quick_sort(data, 0, len(data)-1))
