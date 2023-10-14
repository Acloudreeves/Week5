# This program takes an input of two file paths and compares them to verify if they are homographs or non-homographs.

import os
import platform

# This dictionary contains the test cases for homographs and non-homographs. True = Homograph, False = Non-Homograph
test_cases1 = [
    # Test Case Set 1: Non-homographs
    # Test 1
    # Scenario: On a Windows system, filepath1 is on the C: drive, while filepath2 specifies a different drive.
    {
        "name": "Test 1",
        "filepath1": "C:\\users\\cse453\\secret\\password.txt",
        "filepath2": "D:\\users\\cse453\\secret\\password.txt",
        "expected": False,
    },
    # Test 2
    # Scenario: On a Windows system, filepath1 uses "\" while filepath2 uses "/". Windows will accept either one, but does not treat them as equivalent.
    {
        "name": "Test 2",
        "filepath1": "C:\\users\\cse453\\secret\\password.txt",
        "filepath2": "C:/users/cse453/secret/password.txt",
        "expected": False,
    },
    # Test 3
    # Scenario: Filepath2 uses ./ to specify a current directory. On a Windows system, only .\ is valid.
    {
        "name": "Test 3",
        "filepath1": "/users/cse453/secret/password.txt",
        "filepath2": "/users/cse453/./secret/password.txt",
        "expected": False,
    },
    # Test 4
    # Scenario: Filepath2 uses ../ to specify a parent directory. On a Windows system, only ..\ is valid.
    {
        "name": "Test 4",
        "filepath1": "/users/cse453/secret/password.txt",
        "filepath2": "/users/cse453/secret/../secret/password.txt",
        "expected": False,
    },
    # Test 5
    # Scenario: Filepath2 uses ..\ to specify a parent directory incorrectly on a Windows system.
    {
        "name": "Test 5",
        "filepath1": "\\users\\cse453\\secret\\password.txt",
        "filepath2": "\\users\\cse453\\..\\password.txt",
        "expected": False,
    },
    # Test 6
    # Scenario: Filepath2 uses .\ to specify the current directory incorrectly on a Windows system.
    {
        "name": "Test 6",
        "filepath1": "\\users\\cse453\\secret\\password.txt",
        "filepath2": "\\users\\cse453\\.\\password.txt",
        "expected": False,
    },
    # Test 7
    # Scenario: Filepath2 has a different /cse453/ directory name in the path (Capital "S" instead of "5").
    {
        "name": "Test 7",
        "filepath1": "/users/cse453/secret/password.txt",
        "filepath2": "/users/cse4S3/secret/password.txt",
        "expected": False,
    },

    # Test 8
    # Scenario: Filepath2 includes a special character, #.
    {
        "name": "Test 8",
        "filepath1": "/users/cse453/secret/password.txt",
        "filepath2": "/users/cse453/secret/password#.txt",
        "expected": False,
    },
    # Test 9
    # Scenario: Filepath2 includes a white space.
    {
        "name": "Test 9",
        "filepath1": "/users/cse453/secret/password.txt",
        "filepath2": "/users/cse453/secret/password.txt ",
        "expected": False,
    },
    # Test 10
    # Scenario: Filepath2 uses a cyrillic character for letter "a" in the filename.
    {
        "name": "Test 10",
        "filepath1": "/users/cse453/secret/password.txt",
        "filepath2": "/users/cse453/secret/pаssword.txt",
        "expected": False,
    },
    # Test 11
    # Scenario: On a Windows system, filepath2 contains the cyrillic capital letter "A". Windows paths are case-insensitive.
    {
        "name": "Test 11",
        "filepath1": "C:\\USERS\\CSE453\\SECRET\\PASSWORD.TXT",
        "filepath2": "C:\\USERS\\CSE453\\SECRET\\PАSSWORD.TXT",
        "expected": False,
    }
]
test_cases2 = [
    # Test Case Set 2: Homographs
    # Test 12
    # Scenario: On a Windows system, filepath1 and filepath2 are exactly the same using back slashes.   
    {
        "name": "Test 12",
        "filepath1": "C:\\users\\cse453\\secret\\password.txt",
        "filepath2": "C:\\users\\cse453\\secret\\password.txt",
        "expected": True,
    },
    # Test 13
    # Scenario: On a Windows, Macintosh, or Linux system, Filepath1 and filepath2 are exactly the same, using forward slashes.
    {
        "name": "Test 13",
        "filepath1": "C:/users/cse453/secret/password.txt",
        "filepath2": "C:/users/cse453/secret/password.txt",
        "expected": True,
    },
    # Test 14
    # Scenario: On a Windows system, both filepaths contain the same capital letters. Windows paths are case-insensitive.
    {
        "name": "Test 14",
        "filepath1": "C:\\USERS\\CSE453\\SECRET\\PASSWORD.TXT",
        "filepath2": "C:\\USERS\\CSE453\\SECRET\\PASSWORD.TXT",
        "expected": True,
    },
    # Test 15
    # Scenario: On a Windows system, filepath2 contains capital letters. Windows paths are case-insensitive.
    {
        "name": "Test 15",
        "filepath1": "C:\\users\\cse453\\secret\\password.txt",
        "filepath2": "C:\\USERS\\CSE453\\SECRET\\PASSWORD.TXT",
        "expected": True,
    },
    # Test 16
    # Scenario: In filepath2 the .\ symbol represents the current directory.
    {
        "name": "Test 16",
        "filepath1": "C:\\users\\cse453\\secret\\password.txt",
        "filepath2": "C:\\users\\cse453\\.\\secret\\password.txt",
        "expected": True,
    },
    # Test 17
    # Scenario: In filepath2 the ..\ symbol represents the parent directory on a Windows system.
    {
        "name": "Test 17",
        "filepath1": "C:\\users\\cse453\\secret\\password.txt",
        "filepath2": "C:\\users\\cse453\\secret\\..\\secret\\password.txt",
        "expected": True,
    },
]


