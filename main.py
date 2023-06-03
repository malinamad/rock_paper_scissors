from random import choice


class RockPaperScissors:
    lose_elements = []
    win_elements = []

    def __init__(self, game_option, options_list):
        self.game_option = game_option
        self.options_list = options_list

    def compare_choices(self):
        computer_random_choice = self.computer_choice()
        return self.choices_comparison(computer_random_choice)

    def computer_choice(self):
        return choice(self.options_list)

    def choices_comparison(self, comp_choice):
        lose_options, win_options = self.get_list_of_elements()
        if self.game_option == comp_choice:
            print(f'There is a draw ({self.game_option})')
            return 50
        elif comp_choice in lose_options:
            print(f'Well done. The computer chose {comp_choice} and failed')
            return 100
        elif comp_choice in win_options:
            print(f'Sorry, but the computer chose {comp_choice}')
            return 0

    def get_list_of_elements(self):
        elem_index = self.options_list.index(self.game_option)
        div_elem_amount = (len(self.options_list) - 1) / 2

        win_elements = []
        lose_elements = []
        if elem_index >= div_elem_amount:
            start_index = elem_index - div_elem_amount
            win_elements = [x for x in self.options_list]
            for el in self.options_list[int(start_index):elem_index]:
                lose_elements.append(el)
                win_elements.remove(el)
            win_elements.remove(self.game_option)
            return lose_elements, win_elements

        elif elem_index <= div_elem_amount:
            end_index = div_elem_amount + elem_index + 1
            lose_elements = [x for x in self.options_list]
            for el in self.options_list[elem_index + 1:int(end_index)]:
                win_elements.append(el)
                lose_elements.remove(el)
            lose_elements.remove(self.game_option)
            return lose_elements, win_elements

def greetings(name):
    print(f'Hello, {name}')


def get_user_name():
    str_msg = 'Enter your name: '
    return input(str_msg)


def check_whether_name_is_in_ratings(name, file_path):
    with open(file_path, 'r+') as f:
        for line in f:
            if name in line:
                return True
        return False


def add_name_to_rating(name, file_path):
    with open(file_path, 'a') as f:
        print(name + ' 0', file=f)


def get_rating_value(user, file_path):
    with open(file_path, 'r+') as f:
        for line in f:
            if user in line:
                return line[len(user) + 1:]


def print_user_rating(user, file):
    with open(file, 'r+') as f:
        for line in f:
            if user in line:
                score = get_rating_value(user, file)
                print('Your rating: ' + score)
                break


def update_user_rating(user, file_path, score):
    with open(file_path, 'r+') as f:
        for line in f:
            if user in line:
                f.write(line.replace(line[len(user) + 1:], score))


def overwrite_user_rating(user, new_rating, file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    for i in range(len(lines)):
        if user in lines[i]:
            lines[i] = user + ' ' + new_rating + '\n'
    with open(file_path, 'w') as f:
        f.writelines(lines)

user_name = get_user_name()

greetings(user_name)

rating_file_path = 'rating.txt'
response = check_whether_name_is_in_ratings(user_name, rating_file_path)
if response is not True:
    add_name_to_rating(user_name, rating_file_path)

input_options = input()
if len(input_options) == 0:
    input_options = 'scissors,rock,paper'

input_options = input_options.split(',')

print("Okay, let's start")
while True:
    usr_input = input()
    if usr_input in input_options:
        inst = RockPaperScissors(usr_input, input_options)
        score = inst.compare_choices()
        if score:
            cur_score = get_rating_value(user_name, rating_file_path)
            add_val_to_score = score + int(cur_score)
            overwrite_user_rating(user_name, str(add_val_to_score), rating_file_path)
    elif usr_input == '!exit':
        print('Bye!')
        break
    elif usr_input == '!rating':
        print_user_rating(user_name, rating_file_path)
    else:
        print('Invalid input')
