import math

def my_sd_function(numbers):
    '自訂的標準差函數，請輸入一個數列'
    N = len(numbers)
    summation = 0
    another_summation = 0
    for number in numbers:
        summation = summation + number
    mu = summation / N
    
    for number in numbers:
        another_summation = another_summation + (number - mu)**2
    return math.sqrt(another_summation / N)

#call list
my_list = range(1, 6)
print(my_sd_function(my_list))