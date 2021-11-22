def get_even(array):
   ans = []
   for number in array: 
       if number%2 == 0:
           ans.append(number)
   return ans