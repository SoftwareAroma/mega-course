# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    highest_number = max(A)
    temp = []
    for item in range(1000):
        if item > 0 and item not in A:
            temp.append(item)
    
    if min(A) < 0:
        return 1
    else:
        return min(temp)
        