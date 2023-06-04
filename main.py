from methods.gameplay import prepare_ratings_file, gameplay
from methods.generic_methods import get_input_options


if __name__ == '__main__':
    file_name = 'rating.txt'
    rating_file = prepare_ratings_file(file_name)
    user_input_game_options = get_input_options()
    gameplay(user_input_game_options, rating_file)
