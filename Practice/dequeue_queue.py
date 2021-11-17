def dequeue(queue):
    ans = []
    if not queue:
        return ans
    for index in range(1,len(queue)):
        ans.append(queue[index])
    return ans         