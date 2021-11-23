def reverse_array(array):
    ans = []
    n = len(array)
    counter = n - 1
    while counter >= 0:
        ans.append(array[counter]) 
        counter = counter - 1
    return ans    