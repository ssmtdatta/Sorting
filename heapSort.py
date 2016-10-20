import math


unsorted_arr = [9, 12, 6, 13, 25, 4, 15, 7, 1, 3, 19]
sorted_arr = []

def createHeaps(arr):

  heaps = []

  for i in range(0, len(arr)):
  	p_idx = i
  	p_val = arr[p_idx]

  	if (2*p_idx + 1) < len(arr):
  	  l_idx = 2*p_idx + 1
  	  l_val = arr[l_idx]
  	else:
  	  l_val = "void"

  	if (2*p_idx + 2) < len(arr):
  	  r_idx = 2*p_idx + 2	
  	  r_val = arr[r_idx] 
  	else: 
  	  r_val = "void"

  	if isinstance(l_val, int) and isinstance(r_val, int):
  	  heaps.append([p_val, l_val, r_val])
  	else:
  	  break  
	
  return heaps
	

def swapInTree(tree):
  if tree[0] < tree[1]:
  	tmp = tree[0] 
  	tree[0] = tree[1]
  	tree[1] = tmp
  
  if tree[0] < tree[2]:
  	tmp = tree[0] 
  	tree[0] = tree[2]
  	tree[2] = tmp
  return tree


  