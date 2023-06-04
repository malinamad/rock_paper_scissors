from classes import UserRatingFile as UsrRtFile, RockPaperScissors as RckPprSc


def prepare_ratings_file(file_name):
    file_class = UsrRtFile.UserRatingFile(file_name)
    file_class.greetings()

    if file_class.check_whether_file_exists() is False:
        if file_class.check_whether_name_is_in_ratings() is False:
            file_class.add_name_to_rating()
    return file_class


def gameplay(input_options, rating_file):
    while True:
        usr_selected_option = input()
        if usr_selected_option in input_options:
            game_inst = RckPprSc.RockPaperScissors(usr_selected_option, input_options)
            score = game_inst.compare_choices()
            if score:
                cur_score = rating_file.get_rating_value()
                add_val_to_score = score + int(cur_score)
                rating_file.overwrite_user_rating(str(add_val_to_score))
        elif usr_selected_option == '!exit':
            print('Bye!')
            break
        elif usr_selected_option == '!rating':
            rating_file.print_user_rating()
        else:
            print('Invalid input')
