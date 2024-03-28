test_list = [5, 6, 3, "Gfg", 3, "is", 9, "best", 4]

print("The original list: " + str(test_list))

# Check if any string element is present in the list
string_present = any(isinstance(x, str) for x in test_list)
if string_present:
    print("String element is present in the list.")
else:
    print(" string element is  Not present  in the list.")

# Check if any integer element is present in the list
integer_present = any(isinstance(x, int) for x in test_list)
if integer_present:
    print("Integer element is present in the list.")
else:
    print("integer element is Not  present in the list.")

# Extract strings from the list
string_instances = [elem for elem in test_list if isinstance(elem, str)]
print("The string instances: " + str(string_instances))

# Extract integers from the list
integer_instances = [elem for elem in test_list if isinstance(elem, int)]
print("The integer instances: " + str(integer_instances))
