def pyramind(rows):

    for i in range(0, rows + 1):
        for j in range(i, rows + 1):
            print("-", end= "-")
        
        for j in range(1, i+ 1):
            print(j , end="-")

        for j in range(i-1, 0, -1):
            print(j, end="-")
        print()



# def twoSum( nums, target):
#     """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#     """
#     output = []

#     for k in range(len(nums)):
#         curr = nums[k] # 2
#         next = k + 1
#         while next < len(nums) and curr + nums[next] != target:
#             next += 1
#         if next > len(nums) -1:
#             continue
#         elif curr + nums[next] == target:
#             output.extend([k, next])
#             break
        
#     return output


def twoSum( nums, target):
    seen = {}

    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in seen.keys():
            return [seen[diff], i]
        else:
            seen[nums[i]] = i
    return seen

def removeElement(nums, val):
    k = 0

    for x in nums:
        if x != val:
            nums[k] = x
            k += 1
   
    
    return k

def isvalid(s):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        temp = []
        opening = "([{"
        closing = ")]}"
        for bracket in s:
            if bracket in opening:
                temp.append(bracket)
            elif bracket in closing:
                if len(temp) > 0:
                    last = temp.pop()
                else:
                    return False
                                
                if opening.index(last) != closing.index(bracket):
                    return False
                    
        print(temp)
        
        return not temp
            



# e = isvalid("[]")
# print(e)

def longestCommonPrefix(strs):
    
    if not strs:
        return ""
    prefix = strs[0]

    for word in strs[1:]:
        while word.find(prefix) != 0:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix
    
    

    
# tt = longestCommonPrefix(["flower","flow","flight"])
# print(tt)
# print('sss')

def romanToInt( s,):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        sum = 0
        hv = 0
        for i in reversed(s):
            addition =roman_dict[i]
            if addition<hv :
                sum -= addition
            else:
                sum += addition
                hv=addition
        return sum


def lengthOfLastWord(s):
    # e = s.rstrip()

    r = s.split(" ")
    print(r)
    
    r = 'ss '.isalpha()
    print(r)
    
    
    # last_index = len(e) -1
    # while e[last_index] != ' ':
    #     last_index -= 1
    #     if last_index < 0:
    #         return len(e)
    
    # return len(e[last_index + 1:])


    


def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    # if not digits: return []
    # result =  int(''.join(map(str, digits))) + 1

    # digits = [int(i) for i in str(result)]
    # return digits

    l=len(digits)
    ans=""
    for i in range(0,l):
        ans=ans+(str(digits[i]))
    print(ans)
    # x=int(ans)
    # x=x+1
    # st=str(x)
    # li=[]
    # for i in st:
    #     li.append(int(i))
    # return li
    
    



largeNum = [9,9]
print(plusOne(largeNum))

print("This is test branch")
print("This is main branch")
    






  


    

