def R4(input_string):
    if len(input_string) >= 4:
        return input_string[:4][::-1]
    else:
        return "String is too short. It should have at least 4 characters."

# Example usage:
input_str = "Niranjan"
result = R4(input_str)
print(result)  
