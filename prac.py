

def more_vowels(s, vowels=0):
    
    if len(s) == 0:
        return vowels
    
    def isvowel(char:str):
        return True if char.lower() in 'aeiou' else False
    
    if isvowel(s[0]):
        vowels += 1
    
    return more_vowels(s[1:], vowels)
        

    

    
 



z= more_vowels('Hello, world!')

# print(z)

def isVowelsMore(string):
    vowels = {'a', 'e', 'i', 'o', 'u'}

    def recursiveVowels(string, index=0):
        vowels_count = 0

        if index >= len(string):
            return vowels_count

        if string[index] in vowels:
            vowels_count += 1

        return vowels_count + recursiveVowels(string, index + 1)

    vowels = recursiveVowels(string)

    return len(string) / 2 < vowels


def eee(words):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowels_count = 0
    
    if len(words) == 0:
        return 0
    
    if words[0] in vowels:
        vowels_count += 1
        return vowels_count + eee(words[1:])
    else:
        return eee(words[1:])
    



def even_before_odd(num, index=0):

   

    num_list = list(str(num))

    if index >= len(num_list):
        return int(''.join(map(str, num_list)))

    curr_num = int(num_list[index])

    if curr_num % 2 == 0:
        # num_list[index], num_list[-1] = num_list[-1], num_list[index]
        pop_item = num_list.pop(index)
        num_list.insert(0, pop_item)
    
    int_convert = int(''.join(map(str, num_list)))
    return even_before_odd(int_convert, index = index + 1)
       

    


# r = even_before_odd(9922923)

# print(r)


def rearrange_even_odd(arr, start=0, end=None):
    if end is None:
        end = len(arr) - 1

    if start >= end:
        return arr

    if arr[start] % 2 != 0 and arr[end] % 2 == 0:
        arr[start], arr[end] = arr[end], arr[start]

    if arr[start] % 2 == 0:
        return rearrange_even_odd(arr, start + 1, end)

    if arr[end] % 2 != 0:
        return rearrange_even_odd(arr, start, end - 1)

    return rearrange_even_odd(arr, start + 1, end - 1)

# Example usage:
# sequence = [3, 2, 4, 1, 5, 6, 7, 8, 9]
sequence = [1,2,3,4,5,6]
# rearranged_sequence = rearrange_even_odd(sequence)
# print(rearranged_sequence)

def sorting(S, k, index=0):

    # less or equal to k before k
    if index >= len(S):
        return S
    
    curr = S[index]

    if curr > k and S[-1] <= k:
        S[index], S[-1] = S[-1], S[index]

    if curr <= k:
        return sorting(S, k, index = index + 1)
    else:
        return




   
    


# t  = sorting([4,5,2,1], 3)

# print(t)

def rearrange_less_than_k(S, k):
    if len(S) == 0:
        return []

    pivot = S[0]
    less_than_k = [x for x in S[1:] if x <= k]
    greater_than_k = [x for x in S[1:] if x > k]

    return rearrange_less_than_k(less_than_k, k) + [pivot] + rearrange_less_than_k(greater_than_k, k)

# Example usage:
# S = [4, 6, 2, 7, 1, 8, 3]
# k = 5
# rearranged_S = rearrange_less_than_k(S, k)
# print(rearranged_S)

def power(base, exponent):

    result = 1
    while exponent > 0:
        if exponent % 2 == 1: # odd
            result *= base
        base *=  base
        exponent //= 2
    return result

    
    # output = m
    # i = x
    # while i > 1:
    #     output = output * m
    #     i -= 1
    # return output



w = power(3,5)

print(w)
print(pow(3,5))



