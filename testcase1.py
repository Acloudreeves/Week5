def generate_non_homographs(forbidden_path):
    non_homographs = []
    non_homographs.append(forbidden_path.replace("secret/", ""))
    non_homographs.append(forbidden_path.replace("secret/", "../"))
    non_homographs.append(forbidden_path.replace("secret/", "secret/../"))
    non_homographs.append(forbidden_path.replace("secret/", "secret/./../"))
    return non_homographs

forbidden_path = '/home/user/secret/password.txt'
non_homographs = generate_non_homographs(forbidden_path)
print(non_homographs)

