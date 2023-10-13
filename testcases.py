
"""
Test Case Set 1: Non-homographs
Requirements: 
    1. Non-homographs represent file paths that are similar to, but different than, the forbidden file.
    2. Test the various symbols provided by my system (Windows, Macintosh or Linux) that are used to specify a path. (/, ./, ../, \, C:, D:, etc.)
    3. Create enough tests to capture all aspects of the path symbols for my system.
    """
print("Test Case Set 1: Non-homographs")

def main(filepath1, filepath2):
    return

# Test 1
# Scenario: On a Windows system, filepath1 is on the C: drive, while filepath2 specifies a different drive.
# Expected result: Non-homograph
print("Test 1")
filepath1 = "C:\\users\\cse453\\secret\\password.txt"
filepath2 = "D:\\users\\cse453\\secret\\password.txt"
main(filepath1, filepath2)
print("===================")

# Test 2
# Scenario: Filepath2 has a different /cse453/ directory name in the path (Capital "S" instead of "5").
# Expected result: Non-homograph
print("Test 2")
filepath1 = "/users/cse453/secret/password.txt"
filepath2 = "/users/cse4S3/secret/password.txt"
main(filepath1, filepath2)
print("===================")

# Test 3
# Scenario: Filepath2 uses /../ to specify a parent directory incorrectly.
# Expected result: Non-homograph
print("Test 3")
filepath1 = "/users/cse453/secret/password.txt"
filepath2 = "/users/cse453/../password.txt"
main(filepath1, filepath2)
print("===================")

# Test 4
# Scenario: Filepath2 uses ./ to specify the current directory, incorrectly.
# Expected result: Non-homograph
print("Test 4")
filepath1 = "/users/cse453/secret/password.txt"
filepath2 = "./cse453/secret/password.txt"
main(filepath1, filepath2)
print("===================")

# Test 5
# Scenario: Filepath2 uses a cyrillic character for letter "a" in the filename.
# Expected result: Non-homograph
print("Test 5")
filepath1 = "/users/cse453/secret/password.txt"
filepath2 = "/users/cse453/secret/pаssword.txt"
main(filepath1, filepath2)
print("===================")

# Test 6
# Scenario: Filepath2 includes a special character, #.
# Expected result: Non-homograph
print("Test 6")
filepath1 = "/users/cse453/secret/password.txt"
filepath2 = "/users/cse453/secret/password#.txt"
main(filepath1, filepath2)
print("===================")

# Test 7
# Scenario: Filepath2 includes a white space.
# Expected result: Non-homograph
print("Test 7")
filepath1 = "/users/cse453/secret/password.txt"
filepath2 = "/users/cse453/secret/password.txt "
main(filepath1, filepath2)
print("===================")

# Test 8
# Scenario: On a Windows system, filepath1 and filepath2 both contain capital letter, but filepath2 contains capital letters. Windows paths are case-insensitive.
# Expected result: Non-homograph
print("Test 8")    
filepath1 = "C:\\USERS\\CSE453\\SECRET\\PASSWORD.TXT"
filepath2 = "C:/USERS/CSE453/SECRET/PАSSWORD.TXT"
main(filepath1, filepath2)
print("===================")


"""
Test Case Set 2: Homographs
Requirements: 
    1. Homographs represent file paths that are equivalent to the forbidden file but are different strings.
    2. Test the various symbols provided by my system (Windows, Macintosh or Linux) that are used to specify a path. (/, ./, ../, \, C:, D:, etc.)
    3. Create enough tests to capture all aspects of the path symbols for my system.
    """
print("Test Case Set 2: Homographs")

# Test 1
# Scenario: On a Windows system, filepath1 and filepath2 are exactly the same using back slashes.
# Expected result: Homograph
print("Test 1")    
filepath1 = "C:\\users\\cse453\\secret\\password.txt"
filepath2 = "C:\\users\\cse453\\secret\\password.txt"
main(filepath1, filepath2)
print("===================")

# Test 2
# Scenario: On a Windows, Macintosh, or Linux system, Filepath1 and filepath2 are exactly the same, using forward slashes.
# Expected result: Non-homograph
print("Test 2")    
filepath1 = "C:/users/cse453/secret/password.txt"
filepath2 = "C:/users/cse453/secret/password.txt"
main(filepath1, filepath2)
print("===================")

# Test 3
# Scenario: On a Windows system, filepath1 uses "\" while filepath2 uses "/".
# Expected result: Homograph (both point to the same location)
print("Test 3")    
filepath1 = "C:\\users\\cse453\\secret\\password.txt"
filepath2 = "C:/users/cse453/secret/password.txt"
main(filepath1, filepath2)
print("===================")

# Test 3
# Scenario: On a Windows system, filepath1 is on the C: drive, while filepath2 specifies an administrative path (\\localhost\C$) (This is a UNC path that points to the same location, but requires administrative privileges.)
# Expected result: Homograph
print("Test 3")    
filepath1 = "C:\\users\\cse453\\secret\\password.txt"
filepath2 = "\\\\localhost\\C$\\users\\cse453\\secret\\password.txt"
main(filepath1, filepath2)
print("===================")

# Test 4
# Scenario: In filepath2 the .\ symbol represents the current directory.
# Expected result: Homograph
print("Test 4")    
filepath1 = "C:\\users\\cse453\\secret\\password.txt"
filepath2 = "C:\\users\\cse453\\.\\secret\\password.txt"
main(filepath1, filepath2)
print("===================")

# Test 5
# Scenario: In filepath2 the ../ symbol represents the parent directory.
# Expected result: Homograph
print("Test 5")    
filepath1 = "/users/cse453/secret/password.txt"
filepath2 = "/users/cse453/secret/../secret/password.txt"
main(filepath1, filepath2)
print("===================")

# Test 6
# Scenario: In filepath2 the ./ symbol represents the current directory.
# Expected result: Homograph
print("Test 6")    
filepath1 = "/users/cse453/secret/password.txt"
filepath2 = "/users/cse453/./secret/password.txt"
main(filepath1, filepath2)
print("===================")

# Test 7
# Scenario: On a Windows system, filepath2 contains capital letters. Windows paths are case-insensitive.
# Expected result: Homograph
print("Test 7")    
filepath1 = "C:\\users\\cse453\\secret\\password.txt"
filepath2 = "C:\\USERS\\CSE453\\SECRET\\PASSWORD.TXT" 
main(filepath1, filepath2)
print("===================")

# Test 8
# Scenario: On a Windows system, filepath2 contains capital letters. Windows paths are case-insensitive.
# Expected result: Homograph
print("Test 8")    
filepath1 = "C:/users/cse453/secret/password.txt"
filepath2 = "C:/USERS/CSE453/SECRET/PASSWORD.TXT" 
main(filepath1, filepath2)
print("===================")
