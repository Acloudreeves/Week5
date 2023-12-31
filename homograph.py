# This program takes an input of two file paths and compares them to verify if they are homographs or non-homographs.

import platform

# This dictionary contains the test cases for both homographs and non-homographs on a Linux or Macintosh *nix based system.
nix_cases = [
    # Test 1
    # Scenario: Filepath2 uses ./ to specify a current directory. 
    {
        "name": "Test 1",
        "filepath1": "/users/cse453/secret/password.txt",
        "filepath2": "/users/cse453/./secret/password.txt",
        "expected": "Homograph",
    },
    # Test 2
    # Scenario: Filepath2 uses ../ to specify a parent directory. 
    {
        "name": "Test 2",
        "filepath1": "/users/cse453/secret/password.txt",
        "filepath2": "/users/cse453/secret/../secret/password.txt",
        "expected": "Homograph",
    },

    # Test 3
    # Scenario: Filepath2 includes a white space.
    {
        "name": "Test 3",
        "filepath1": "/users/cse453/secret/password.txt",
        "filepath2": "/users/cse453/secret/password.txt ",
        "expected": "Homograph",
    },

    # Homograph
    # Test 4
    # Scenario: Filepath2 uses ..\ to specify a parent directory incorrectly.
    {
        "name": "Test 4",
        "filepath1": "/users/cse453/secret/password.txt",
        "filepath2": "/users/cse453/../password.txt",
        "expected": "Non-Homograph",
    },
    # Test 5
    # Scenario: Filepath2 uses .\ to specify the current directory incorrectly on a Windows system.
    {
        "name": "Test 5",
        "filepath1": "/users/cse453/secret/password.txt",
        "filepath2": "/users/cse453/./password.txt",
        "expected": "Non-Homograph",
    },
    # Test 6
    # Scenario: Filepath2 has a different /cse453/ directory name in the path (Capital "S" instead of "5").
    {
        "name": "Test 6",
        "filepath1": "/users/cse453/secret/password.txt",
        "filepath2": "/users/cse4S3/secret/password.txt",
        "expected": "Non-Homograph",
    },

    # Test 7
    # Scenario: Filepath2 includes a special character, #.
    {
        "name": "Test 7",
        "filepath1": "/users/cse453/secret/password.txt",
        "filepath2": "/users/cse453/secret/password#.txt",
        "expected": "Non-Homograph",
    },
    # Test 8
    # Scenario: Filepath2 uses a cyrillic character for letter "a" in the filename.
    {
        "name": "Test 8",
        "filepath1": "/users/cse453/secret/password.txt",
        "filepath2": "/users/cse453/secret/pаssword.txt",
        "expected": "Non-Homograph",
    },
    # Test 9 
    # Scenario: Filepath1 and filepath2 are exactly the same.
    {
        "name": "Test 9",
        "filepath1": "/users/cse453/secret/password.txt",
        "filepath2": "/users/cse453/secret/password.txt",
        "expected": "Homograph",
    },
]
win_cases = [
    # Test 1
    # Scenario: On a Windows system, filepath1 is on the C: drive, while filepath2 specifies a different drive.
    {
        "name": "Test 1",
        "filepath1": "C:\\users\\cse453\\secret\\password.txt",
        "filepath2": "D:\\users\\cse453\\secret\\password.txt",
        "expected": "Non-Homograph",
    },
    # Test 2 Scenario: On a Windows system, filepath1 uses "\" while filepath2 uses "/". 
    {
        "name": "Test 2",
        "filepath1": "C:\\users\\cse453\\secret\\password.txt",
        "filepath2": "C:/users/cse453/secret/password.txt",
        "expected": "Homograph",
    },
    # Test 3 Scenario: On a Windows system, filepath2 contains the cyrillic capital letter "A". Windows paths are
    # case-insensitive.
    {
        "name": "Test 3",
        "filepath1": "C:\\USERS\\CSE453\\SECRET\\PASSWORD.TXT",
        "filepath2": "C:\\USERS\\CSE453\\SECRET\\PАSSWORD.TXT",
        "expected": "Non-Homograph",
    },
    # Test 4
    # Scenario: On a Windows system, filepath1 and filepath2 are exactly the same using back slashes.   
    {
        "name": "Test 4",
        "filepath1": "C:\\users\\cse453\\secret\\password.txt",
        "filepath2": "C:\\users\\cse453\\secret\\password.txt",
        "expected": "Homograph",
    },
    # Test 5 Scenario: On a Windows system, both filepaths contain the same capital letters. Windows paths are
    # case-insensitive.
    {
        "name": "Test 5",
        "filepath1": "C:\\USERS\\CSE453\\SECRET\\PASSWORD.TXT",
        "filepath2": "C:\\USERS\\CSE453\\SECRET\\PASSWORD.TXT",
        "expected": "Homograph",
    },
    # Test 6
    # Scenario: On a Windows system, filepath2 contains capital letters. Windows paths are case-insensitive.
    {
        "name": "Test 6",
        "filepath1": "C:\\users\\cse453\\secret\\password.txt",
        "filepath2": "C:\\USERS\\CSE453\\SECRET\\PASSWORD.TXT",
        "expected": "Homograph",
    },
    # Test 7
    # Scenario: In filepath2 the .\ symbol represents the current directory.
    {
        "name": "Test 7",
        "filepath1": "C:\\users\\cse453\\secret\\password.txt",
        "filepath2": "C:\\users\\cse453\\.\\secret\\password.txt",
        "expected": "Homograph",
    },
    # Test 8
    # Scenario: In filepath2 the ..\ symbol represents the parent directory on a Windows system.
    {
        "name": "Test 8",
        "filepath1": "C:\\users\\cse453\\secret\\password.txt",
        "filepath2": "C:\\users\\cse453\\secret\\..\\secret\\password.txt",
        "expected": "Homograph",
    }
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

    # Define the tokens for the parent directory and the current directory, respectively. 
    parent_directory_token = ".."
    current_directory_token = "."

    # Set the directory separator based on the operating system.
    os_dir_separator = "\\" if platform.system() == "Windows" else "/"

    # Replace the directory separators in the input file path with the appropriate separator for the current operating system.
    filepath = filepath.replace("/" if platform.system() == "Windows" else "\\", os_dir_separator)

    # Remove any leading or trailing whitespace from the file path.
    filepath = filepath.strip()

    # Split the file path into a list of directories. 
    list_directories = filepath.split(os_dir_separator)

    temp_token = ""
    abs_path = []

    # Iterate over each token (directory) in the list of directories.  
    for token in list_directories:

        # If not the same as the previous token, remove the last directory from the absolute path.     
        if token == parent_directory_token and token != temp_token:
            temp_token = abs_path.pop()

        # If the token is a parent directory token and it’s not the same as the previous token, skip to the next iteration. Otherwise, add the token to the absolute path. 
        if token == parent_directory_token or token == current_directory_token:
            continue
        abs_path.append(token)

    # Join all directories in the absolute path with the appropriate directory separator and return the result. 
    return os_dir_separator.join(abs_path)


# Function to determine if filepath1 and filepath2 are the same, taking into account case sensitivity and relative paths. 
def homograph(filepath1: str, filepath2: str) -> str:

    # Convert both file paths to lowercase and then call the canon function. Return “Homograph” if the absolute paths of both file paths are the same (ignoring case), and “Non-Homograph” otherwise.
    return "Homograph" if canon(filepath1.lower()) == canon(filepath2.lower()) else "Non-Homograph"


# This Function implements the menu, runs the test cases or manual inputs, prints test results, and calls other functions to execute.
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
            print("The paths are non-homographs") if homograph(filepath1, filepath2) else print("The paths are homographs")
            continue
        if choice == "4":
            break
        print("Invalid choice. Please select from the available choices.")

# This function runs a for-loop for each test in the test cases dictionary. Each loop gets the two file paths from the test_cases dictionary, prints them, and then calls the homograph() function to compare the two paths. The expected and actual results are then printed.  
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
