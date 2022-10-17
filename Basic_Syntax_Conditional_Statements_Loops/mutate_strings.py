string_one = input()
string_two = input()
last_printed = string_one
for character in range(len(string_one)):
    left_side = string_two[:character + 1]
    right_side = string_one[character + 1:]
    current_string = left_side + right_side
    if current_string == last_printed:
        continue
    print(current_string)
    last_printed = current_string

# за лявата страна взимаме всички букви от втория стринг до символа на който се намираме # [0:character + 1:1]
# за дясната взимаме от първия от символа на който сме # [character + 1:len(string_one):1]
# : - oбозначават началото на стринга ако са в началото, до края - ако са в края
# ::-1 - едните : са за началото, другите за края и -1 е стъпката
