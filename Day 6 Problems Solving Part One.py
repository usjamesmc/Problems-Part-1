def print_team(my_team):
    for number in range(0, 7, 6):
        print(my_team[number])
print_team('Packers')

def print_divisibility(start_number, stop_number, step_number):
    for number in range(start_number, stop_number, step_number):
        if number % 3 == 0:
            print('peanut butter')
        elif number % 5 == 0:
            print('jelly')
        elif number % 3 == 0 and number % 5 ==0:
            print('peanut butter jelly')
        else:
            print(number)
print_divisibility(0, 101, 1)

def jumble_word(word):
    final_result = ''
    for number in range(0, 7, 1):
        if word == 'Monitor':
            final_result = word[number]
            print(final_result)
            print(number)
        else:print('yes')
jumble_word('Monitor')

def search_ingredients(ingredients_list):
    user_input = input('Which ingredient would you like to search for?')
    if user_input == 'Salt':
        return 'Salt'
    elif user_input == 'Pepper':
        return 'Pepper'
    elif user_input == 'Paprika':
        return 'Paprika'
    elif user_input == 'Cumin':
        return 'Cumin'
    elif user_input == 'Oregano':
        return 'Oregano'
    else:
        user_input = input('Sorry, selection not available. Would you like to search for something else?')
        if user_input == 'yes':
            search_ingredients(['Salt', 'Pepper', 'Paprika', 'Cumin', 'Oregano'])
        else:
            print('Goodbye')
search_ingredients(['Salt', 'Pepper', 'Paprika', 'Cumin', 'Oregano'])

def reverse_index(reverse_list):
    new_list = ''
    new_list = (reverse_list[3], reverse_list[2], reverse_list[1], reverse_list[0])
    return(new_list)
reverse_index(['one', 'two', 'three', 'four'])

def names_list(names):  
    new_list = names
    a = len(names[0])
    b = len(names[1])
    c = len(names[2])
    d = len(names[3])
    e = len(names[4])
    f = len(names[5])
    if (int(a)) < 5:
        names.remove('Sarah')
    if (int(b)) < 5:
        names.remove('Tom')
    if (int(c)) < 5:
        names.remove('Jessica')
    if (int(d)) < 5:
        names.remove('Bobby')
    if (int(e)) < 5:
        names.remove('Andy')
    if (int(f)) < 5:
        names.remove('Terry')
    return new_list
new_list = names_list(['Sarah', 'Tom', 'Jessica', 'Bobby', 'Andy', 'Terry'])
