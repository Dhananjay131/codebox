#!usr/bin/python3

def quicksort(A):
	quicksort2(A, 0, len(A)-1)

def quicksort2(A, low, hi):
	if low < hi:
		p = partition(A, low, hi)
		quicksort2(A, low, p-1)
		quicksort2(A, p+1, hi)

def get_pivot(A, low, hi):
	mid = (hi+low) //2
	pivot = hi
	if A[low] < A[mid]:
		if A[mid] < A[hi]:
			pivot = mid

	elif A[low] < A[hi]:
		pivot = low

	return pivot

def partition(A, low, hi):
	pivotindex = get_pivot(A, low, hi)
	pivotvalue = A[pivotindex]

	A[pivotindex], A[low] = A[low], A[pivotindex]
	border = low

	for i in range(low, hi+1):
		if A[i]<pivotvalue:
			border += 1
			A[i], A[border] = A[border], A[i]
	A[low], A[border] = A[border], A[low]	

	return (border)

A = [16, 18, 56, 27, 93, 0]
quicksort(A)
print A

