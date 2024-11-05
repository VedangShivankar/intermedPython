def get_squared_numbers(numbers):
    squared_numbers = []
    for n in numbers:
        squared_numbers.append(n*n)
    return squared_numbers
numbers = [2, 5, 8, 9]

print(get_squared_numbers(numbers))

#seciton 2

def find_first_pe(prices, eps, index):
    pe = prices[index]/eps[index]
    return(pe)

#section 3

list1ofnums = [3, 6, 2, 4, 3, 6, 8, 9]
for i in range(len(list1ofnums)):
    for j in range(i+1, len(list1ofnums)):
        if list1ofnums[i] == list1ofnums[j]:
            print(list1ofnums[i], "is duplicate")
            break

#section 4

list2ofnums =  [3, 6, 2, 4, 3, 6, 8, 9]
duplicate = None
for i in range(len(list2ofnums)):
    for j in range(i+1, len(list2ofnums)):
        if list1ofnums[i] == list1ofnums[j]:
            duplicate =numbers[i]
            break

for i in range(len(list2ofnums)):
    if numbers[i] == duplicate:
        print[i]