def remove_extra_spaces(input_string):
    output_string = ""
    prev_char = ""

    for char in input_string:
        if char != " " or prev_char != " ":
            output_string += char
        prev_char = char

    return output_string

input_string = input("Enter a string (length <= 1000): ")

result = remove_extra_spaces(input_string)
print("Modified string with consecutive spaces removed:")
print(result)
