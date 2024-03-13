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
            



e = isvalid("[]")
print(e)

  


    

