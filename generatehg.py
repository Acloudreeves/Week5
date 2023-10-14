def generate_non_homographs(forbidden_path):
    non_homographs = []
    non_homographs.append(forbidden_path.replace('secret/', ''))
    non_homographs.append(forbidden_path.replace('secret/', '../'))
    non_homographs.append(forbidden_path.replace('secret/', 'secret/../'))
    non_homographs.append(forbidden_path.replace('secret/', 'secret/./../'))
    non_homographs.append(forbidden_path.replace("password", "p\x61ssword"))  # "password" (UTF-8 "a")
    non_homographs.append(forbidden_path.replace("password", "p\u0061ssword"))  # "password" (ASCii "a")
    non_homographs.append(forbidden_path.replace("password", "p\u0430ssword"))  # "pаssword" (cyrillic "a")
    non_homographs.append(forbidden_path.replace("password", "p\u03B1ssword"))  # "pαssword" (Greek "a")
    non_homographs.append(forbidden_path.replace("password", "p\uFF41ssword"))  # "pａssword"
    non_homographs.append(forbidden_path.replace("password", "p\u00E3ssword"))  # "pãssword"
    non_homographs.append(forbidden_path.replace("password", "p\u00E4ssword"))  # "pässword"
    non_homographs.append(forbidden_path.replace("password", "p\u04D3ssword"))  # "pӓssword"
    non_homographs.append(forbidden_path.replace("password", "p\u0101ssword"))  # "pāssword"
    non_homographs.append(forbidden_path.replace("password", "p\u00E0ssword"))  # "pàssword"
    non_homographs.append(forbidden_path.replace("password", "p\u00E1ssword"))  # "pássword"
    non_homographs.append(forbidden_path.replace("password", "p\u00E2ssword"))  # "pâssword"
    non_homographs.append(forbidden_path.replace("password", "p\u01CEssword"))  # "pǎssword"
    non_homographs.append(forbidden_path.replace("password", "p\u0203ssword"))  # "pȃssword"
    non_homographs.append(forbidden_path.replace("password", "p\u00E5ssword"))  # "påssword"
    non_homographs.append(forbidden_path.replace("password", "p\u1EA3ssword"))  # "pảssword"
    non_homographs.append(forbidden_path.replace("password", "p\u00E6ssword"))  # "pæssword"
    non_homographs.append(forbidden_path.replace("password", "p\u0103ssword"))  # "păssword"
    non_homographs.append(forbidden_path.replace("password", "p\u0105ssword"))  # "pąssword"
    non_homographs.append(forbidden_path.replace("password", "p\u01DFssword"))  # "pǟssword"
    non_homographs.append(forbidden_path.replace("password", "p\u018Cssword"))  # "pƌssword"
    non_homographs.append(forbidden_path.replace("password", "p\u01A3ssword"))  # "pƣssword"
    non_homographs.append(forbidden_path.replace("password", "p\u01E1ssword"))  # "pǡssword"
    non_homographs.append(forbidden_path.replace("password", "p\u0201ssword"))  # "pȁssword"
    non_homographs.append(forbidden_path.replace("password", "p\u0227ssword"))  # "pȧssword"
    non_homographs.append(forbidden_path.replace("password", "\u00FEassword")) # "þassword"
    non_homographs.append(forbidden_path.replace("password", "\u03F8assword")) # "ϸassword" (Greek "p")
    non_homographs.append(forbidden_path.replace("password", "\u03FCassword")) # "ϼassword" (Greek "p")
    non_homographs.append(forbidden_path.replace("password", "\u1D29assword")) # "ᴩassword" (Greek "p")
    non_homographs.append(forbidden_path.replace("password", "\u0440assword")) # "рassword" (Cyrillic "p")
    non_homographs.append(forbidden_path.replace("password", "\u0420assword")) # "Рassword" (Cyrillic "P")
    non_homographs.append(forbidden_path.replace("password", "pa\u0455\u0455word")) # "paѕѕword" (Cyrillic "ss")
    non_homographs.append(forbidden_path.replace("password", "pass\u0461ord")) # "passѡord" (Cyrillic "w")
    non_homographs.append(forbidden_path.replace("password", "pass\u0448ord")) # "passшord" (Cyrillic "ш")
    non_homographs.append(forbidden_path.replace("password", "pass\u0449ord")) # "passщord" (Cyrillic "щ")
    non_homographs.append(forbidden_path.replace("password", "P\u0410SSWORD"))  # "PАSSWORD" (Cyrillic "A")
    non_homographs.append(forbidden_path.replace("password", "P\u0041SSWORD"))  # "PASSWORD"
    non_homographs.append(forbidden_path.replace("password", "P\u0391SSWORD"))  # "PΑSSWORD"
    non_homographs.append(forbidden_path.replace("password", "P\uFF21SSWORD"))  # "PＡSSWORD"
    non_homographs.append(forbidden_path.replace("password", "PASS\u0460ORD")) # "PASSѠORD" (Cyrillic "W")
    non_homographs.append(forbidden_path.replace("password", "PＡSSWORD"))  # "PＡSSWORD"
    


    
    return non_homographs
    

forbidden_path = '/home/user/secret/password.txt'
non_homographs = generate_non_homographs(forbidden_path)
print(non_homographs)


"""
Report Ideas
Terms:
e: The encoding in this scenario is the file path, which is a string that represents the location of a file on the file system. For example, “C:\users\cse453\secret\password.txt” is an encoding.
r: There is no requirement to have a rendition (r) in the code.
R(): There is no requirement to write a separate rendering function for this assignment.
c: The canon is a canonical representation of a file path, which is a unique and simplified way of writing a file path. For example, “/users/cse453/secret/password.txt” is a canon for the file path “/users/cse453/./secret/password.txt”.
C(): The canonicalization function is a function that takes an encoding (a file path) and returns a canon (a canonical representation of the file path). In the code, this is the "canon()" function.
H(): The homograph function is a function that takes two encodings (two file paths) and returns True if they are homographs (they refer to the same file) or False otherwise. This function uses the canonicalization function to compare the two encodings. In the code, this is the "homograph()" function. 


"""