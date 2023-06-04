from random import choice


class RockPaperScissors:
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
        lose_options, win_options = self.work_with_selected_game_option_based_on_its_index(
            elem_index, div_elem_amount)
        return lose_options, win_options

    def work_with_selected_game_option_based_on_its_index(self, element_index, half_elements_amount):
        if element_index >= half_elements_amount:
            win_elements = [x for x in self.options_list]
            lose_elements = []
            win_options, lose_options = self.modify_lists_with_win_lose_options_on_other_half(
                lose_elements, win_elements, element_index, half_elements_amount)
            return lose_options, win_options
        elif element_index <= half_elements_amount:
            win_elements = []
            lose_elements = [x for x in self.options_list]
            lose_options, win_options = self.modify_lists_with_win_lose_options_on_first_half(
                win_elements, lose_elements, element_index, half_elements_amount)
            return lose_options, win_options

    def modify_lists_with_win_lose_options_on_first_half(
            self, first_list, second_list, elem_index, half_elem_am):
        end_index = half_elem_am + elem_index + 1
        for el in self.options_list[elem_index + 1:int(end_index)]:
            first_list.append(el)
            second_list.remove(el)
        second_list.remove(self.game_option)
        return first_list, second_list

    def modify_lists_with_win_lose_options_on_other_half(
            self, first_list, second_list, elem_index, half_elem_am):
        start_index = elem_index - half_elem_am
        for el in self.options_list[int(start_index):elem_index]:
            first_list.append(el)
            second_list.remove(el)
        second_list.remove(self.game_option)
        return first_list, second_list
