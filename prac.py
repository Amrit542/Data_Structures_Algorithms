

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


def even_before_odd(num, output=[]):

    if not num:
        return 
    list_num = list(str(num))

    first_digit = int(list_num[0])
    
    if first_digit % 2 == 0:
        output.append(first_digit)
    else:
        output.insert(0, first_digit)
    
    w = even_before_odd(int(''.join(list_num[1:])))
    return int(w)



r = even_before_odd(123456)

print(r)



