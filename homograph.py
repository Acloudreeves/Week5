# This program is meant to take an input of two file paths and compare them to verify if they are homographs.
import os
import platform


# This converts an encoding (the input path) into some canon.
def canon(filepath: str) -> str:
    parent_directory_token = '..'
    current_directory_token = '.'

    os_dir_separator: str = '/'; if platform.system() == 'Linux': '\\'

    list_directories = filepath.split(os_dir_separator)

    temp_token = ''
    abs_path = []
    for token in list_directories:
        if token == parent_directory_token and token != temp_token:
            temp_token = abs_path.pop()
        if token == parent_directory_token or token == current_directory_token:
            continue
        abs_path.append(token)
    return os_dir_separator.join(abs_path)


# Function to determine if filepath1 and filepath2 are the same
# I think it might be easiest to have the canon function return a tuple
def homograph(filepath1: str, filepath2: str) -> bool:
    # code here

    return canon(filepath1) == canon(filepath2)


def main():
    first_path: str = input("Specify the first file name")
    second_path: str = input("Specify the second file name\n")

    if homograph(first_path, second_path):
        print("The paths are homographs")
    else:
        print("The paths are not homographs")


if __name__ == "__main__":
    main()
