def insertion_Sort(data):
    
    for k in range(1, len(data)):
        curr = data[k]

        j = k
        while j > 0 and data[j-1] > curr:
            data[j] = data[j-1]
            j -= 1
        data[j] = curr
    
    return data


data = [9, 5, 1, 4, 3]
insertion_Sort(data)
print('Sorted Array in Ascending Order:')
print(data)

# Pyramid Shape

def pyramind(rows):

    for i in range(0, rows + 1):
        for j in range(i, rows + 1):
            print("-", end= "-")
        
        for j in range(1, i+ 1):
            print(j , end="-")

        for j in range(i-1, 0, -1):
            print(j, end="-")
        print()



e = pyramind(4)
print(e)