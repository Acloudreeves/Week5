def generate_non_homographs(forbidden_path):
    non_homographs = []
    non_homographs.append(forbidden_path.replace("secret/", ""))
    non_homographs.append(forbidden_path.replace("secret/", "../"))
    non_homographs.append(forbidden_path.replace("secret/", "secret/../"))
    non_homographs.append(forbidden_path.replace("secret/", "secret/./../"))
    non_homographs.append(
        forbidden_path.replace("password", "p\u0061ssword"))  # "password"
    non_homographs.append(
        forbidden_path.replace("password", "p\uFF21ssword")
    )  # "pＡssword"
    non_homographs.append(
        forbidden_path.replace("password", "p\u0410ssword")
    )  # "pАssword"
    non_homographs.append(
        forbidden_path.replace("password", "p\u0041ssword")
    )  # "password"
    # non_homographs.append(forbidden_path.replace("password", "p\u0391ssword"))
    # non_homographs.append(forbidden_path.replace("password", "p\u0430ssword"))
    # non_homographs.append(forbidden_path.replace("password", "p\uFF41ssword"))
    # non_homographs.append(forbidden_path.replace("password", "p\u04D3ssword"))
    # non_homographs.append(forbidden_path.replace("password", "p\u0101ssword"))
    # non_homographs.append(forbidden_path.replace("password", "p\u01CEssword"))
    # non_homographs.append(forbidden_path.replace("password", "p\u0203ssword"))
    # non_homographs.append(forbidden_path.replace("password", "p\u00E0ssword"))
    # non_homographs.append(forbidden_path.replace("password", "p\u00E1ssword"))
    # non_homographs.append(forbidden_path.replace("password", "p\u00E2ssword"))
    # non_homographs.append(forbidden_path.replace("password", "p\u1EA3ssword"))
    # non_homographs.append(forbidden_path.replace("password", "p\u00E6ssword"))
    # non_homographs.append(forbidden_path.replace("password", "p\u00E7ssword"))
    # non_homographs.append(forbidden_path.replace("password", "p\u00E5ssword"))
    # non_homographs.append(forbidden_path.replace("password", "p\u00E4ssword"))
    # non_homographs.append(forbidden_path.replace("password", "p\u00E3ssword"))
    # non_homographs.append(forbidden_path.replace("password", "p\u00FCssword"))
    # non_homographs.append(forbidden_path.replace("password", "\u00FEassword")) # "þassword"
    # non_homographs.append(forbidden_path.replace("password", "þassword")) # "þassword"
    return non_homographs


forbidden_path = "/home/user/secret/password.txt"
non_homographs = generate_non_homographs(forbidden_path)
print("non_homographs")
print(non_homographs)
