def test_tautology() -> dict:
    return {
        "Dan": "'i_dont_have' OR '1'='1",
        "Stan": "' OR 'a'='a",
        "Fran": "' OR '2'='2",
        "Nan": "' OR 'b'='b",
        "Jan": "' OR '3'='3"
    }


def test_union() -> dict:
    return {
        "Dan": "'nope' UNION SELECT * FROM users --",
        "Stan": "'' UNION SELECT username, password FROM users --",
        "Fran": "'nothing' UNION SELECT * FROM admin --",
        "Nan": "'weak' UNION SELECT email, password FROM users --",
        "Jan": "'something' UNION SELECT * FROM users WHERE '1'='1' --"
    }


def test_comment() -> dict:
    return {
        "Dan": "'nothing' OR '1'='1' --",
        "Stan": "'nope' OR 'a'='a' /*",
        "Fran": "'smthg' OR '2'='2' #",
        "Nan": "'' OR 'b'='b' -- -",
        "Jan": "'forgot' OR '3'='3' --+"
    }


def test_additional_statement() -> dict:
    return {
        "Dan": "'nope'; DROP TABLE users; --",
        "Stan": "'forgot'; DELETE FROM users; --",
        "Fran": "'weak'; INSERT INTO users VALUES ('Fran', 'password'); --",
        "Nan": "''; UPDATE users SET password='password'; --",
        "Jan": "'something'; SELECT * FROM users; --"
    }


def test_valid() -> dict:
    return {
        "Dan": "password123",
        "Stan": "Stan_456",
        "Fran": "Fran7890",
        "Nan": "Nan_1234",
        "Jan": "Jan5678"
    }


def general_query_generator(username, password):
    return f"SELECT * FROM users WHERE username = {username} AND password = {password}"


def weak_mitigation_query_wrapper(username: str, password: str) -> str:
    """Some wrapper code over here"""
    return general_query_generator(username, password)


def strong_mitigation_query_wrapper(username: str, password: str) -> str:
    """Some wrapper code over here"""
    return general_query_generator(username, password)


def run_test(cases: dict):
    for username, password in cases.items():
        query = general_query_generator(username, password)
        print(f"Query for {username}: {query}")


def driver_program():
    print_menu()

    while True:
        choice = input("Please make a choice: ")
        if choice == "1":
            print("\nTest Validation")
            run_test(test_valid())
            continue
        if choice == "2":
            print("\nTest Tautology")
            run_test(test_tautology())
            continue
        if choice == "3":
            print("\nTest Union")
            run_test(test_union())
            continue
        if choice == "4":
            print("\nTest Additional Statement")
            run_test(test_additional_statement())
            continue
        if choice == "5":
            print("\nTest Comment")
            run_test(test_comment())
            continue
        if choice == "6":
            print("\nTest Weak Tautology")
            run_test(test_tautology())
            continue
        if choice == "7":
            print("\nTest Weak Union")
            run_test(test_union())
            continue
        if choice == "8":
            print("\nTest Weak Additional Statement")
            run_test(test_additional_statement())
            continue
        if choice == "9":
            print("\nTest Weak Comment")
            run_test(test_comment())
            continue
        if choice == "10":
            print("\nTest Strong Tautology")
            run_test(test_tautology())
            continue
        if choice == "11":
            print("\nTest Strong Union")
            run_test(test_union())
            continue
        if choice == "12":
            print("\nTest Strong Additional Statement")
            run_test(test_additional_statement())
            continue
        if choice == "13":
            print("\nTest Strong Comment")
            run_test(test_comment())
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
    h. Display menu\n
    q. Exit\n""")


if __name__ == "__main__":
    driver_program()
