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
            "Dan": "nothing' OR '1'='1' -- AND role = 'user'",
            "Stan": "nope' OR 'a'='a' /* AND status = 'active'",
            "Fran": "smthg' OR '2'='2' # AND account_type = 'standard'",
            "Nan": "' OR 'b'='b' -- AND is_locked = 0",
            "Jan": "forgot' OR '3'='3' -- AND num_attempts < 5"
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
    sanitized_username = username.replace("'", "' --")
    sanitized_password = password.replace("'", "' --")
    # uses comments to turn attacks into a comment so the attack code never gets executed.
    return general_query_generator(sanitized_username, sanitized_password)


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
            display(weak_mitigation_query_wrapper(
                username, password), username)
            continue
        if test_type == 'strong':
            display(strong_mitigation_query_wrapper(
                username, password), username)


def display(query, username):
    print(f"Query for {username}: {query}")


def driver_program():
    print_menu()

    while True:
        choice = input("Please make a choice: ")
        if choice == "1":
            print("\nRun Validation and Vulnerability sets of tests")
            run_tests(test_valid())
            run_tests(test_tautology())
            run_tests(test_union())
            run_tests(test_additional_statement())
            run_tests(test_comment())
            continue
        if choice == "2":
            print("\nRun Weak set of tests")
            test_type = 'weak'
            run_tests(test_tautology(), test_type=test_type)
            run_tests(test_union(), test_type=test_type)
            run_tests(test_additional_statement(), test_type=test_type)
            run_tests(test_comment(), test_type=test_type)
            continue
        if choice == "3":
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
    1. Set of tests without any Mitigation\n
    2. Set of Weak Mitigation Tests\n
    3. Set of Strong Mitigation Tests\n
    h. Display menu\n
    q. Exit\n""")


if __name__ == "__main__":
    driver_program()
