
#In this file, a function called largest_number which is
#used to find largest number in array is created.


def largest_number(array):

    if len(array) == 1:
      #Above, in line 8, when length of array is 1, the function will return the actual
      #largest number in array.""
        return array[0]
    
    if array[0] <= array[-1]: #Here, comparing first element of array with last element of array.
        return largest_number(array[1:])
       #If condition in line 13 is true, then first element of array is removed,
       #to do this got subarray of array which is array[1:].
    else: #If condition in line 13 is not true, then removing last
          #element of array.
        array.pop()
        return largest_number(array)
    # In line 20, largest_number function calls itself.


# Below, the function largest_number is being tested with two arrays.
print(largest_number([1, 4, 3]))

print(largest_number([-1, 0, -4, 0]))


