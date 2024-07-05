
#In this file, the function called "adding_up_to" is created,
#this function takes in two inputs, the first input is an array and the second input
   #is any index of that array, then the function will add together all the elements in that array that have index values between (and including) 0 and
   #value of second input. For example, adding_up_to([1,2,3,4], 2) will give 6, and 6 is sum of elements in [1,2,3,4] that have
   #index values between (and including) 0 and 2. 


def adding_up_to(array, index):
   """This function takes in two inputs, the first input is an array and the second input is any index of that array,
      then the function will add together all elements in that array that have index values between (and including) 0 and
      value of the second input. For example, adding_up_to([1,2,3,4], 2) will give 6, and 6 is sum of elements in [1,2,3,4] that have
      index values between (and including) 0 and 2."""
   if index < 0: # Here, this is the base case.
      """In line 13, when index value becomes equal to -1, the function will stop calling itself,
         to do this we tell the function to give zero as an output (this is shown in line 19,
         note that this is not the final output of the function), this will not affect the final output of the
         function because we are telling the function to add elements of array together, so adding zero to the total sum
         does nothing to the total sum.
           """
      return 0
   
   return array[index] + adding_up_to(array, index - 1) # Here, this is the recursive statement.


# Using the function called adding_up_to, this is shown below:

print(adding_up_to([1, 4, 5, 3, 12, 16], 4))


print(adding_up_to([4, 3, 1, 5], 1))
