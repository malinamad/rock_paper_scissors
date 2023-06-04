def get_input_options():
    input_options = input()
    validated_input_options = input_options_validation(input_options)
    modified_input_options = validated_input_options.split(',')
    print("Okay, let's start")
    return modified_input_options


def input_options_validation(options):
    default_game_options = 'paper,rock,scissors'
    if len(options) == 0:
        options = default_game_options
    return options
