"""
Creating a note-taking program.
It prompts the user to enter a file name.
If the file name does not exist they are prompted them to enter the text.
After the text is enterred, the file is saved and program ends.
If the file name exists user can either read, delete and start over or append.
ASper extra credit, the user can also choose to replace a single line.
"""
import os
existFile = open("existFile", "w")
existFile.write("Line 1\nLine 2\nLine 3\n")
name = input("Enter a filename : ")
print("Filename entered is :",name)
if os.path.isfile(name) == True:
    print("File exists")
    print("1 : Read the file\n2 : Delete file and start over\n3 : Append to file")
    choice = int(input("Enter your choice(1, 2, 3) : "))
    if choice == 1:
        print("You have chosen to read the file")
        print("Contents of file : ")
        existFile.close()
        existFile = open("existFile", "r")
        print(existFile.read())
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("End of program")
    elif choice == 2:
        print("You have chosen to delete the file and start over")
        existFile.close()
        os.remove("./" + "existFile")
        newFile = open("newFile", "w")
        print("A new empty file called newFile has been created")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("End of program")
    elif choice == 3:
        print("You have chosen to append the file")
        existFile.close()
        existFile = open("existFile", "a")
        appendText = input("Enter the text you want to append : ")
        existFile.write(appendText)
        existFile.close()
        existFile = open("existFile", "r")
        print("The appended file: ")
        print(existFile.read())
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("End of program")
        existFile.close()
    else:
        print("Invalid choice entered")
else:
    print("This file does not exist so a new one is created")
    userFile = open("userFile", "w")
    text = input("Enter the text you want to write to the file : ")
    userFile.write(text)
    userFile.close()
    userFile = open("userFile", "r")
    print("The updated file :")
    print(userFile.read())
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("End of program")
    userFile.close()
existFile.close() #Closing it again just in case
"""
End of program,
Thank you!
"""
