

#======================
# Author: Susmita Datta
# Title:  insertionSort
#
# Time Complexity of Solution:
# O(n^2)
#
# Sample input =  [3, 2, 1, 4, 5, 6, 9, 8, 7]
# Sample output = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
#--------------------------------------------


def insertionSort(unsorted):

  for index in range(1, len(unsorted)):

    current_value = unsorted[index]
    position = index

    while position>0 and unsorted[position-1]>current_value:
      unsorted[position]=unsorted[position-1]
      position = position-1
      unsorted[position]=current_value

  return unsorted



if __name__ =="__main__":

	import random

	unsorted_list = random.sample(range(101), 11)

	print(unsorted_list)

	sorted_list = insertionSort(unsorted_list)

	print(sorted_list)