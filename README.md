Imagine that the most of the functions that we have been using to process lists in Python do not exist. For the problems below you are not allowed to use any list methods (append, remove, insert, etc) or certain core Python functions specified in each problem. You may, however, use your own custom-written functions to solve these problems (i.e. if you find that your listlen() function would be useful in writing another function you are welcome to use it). Given these restrictions, write a series of functions that do the following:

1. Write a new function called "listlen" based on the following IPO:
# function:    listlen
# INPUT:       a list
# PROCESSING:  determines the size of the list
# OUTPUT:      an integer representing the size of the list
Note that you cannot use the "len" function in your program. If the list is empty your function should return a value of 0.

2. Write a new function called "listmax" based on the following IPO
# function:    listmax
# INPUT:       a list
# PROCESSING:  obtains the largest element in the list
# OUTPUT:      returns the largest element in the list
Make sure that you DO NOT use the "max" function in your program. You cannot assume that the list supplied will be non-empty - if this is the case your function should return the value None. You can assume that the supplied list contains data elements of the same type (i.e. the list will contain all strings, or all ints, or all floats, or all Boolean values). The original list should NOT be changed after you call the 'listmax' function (and sorting the list will cause the list to change).

3. Write a new function called "listcopy" based on the following IPO
# function:    listcopy
# INPUT:       a list
# PROCESSING:  creates a new list which serves as a copy of the supplied list
# OUTPUT:      returns a new copy of the list
Make sure that you DO NOT use anyt list methods, including "append", "insert" or "copy". You cannot assume that the list supplied will be non-empty - if this is the case your function should return an empty list.

4. Write a new function called "listappend" based on the following IPO
# function:    listappend
# INPUT:       a list and an element to add to the list (any data type)
# PROCESSING:  creates a new list which includes the new element appended
#              to the end of the list
# OUTPUT:      returns a new copy of the list
Make sure that you DO NOT use any list methods such as "append" in your program. Note that your original list should not change when you run this function.

5. Write a new function called "listinsert" based on the following IPO
# function:    listinsert
# INPUT:       a list, a location (integer) and a data 
#              element (can be a string, float, Boolean or 
#              int)
# PROCESSING:  inserts the supplied data element into the 
#              list at the desired location
# OUTPUT:      return a new copy of the list that contains
#              the inserted element
Make sure that you DO NOT use any list methods, such as the "insert" or "append" methods, in your program. Note that your original list should not change when you run this function.

6. Write a new function called "listremove" based on the following IPO
# function:    listremove
# INPUT:       a list and a data element (can be a string, 
#              float, Boolean or int)
# PROCESSING:  removes all occurrences of the supplied 
#              data element from the list.  You can assume 
#              that the data element is present in the list 
#              somewhere.
# OUTPUT:      return a new copy of the list with the
#              desired element removed
Make sure that you DO NOT use any list methods, such as the "remove" method, or the "del" command in your program. Note that your original list should not change when you run this function.

7. Write a new function called "listreverse" based on the following IPO
# function:    listreverse
# INPUT:       a list
# PROCESSING:  creates a copy of the supplied list that
#              contains the same elements as the original
#              list, but in reverse order
# OUTPUT:      return a new copy of the list in reverse order
Make sure that you DO NOT use any list methods such as "reverse" your program. Note that your original list should not change when you run this function.
