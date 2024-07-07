 # Q : Copy content from one file and paste in another file using file functions.

with open("source_file.txt" , "r") as source_file:
    
    content = source_file.read()

with open("destination_file.txt" , "w") as destination_file:

    destination_file.write(content)

print("Content copied successfully!")

