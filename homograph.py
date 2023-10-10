# This program is meant to take an input of two file paths and compare them to verify if they are homographs.


# This converts an encoding (the input path) into some canon.
def canon(filepath1, filepath2):
    # code here
    pass


# Function to determine if filepath1 and filepath2 are the same
def homograph(filepath1, filepath2):
    # code here
    canon(filepath1, filepath2)


def main():
    firstpath = input("Specify the first file name")
    secondpath = input("Specify the second file name\n")

    if homograph(firstpath, secondpath):
        print("The paths are homographs")
    else:
        print("The paths are not homographs")


if __name__ == "__main__":
    main()
