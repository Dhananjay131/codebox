#!usr/bin/python3

arr = [1,4,6,4]

def mergefunc(arr, length):
	
	low = 0
	high = length-1
	mid= (low + high)/2
	if(low < mid):
		mergesort(arr,low, mid)
	elif(mid+1 < high):
 		mergesort(arr, mid+1, high)
	return mid

def mergesort(arr, low, high):
	if(arr[low] < arr[high]:
		low+=1
	else:
		temp = arr[low]
		arr[low] = arr[high]
		arr[high] = temp


mergefunc(arr, i, j))

