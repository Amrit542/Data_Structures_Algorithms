def binary_search(data, target, low, high):

    if low > high: return False
    else:
        mid =  (low + high) // 2 # truncate the value
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)
        


e = binary_search([3,5,7,9,11,24,56], 11, 0, 7)
print(e)

def reverse(S, start, stop):
    if start < stop -1:
        S[start], S[stop -1] = S[stop -1], S[start]
        reverse(S, start + 1, stop - 1)

