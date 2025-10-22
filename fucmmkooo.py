# create a new file
new_file = open('mime.txt','x')
new_file.close()


# check if a file exists
import os
print("Checking if my_file exists or not....")
if os.path.exists("mine1.txt"):
    os.remove("my_file.txt")
else:
    print("The file does not exist")

# create a new if it doesn't
my_file = open("my_file.txt",'w')
my_file.write("Every sunrise is an invitation to begin again.")
my_file.close()


#delete file named swipe.txt
os.rmdir('swipe.txt')

# delete the folder
os.rmdir('Folder')