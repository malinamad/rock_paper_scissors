from os import access, R_OK


class UserRatingFile:
    def __init__(self, file_path):
        self.file_path = file_path
        self.name = self.get_user_name()

    def greetings(self):
        print(f'Hello, {self.name}')

    def get_user_name(self):
        str_msg = 'Enter your name: '
        return input(str_msg)

    def check_whether_name_is_in_ratings(self):
        with open(self.file_path, 'r+') as f:
            for line in f:
                if self.name in line:
                    return True
            return False

    def add_name_to_rating(self):
        with open(self.file_path, 'a') as f:
            print(self.name + ' 0', file=f)

    def get_rating_value(self):
        with open(self.file_path, 'r+') as f:
            for line in f:
                if self.name in line:
                    return line[len(self.name) + 1:]

    def print_user_rating(self):
        with open(self.file_path, 'r+') as f:
            for line in f:
                if self.name in line:
                    rating = self.get_rating_value()
                    print('Your rating: ' + rating)
                    break

    def update_user_rating(self, rating):
        with open(self.file_path, 'r+') as f:
            for line in f:
                if self.name in line:
                    f.write(line.replace(line[len(self.name) + 1:], rating))

    def overwrite_user_rating(self, new_rating):
        with open(self.file_path, 'r') as f:
            lines = f.readlines()
        for i in range(len(lines)):
            if self.name in lines[i]:
                lines[i] = self.name + ' ' + new_rating + '\n'
        with open(self.file_path, 'w') as f:
            f.writelines(lines)

    def check_whether_file_exists(self):
        if access(self.file_path, R_OK) is not True:
            with open(self.file_path, 'w'):
                self.add_name_to_rating()
                return True
        return False
