#=======================
#  Author: Susmita Datta
#  Algorithm: Bubble Sort
#  Title: bubbleSort
#
# Time Complexity of Solution:
# Best O(n^2); Average O(n^2); Worst O(n^2).
# 
#  Sample Input:  [8,5,3,1,9,6,0,7,4,2,5]
#  Sample Output: [0,1,2,3,4,5,5,6,7,8,9]
#----------------------------------------



def bubbleSort(unsorted):

	sort_count = 0
	
	for k in range(0, len(unsorted)-1):

		num1 = unsorted[k]
		num2 = unsorted[k+1]

		if num1 > num2:
			unsorted[k+1] = num1
			unsorted[k] = num2
			sort_count += 1
		
	if sort_count != 0:
		return bubbleSort(unsorted)
	
	if sort_count == 0:
		return unsorted



if __name__ == "__main__":
	
	import random	
	
	unsorted_list = random.sample(range(99), 11) 
	print(" Unsorted list of numbers:\n",unsorted_list,'\n')

	sorted_list = bubbleSort(unsorted_list)
	print(" Sorted list:\n",sorted_list,"\n")



    


