import os.path
import shutil

if __name__ == '__main__':
    print("Generic numbers folder (#) or folder for each individual number?")
    print("1) Generic")
    print("2) Individual")
    numAnswer = input()
    while numAnswer != "1" and numAnswer != "2":
        print("Enter 1 or 2")
        numAnswer = input()
        if numAnswer == "1 or 2":
            print("Very funny")

    if numAnswer == "1":
        letters = ["#", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                   "T", "U", "V", "W", "X", "Y", "Z"]
    else:
        letters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                   "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

    print("Upper case folder names, or all lower?")
    print("1) Upper")
    print("2) Lower")
    caseAnswer = input()
    while caseAnswer != "1" and caseAnswer != "2":
        print("Enter 1 or 2")
        caseAnswer = input()
        if caseAnswer == "1 or 2":
            print("Very funny")

    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

    print("Create folders even if no matching file exists?")
    print("1) Yes")
    print("2) No")
    folderAnswer = input()
    while folderAnswer != "1" and folderAnswer != "2":
        print("Enter 1 or 2")
        folderAnswer = input()
        if folderAnswer == "1 or 2":
            print("Very funny")

    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

    currDir = os.getcwd()
    files = [i for i in os.listdir(currDir) if not os.path.isdir(i)]
    files.sort()

    if folderAnswer == "1":
        for letter in letters:
            if caseAnswer == "1":
                newPath = os.path.join(currDir, letter.upper())
            else:
                newPath = os.path.join(currDir, letter.lower())

            if not os.path.isdir(newPath):
                os.mkdir(newPath)
                print("Created folder " + newPath)

    for file in files:
        if file != os.path.basename(__file__):
            fileMinusSpecials = ''.join(i for i in os.path.splitext(file)[0] if i.isalnum())
            if len(fileMinusSpecials) > 0:
                firstChar = fileMinusSpecials[0]
                if firstChar.isnumeric():
                    if numAnswer == "1":
                        firstChar = "#"

                if caseAnswer == "1":
                    newPath = os.path.join(currDir, firstChar.upper())
                    if not os.path.isdir(newPath):
                        os.mkdir(newPath)
                        print("Created folder " + newPath)

                    shutil.move(os.path.join(currDir, file), os.path.join(currDir, firstChar.upper(), file))
                elif caseAnswer == "2":
                    newPath = os.path.join(currDir, firstChar.lower())
                    if not os.path.isdir(newPath):
                        os.mkdir(newPath)
                        print("Created folder " + newPath)

                    shutil.move(os.path.join(currDir, file), os.path.join(currDir, firstChar.lower(), file))
            else:
                print("Found file whose name consists entirely of special characters - skipping...")

    print("All done.")
    input()
