def catTuples(list_of_tuples):
    concatenated_tuple = ()
    for tpl in list_of_tuples:
        concatenated_tuple += tpl
    return concatenated_tuple

# Example usage:
list_of_tuples = [(1, 2), ('a', 'b'), (True, False)]
result = catTuples(list_of_tuples)
print(result)  # Output will be (1, 2, 'a', 'b', True, False)
