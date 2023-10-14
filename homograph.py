# This program takes an input of two file paths and compares them to verify if they are homographs or non-homographs.

import platform

# This dictionary contains the test cases for homographs and non-homographs. True = Homograph, False = Non-Homograph
nix_cases = [
    # Non-Homograph
    # Test 1
    # Scenario: Filepath2 uses ./ to specify a current directory. On a Windows system, only .\ is valid.
    {
        "name": "Test 1",
        "filepath1": "/users/cse453/secret/password.txt",
        "filepath2": "/users/cse453/./secret/password.txt",
        "expected": "Non-Homograph",
    },
    # Test 2
    # Scenario: Filepath2 uses ../ to specify a parent directory. On a Windows system, only ..\ is valid.
    {
        "name": "Test 2",
        "filepath1": "/users/cse453/secret/password.txt",
        "filepath2": "/users/cse453/secret/../secret/password.txt",
        "expected": "Non-Homograph",
    },

    # Test 3
    # Scenario: Filepath2 includes a white space.
    {
        "name": "Test 3",
        "filepath1": "/users/cse453/secret/password.txt",
        "filepath2": "/users/cse453/secret/password.txt ",
        "expected": "Non-Homograph",
    },

    # Homograph
    # Test 4
    # Scenario: Filepath2 uses ..\ to specify a parent directory incorrectly on a Windows system.
    {
        "name": "Test 4",
        "filepath1": "\\users\\cse453\\secret\\password.txt",
        "filepath2": "\\users\\cse453\\..\\password.txt",
        "expected": "Homograph",
    },
    # Test 5
    # Scenario: Filepath2 uses .\ to specify the current directory incorrectly on a Windows system.
    {
        "name": "Test 5",
        "filepath1": "\\users\\cse453\\secret\\password.txt",
        "filepath2": "\\users\\cse453\\.\\password.txt",
        "expected": "Homograph",
    },
    # Test 6
    # Scenario: Filepath2 has a different /cse453/ directory name in the path (Capital "S" instead of "5").
    {
        "name": "Test 6",
        "filepath1": "/users/cse453/secret/password.txt",
        "filepath2": "/users/cse4S3/secret/password.txt",
        "expected": "Homograph",
    },

    # Test 7
    # Scenario: Filepath2 includes a special character, #.
    {
        "name": "Test 7",
        "filepath1": "/users/cse453/secret/password.txt",
        "filepath2": "/users/cse453/secret/password#.txt",
        "expected": "Homograph",
    },
    # Test 8
    # Scenario: Filepath2 uses a cyrillic character for letter "a" in the filename.
    {
        "name": "Test 8",
        "filepath1": "/users/cse453/secret/password.txt",
        "filepath2": "/users/cse453/secret/pаssword.txt",
        "expected": "Homograph",
    }
]
win_cases = [
    # Test 1
    # Scenario: On a Windows system, filepath1 is on the C: drive, while filepath2 specifies a different drive.
    {
        "name": "Test 1",
        "filepath1": "C:\\users\\cse453\\secret\\password.txt",
        "filepath2": "D:\\users\\cse453\\secret\\password.txt",
        "expected": "Homograph",
    },
    # Test 2 Scenario: On a Windows system, filepath1 uses "\" while filepath2 uses "/". Windows will accept either
    # one, but does not treat them as equivalent.
    {
        "name": "Test 2",
        "filepath1": "C:\\users\\cse453\\secret\\password.txt",
        "filepath2": "C:/users/cse453/secret/password.txt",
        "expected": "Non-Homograph",
    },
    # Test 3 Scenario: On a Windows system, filepath2 contains the cyrillic capital letter "A". Windows paths are
    # case-insensitive.
    {
        "name": "Test 3",
        "filepath1": "C:\\USERS\\CSE453\\SECRET\\PASSWORD.TXT",
        "filepath2": "C:\\USERS\\CSE453\\SECRET\\PАSSWORD.TXT",
        "expected": "Homograph",
    },
    # Test 4
    # Scenario: On a Windows system, filepath1 and filepath2 are exactly the same using back slashes.   
    {
        "name": "Test 4",
        "filepath1": "C:\\users\\cse453\\secret\\password.txt",
        "filepath2": "C:\\users\\cse453\\secret\\password.txt",
        "expected": "Non-Homograph",
    },
    # Test 5 Scenario: On a Windows, Macintosh, or Linux system, Filepath1 and filepath2 are exactly the same,
    # using forward slashes.
    {
        "name": "Test 5",
        "filepath1": "C:/users/cse453/secret/password.txt",
        "filepath2": "C:/users/cse453/secret/password.txt",
        "expected": "Non-Homograph",
    },
    # Test 6 Scenario: On a Windows system, both filepaths contain the same capital letters. Windows paths are
    # case-insensitive.
    {
        "name": "Test 6",
        "filepath1": "C:\\USERS\\CSE453\\SECRET\\PASSWORD.TXT",
        "filepath2": "C:\\USERS\\CSE453\\SECRET\\PASSWORD.TXT",
        "expected": "Non-Homograph",
    },
    # Test 7
    # Scenario: On a Windows system, filepath2 contains capital letters. Windows paths are case-insensitive.
    {
        "name": "Test 7",
        "filepath1": "C:\\users\\cse453\\secret\\password.txt",
        "filepath2": "C:\\USERS\\CSE453\\SECRET\\PASSWORD.TXT",
        "expected": "Non-Homograph",
    },
    # Test 8
    # Scenario: In filepath2 the .\ symbol represents the current directory.
    {
        "name": "Test 8",
        "filepath1": "C:\\users\\cse453\\secret\\password.txt",
        "filepath2": "C:\\users\\cse453\\.\\secret\\password.txt",
        "expected": "Non-Homograph",
    },
    # Test 9
    # Scenario: In filepath2 the ..\ symbol represents the parent directory on a Windows system.
    {
        "name": "Test 9",
        "filepath1": "C:\\users\\cse453\\secret\\password.txt",
        "filepath2": "C:\\users\\cse453\\secret\\..\\secret\\password.txt",
        "expected": "Non-Homograph",
    },
]


