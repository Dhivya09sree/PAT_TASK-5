data = [10, 501, 22, 37, 100, 999, 87, 351]
result = filter(lambda x: x > 4, data)
# filters the elements of data using lambda function each element is greater than 4 
print(list(result))
