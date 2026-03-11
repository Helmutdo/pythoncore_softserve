string = "abracadabra"
position = 5
character = "k"

# def mutate_string(string, position, character):
#     new = string.replace(string[position], character)
    
#     return  new

# result = mutate_string(string, position, character)
# print(result)

new_string = string[:position] + character + string[position+1:]
print(new_string)