# This function allows the user to select options from a menu.
def menu():
    print("1. Run test cases Linux OS")
    print("2. Run test cases Windows OS")
    print("3. Enter file paths manually")
    print("4. Exit")
    choice = input("Enter your choice: ")
    return choice


# This converts an encoding (the input path) into some canon.
def canon(filepath: str) -> str:
    parent_directory_token = ".."
    current_directory_token = "."

    os_dir_separator = "\\" if platform.system() == "Windows" else "/"

    filepath = filepath.replace("/" if platform.system() == "Windows" else "\\", os_dir_separator)

    filepath = filepath.strip()
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
def homograph(filepath1: str, filepath2: str) -> str:
    return "Non-Homograph" if canon(filepath1.lower()) == canon(filepath2.lower()) else "Homograph"


# This Function implements the menu, runs the test cases or manual inputs, prints test results, and calls other
# functions to execute.
def main():
    while True:
        choice = menu()
        if choice == "1":
            print("\nTest Case Set 1: *nix base test cases")
            run_tests(nix_cases)
            continue
        if choice == "2":
            print("\nTest Case Set 2: Windows test cases")
            run_tests(win_cases)
            continue
        if choice == "3":
            filepath1 = input("Enter the first file path: ")
            filepath2 = input("Enter the second file path: ")
            print("The paths are non-homographs") if homograph(filepath1, filepath2) else print("The paths are "
                                                                                                "homographs")
            continue
        if choice == "4":
            break
        print("Invalid choice. Please chose out of available.")


def run_tests(cases):
    for tests in cases:
        print(tests["name"])
        print(tests["filepath1"])
        print(tests["filepath2"])
        result = homograph(tests["filepath1"], tests["filepath2"])
        print("Expected:", tests["expected"])
        print("Actual:", result)
        print("===================")


if __name__ == "__main__":
    main()
