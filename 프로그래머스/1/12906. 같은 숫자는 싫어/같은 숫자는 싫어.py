def solution(arr):
    result = [arr[0]]
    
    for num in arr[1:]:
        if num != result[-1]:
            result.append(num)
            
    return result