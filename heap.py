#In python language heap is created in min-heap manner only.
#To construct max-heap we have to multiply the values by -1 while inserting.
#To use heap methods we import methods from heapq.

from heapq import *
lst = [21, 1, 45, 78, 3, 5]
 
#creating min-heap
#method-1 [convert given list into heap].
heapify(lst)

#method-2 [take a new list and use heap methods].
min_heap = []
for element in lst:
    heappush(min_heap, element)

#creating max-heap
max_heap = []
for element in lst:
    heappush(max_heap, -element)
    
#insert an element
heappush(min_heap, 4)
 
#pop from heap
heappop(min_heap)
 
#replace top element of heap with some value k.
heapreplace(min_heap, 6)
