# with open('passwords.txt') as file:
#     lines = file.readlines()
#     lines = [n.strip() for n in lines]

# correctPasswords = 0
# for a in lines:
#     ss = a.split(' ', 2)
#     numbers = ss[0].split('-', 2)
#     letter = ss[1].replace(':', '')
#     password = ss[2]
#     occurrences = password.count(letter)
#     if occurrences >= int(numbers[0]) and occurrences <= int(numbers[1]): 
#          correctPasswords += 1
         
# print(correctPasswords)



# part 2


with open('passwords.txt') as file:
    lines = file.readlines()
    lines = [n.strip() for n in lines]

correctPasswords = 0
for a in lines:
    ss = a.split(' ', 2)
    numbers = ss[0].split('-', 2)
    letter = ss[1].replace(':', '')
    password = ss[2]
    occurrences = password.count(letter)
    n1 = int(numbers[0]) - 1
    n2 = int(numbers[1]) - 1

    if password[n1] == letter and password[n2] != letter or password[n1] != letter and password[n2] == letter:
                correctPasswords += 1

print(correctPasswords)
         









    



