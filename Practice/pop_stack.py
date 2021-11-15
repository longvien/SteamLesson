def pop(stack):
    ans = []
    if not stack:
        return ans
    else:
        for index in range(0,len(stack)-1):
            ans.append(stack[index])
    return ans
        