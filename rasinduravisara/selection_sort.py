# Python program for implementation of Selection
# Sort
import sys
A = input("Enter the numbers you want to sort with commas. : ")
A = A.split(",")
A = [eval(i) for i in A]

# Traverse through all array elements
for i in range(len(A)):
	
	# Find the minimum element in remaining 
	# unsorted array
	min_idx = i
	for j in range(i+1, len(A)):
		if A[min_idx] > A[j]:
			min_idx = j
			
	# Swap the found minimum element with 
	# the first element	 
	A[i], A[min_idx] = A[min_idx], A[i]

# Driver code to test above
print ("Sorted array")
for i in range(len(A)):
	print("%d" %A[i],end=" , ") 
