import re


def test_tautology() -> dict:
    return {
        "name": "Tautology test cases",
        "cases": {
            "Dan": "i_dont_have' OR '1'='1",
            "Stan": "' OR 'a'='a",
            "Fran": "miss' OR '2'='2",
            "Nan": "123' OR 'b'='b",
            "Jan": "554_' OR '3'='3"
        }
    }


def test_union() -> dict:
    return {
        "name": "Union test cases",
        "cases": {
            "Dan": "nope' UNION SELECT * FROM users --",
            "Stan": "' UNION SELECT username, password FROM users --",
            "Fran": "nothing' UNION SELECT * FROM admin --",
            "Nan": "weak' UNION SELECT email, password FROM users --",
            "Jan": "something' UNION SELECT * FROM users WHERE '1'='1' --"
        }
    }


def test_comment() -> dict:
    return {
        "name": "Comment test cases",
        "cases": {
            "Dan": "nothing' OR '1'='1' -- AND role = 'admin'",
            "Stan": "nope' OR 'a'='a' /* AND role = 'user'",
            "Fran": "smthg' OR '2'='2' # AND status = 'paid'",
            "Nan": "' OR 'b'='b' -- - ORDER BY role ASC ",
            "Jan": "forgot' OR '3'='3' --+ ORDER BY status DESC"
        }
    }


def test_additional_statement() -> dict:
    return {
        "name": "Additional Statement test cases",
        "cases": {
            "Dan": "nope'; DROP TABLE users; --",
            "Stan": "forgot'; DELETE FROM users; --",
            "Fran": "weak'; INSERT INTO users VALUES ('Fran', 'password'); --",
            "Nan": "'; UPDATE users SET password='password'; --",
            "Jan": "something'; SELECT * FROM users; --"
        }
    }


def test_valid() -> dict:
    return {
        "name": "Validity test cases",
        "cases": {
            "Dan": "password123",
            "Stan": "Stan_456",
            "Fran": "Fran7890",
            "Nan": "Nan_1234",
            "Jan": "Jan5678"
        }
    }


def general_query_generator(username, password):
    return f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"


def weak_mitigation_query_wrapper(username: str, password: str) -> str:
    """Some wrapper code over here"""
    return general_query_generator(username, password)


def strong_mitigation_query_wrapper(username: str, password: str) -> str:
    pattern = r"^(['])?(?P<UserName_Password>\w+)(['])?(.*)$"
    found = re.match(pattern, username)

    if not found:
        return "Your Username either isn't valid or can't be empty"
    valid_username = found.group('UserName_Password')

    found = re.match(pattern, password)

    if not found:
        return "Your Password either isn't valid or can't be empty"

    valid_password = found.group('UserName_Password')

    return general_query_generator(valid_username, valid_password)


def run_tests(test_set: dict, test_type="simple"):
    print("\n{}\n".format(test_set.get("name")))
    cases = test_set.get('cases')
    for username, password in cases.items():
        if test_type == 'simple':
            display(general_query_generator(username, password), username)
            continue
        if test_type == 'weak':
            display(weak_mitigation_query_wrapper(username, password), username)
            continue
        if test_type == 'strong':
            display(strong_mitigation_query_wrapper(username, password), username)


def display(query, username):
    print(f"Query for {username}: {query}")


def driver_program():
    print_menu()

    while True:
        choice = input("Please make a choice: ")
        if choice == "1":
            print("\nTest Validation")
            run_tests(test_valid())
            continue
        if choice == "2":
            print("\nTest Tautology")
            run_tests(test_tautology())
            continue
        if choice == "3":
            print("\nTest Union")
            run_tests(test_union())
            continue
        if choice == "4":
            print("\nTest Additional Statement")
            run_tests(test_additional_statement())
            continue
        if choice == "5":
            print("\nTest Comment")
            run_tests(test_comment())
            continue
        if choice == "6":
            print("\nTest Weak Tautology")
            run_tests(test_tautology(), test_type="weak")
            continue
        if choice == "7":
            print("\nTest Weak Union")
            run_tests(test_union(), test_type="weak")
            continue
        if choice == "8":
            print("\nTest Weak Additional Statement")
            run_tests(test_additional_statement(), test_type="weak")
            continue
        if choice == "9":
            print("\nTest Weak Comment")
            run_tests(test_comment(), test_type="weak")
            continue
        if choice == "10":
            print("\nTest Strong Tautology")
            run_tests(test_tautology(), test_type="strong")
            continue
        if choice == "11":
            print("\nTest Strong Union")
            run_tests(test_union(), test_type="strong")
            continue
        if choice == "12":
            print("\nTest Strong Additional Statement")
            run_tests(test_additional_statement(), test_type="strong")
            continue
        if choice == "13":
            print("\nTest Strong Comment")
            run_tests(test_comment(), test_type="strong")
            continue

        if choice == "14":
            print("\nRun Validation and Vulnerability sets of tests")
            run_tests(test_valid())
            run_tests(test_tautology())
            run_tests(test_union())
            run_tests(test_additional_statement())
            run_tests(test_comment())
            continue
        if choice == "15":
            print("\nRun Weak set of tests")
            test_type = 'weak'
            run_tests(test_tautology(), test_type=test_type)
            run_tests(test_union(), test_type=test_type)
            run_tests(test_additional_statement(), test_type=test_type)
            run_tests(test_comment(), test_type=test_type)
            continue
        if choice == "16":
            print("\nRun Strong set of tests")
            test_type = 'strong'
            run_tests(test_tautology(), test_type=test_type)
            run_tests(test_union(), test_type=test_type)
            run_tests(test_additional_statement(), test_type=test_type)
            run_tests(test_comment(), test_type=test_type)
            continue
        if choice == "h":
            print_menu()
            continue
        if choice == "q":
            break
        print("Invalid choice. Please chose out of available.")


def print_menu():
    print("""
    1. Test Validation\n
    2. Test Tautology\n
    3. Test Union query\n
    4. Test Additional Statement\n
    5. Test Comment\n    
    6. Test Weak Tautology\n
    7. Test Weak Union query\n
    8. Test Weak Additional Statement\n
    9. Test Weak Comment\n 
    10. Test Strong Tautology\n
    11. Test Strong Union query\n
    12. Test Strong Additional Statement\n
    13. Test Strong Comment\n
    14. Set of tests without any Mitigation\n
    15. Set of Weak Mitigation Tests\n
    16. Set of Strong Mitigation Tests\n
    h. Display menu\n
    q. Exit\n""")


if __name__ == "__main__":
    driver_program()
