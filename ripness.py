# write in file using with() function
with open('swipe.txt','w') as file:
    file.write("The sky blushed with hues of lavender as the sun whispered its final goodbye.")
file.close()

# spilt file into words
with open('swipe.txt','r') as file:
    data = file.readlines()
    print("Words in this file are....")
    for line in data:
     word = line.split()
     print (word)
file.close()