# This function allows the user to select options from a menu.
def menu():
    print("\n1. Run test cases")
    print("2. Enter file paths manually")
    print("3. Exit")
    choice = input("Enter your choice: ")
    return choice

# This converts an encoding (the input path) into some canon.
def canon(filepath: str) -> str:
    parent_directory_token = ".."
    current_directory_token = "."

    os_dir_separator = "\\" if platform.system() == "Windows" else "/"

    list_directories = filepath.split(os_dir_separator)

    temp_token = ""
    abs_path = []
    for token in list_directories:
        if token == parent_directory_token and token != temp_token:
            temp_token = abs_path.pop()
        if token == parent_directory_token or token == current_directory_token:
            continue
        abs_path.append(token)
    return os_dir_separator.join(abs_path)


# Function to determine if filepath1 and filepath2 are the same.
def homograph(filepath1: str, filepath2: str) -> bool:
    return canon(filepath1.lower()) == canon(filepath2.lower())

# This Function implements the menu, runs the test cases or manual inputs, prints test results, and calls other functions to execute.
def main():
    while True:
        choice = menu()
        if choice == "1":
            print("\nTest Case Set 1: Non-homographs")
            for test_case in test_cases1:
                print(test_case["name"])
                print(test_case["filepath1"])
                print(test_case["filepath2"])
                result = homograph(test_case["filepath1"], test_case["filepath2"])
                print("Expected:", test_case["expected"])
                print("Actual:", result)
                print("===================")
            print("\nTest Case Set 2: Homographs")
            for test_case in test_cases2:
                print(test_case["name"])
                print(test_case["filepath1"])
                print(test_case["filepath2"])
                result = homograph(test_case["filepath1"], test_case["filepath2"])
                print("Expected:", test_case["expected"])
                print("Actual:", result)
                print("===================")
        elif choice == "2":
            filepath1 = input("Enter the first file path: ")
            filepath2 = input("Enter the second file path: ")
            if homograph(filepath1, filepath2):
                print("The paths are homographs")
            else:
                print("The paths are non-homographs")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
